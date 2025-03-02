from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

import httpx
import json

class ChakoshiJudgeTextTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        text: str = tool_parameters.get("text")
        model: str = tool_parameters.get("model") or "chakoshi-moderation-241223"
        category_set_id: str | None = tool_parameters.get("category_set_id")

        url = "https://api.beta.chakoshi.ntt.com/v1/judge/text"
        headers = {
            "Authorization": f"Bearer {self.runtime.credentials['api_key']}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        data = {
            "input": text,
            "model": model,
            "category_set_id": category_set_id,
        }
        response = httpx.post(url, headers=headers, json=data)

        if response.is_success:
            json_response = response.json()
            result = json_response["results"]
            unsafe_flag = result["unsafe_flag"]
            unsafe_score = result["unsafe_score"]
            unsafe_category = result["unsafe_category"]

            return [
                self.create_json_message(json_response),
                self.create_text_message("true" if unsafe_flag else "false"),
                self.create_variable_message("flagged", unsafe_flag),
                self.create_variable_message("unsafe_score", unsafe_score),
                self.create_variable_message("flagged_categories", [unsafe_category] if unsafe_category else []),
            ]
        else:
            raise ValueError(response.text)
