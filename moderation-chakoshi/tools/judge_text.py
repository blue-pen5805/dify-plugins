from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

import httpx
import json

class ChakoshiJudgeTextTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        text = tool_parameters.get("text")
        model = tool_parameters.get("model") or "chakoshi-moderation-241223"
        category_set_id = tool_parameters.get("category_set_id")

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

            yield self.create_text_message(json.dumps(json_response))
            yield self.create_json_message(json_response)
            yield self.create_variable_message("unsafe_flag", json_response["results"]["unsafe_flag"])
            yield self.create_variable_message("label_str", json_response["results"]["label_str"])
            yield self.create_variable_message("unsafe_score", json_response["results"]["unsafe_score"])
            yield self.create_variable_message("unsafe_category", json_response["results"]["unsafe_category"])
        else:
            raise ValueError(response.text)
