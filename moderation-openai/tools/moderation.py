from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

import httpx
import json

class OpenAIModerationTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        text = tool_parameters.get("text")
        image = tool_parameters.get("image")
        model = "omni-moderation-latest"

        inputs = []
        if text:
            inputs.append({ "type": "text", "text": text })
        if image:
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

            yield self.create_text_message(json.dumps(json_response))
            yield self.create_json_message(json_response)
            yield self.create_variable_message("flagged", result["flagged"])
            yield self.create_variable_message("categories", result["categories"])
            yield self.create_variable_message("category_scores", result["category_scores"])
            yield self.create_variable_message("category_applied_input_types", result["category_applied_input_types"])
        else:
            raise ValueError(response.text)
