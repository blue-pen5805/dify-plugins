from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage
from dify_plugin.file.file import File, FileType

import httpx
import json

class OpenAIModerationTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        text: str | None = tool_parameters.get("text")
        image: File | None = tool_parameters.get("image")
        model = "omni-moderation-latest"

        inputs = []
        if text:
            inputs.append({ "type": "text", "text": text })
        if image:
            if image.type != FileType.IMAGE:
                raise ValueError("Not a valid image file")

            if not image.url:
                raise ValueError("Image must have a URL")

            inputs.append({ "type": "image_url", "image_url": { "url": image.url } })

        if len(inputs) == 0:
            raise ValueError("Either text or image must be provided")

        base_url = self.runtime.credentials.get('api_base') or "https://api.openai.com/v1"
        url = f"{base_url}/moderations"
        headers = {
            "Authorization": f"Bearer {self.runtime.credentials['api_key']}",
            "Content-Type": "application/json",
        }
        data = {
            "input": inputs,
            "model": model,
        }
        response = httpx.post(url, headers=headers, json=data)

        if response.is_success:
            json_response = response.json()
            result = json_response["results"][0]

            flagged = result["flagged"]
            categories = result["categories"]
            category_scores = result["category_scores"]
            category_applied_input_types = result["category_applied_input_types"]

            unsafe_score = max(category_scores.values())
            flagged_categories = [category for category, is_flagged in categories.items() if is_flagged]
            applied_categories = [key for key, value in category_applied_input_types.items() if value]
            filtered_category_scores = {key: value for key, value in category_scores.items() if key in applied_categories}

            return [
                self.create_json_message(json_response),
                self.create_text_message("true" if flagged else "false"),
                self.create_variable_message("flagged", flagged),
                self.create_variable_message("unsafe_score", unsafe_score),
                self.create_variable_message("flagged_categories", flagged_categories),
                self.create_variable_message("category_scores", filtered_category_scores),
            ]
        else:
            raise ValueError(response.text)
