from typing import Any

import httpx

BASE_URL = "https://api.frankfurter.dev/v1"
TIMEOUT: float = 10

class APIError(Exception):
    pass

def get_rates(base: str, targets: list[str] | None):
    params: dict[str, Any] = {"base": base.upper()}

    if targets:
        params["symbols"] = ",".join(target.upper() for target in targets)

    try:
        response = httpx.get(f"{BASE_URL}/latest", params=params, timeout=TIMEOUT)

        response.raise_for_status()

        return response.json()

    except httpx.HTTPStatusError:
        raise APIError()

    except httpx.RequestError:
        raise APIError()
