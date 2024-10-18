import hashlib
import hmac
import json
import time
from datetime import datetime
from typing import Dict, Optional

import requests  # type: ignore
from gmo_repository_model import AssetsResponse

# TODO: 必要に応じて抽象クラス追加


class GmoRepository:
    _base_url_private = "https://forex-api.coin.z.com/private"
    _base_url_public = "https://forex-api.coin.z.com/private"

    def __init__(self, api_key: str, secret_key: str):
        self._api_key = api_key
        self._secret_key = secret_key

    def get_assets(self) -> Optional[AssetsResponse]:
        headers = self._generate_header("GET", "/v1/account/assets")
        try:
            response = requests.get(
                f"{self._base_url_private}/v1/account/assets", headers=headers
            )
            response.raise_for_status()

            # TODO: デバッグログ出力に変更
            data = response.json()
            print(json.dumps(data, indent=2))

            return AssetsResponse(**response.json())
        except requests.exceptions.HTTPError as err:
            data = response.json()
            print(json.dumps(data, indent=2))
            print(f"HTTP error on calling GET assets: {err}")
        except Exception as err:
            data = response.json()
            print(json.dumps(data, indent=2))
            print(f"Exception occurred on calling GET assets: {err}")
        return None

    def _generate_header(self, method: str, path: str) -> Dict[str, str]:
        timestamp = f"{int(time.mktime(datetime.now().timetuple()))}000"

        text = timestamp + method + path
        sign = hmac.new(
            bytes(self._secret_key.encode("ascii")),
            bytes(text.encode("ascii")),
            hashlib.sha256,
        ).hexdigest()

        headers = {
            "API-KEY": self._api_key,
            "API-TIMESTAMP": timestamp,
            "API-SIGN": sign,
        }
        return headers
