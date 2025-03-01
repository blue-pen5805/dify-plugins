from typing import Any

from dify_plugin import ToolProvider
from dify_plugin.errors.tool import ToolProviderCredentialValidationError

import httpx

class ChakoshiProvider(ToolProvider):
    def _validate_credentials(self, credentials: dict[str, Any]) -> None:
        try:
            url = "https://api.beta.chakoshi.ntt.com/v1/models/"
            headers = {
                "Authorization": f"Bearer {credentials['api_key']}",
                "Content-Type": "application/json",
                "Accept": "application/json",
            }
            response = httpx.get(url, headers=headers)

            if response.is_success:
                pass
            else:
                raise ToolProviderCredentialValidationError(response.text)
        except Exception as e:
            raise ToolProviderCredentialValidationError(str(e))
