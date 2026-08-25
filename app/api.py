from typing import Any

import httpx

# VARIABLES
BASE_URL = "https://api.frankfurter.dev/v1"
TIMEOUT: float = 10


# ERROR CATCH
class APIError(Exception):
    pass

# GET RATES FROM API
def get_rates(base: str, targets: list[str] | None):
    params: dict[str, Any] = {"base": base.upper()}

    if targets:
        params["symbols"] = ",".join(target.upper() for target in targets)

    try:
        response = httpx.get(f"{BASE_URL}/latest", params=params, timeout=TIMEOUT)

        response.raise_for_status()

        return response.json()

    except (httpx.HTTPStatusError, httpx.RequestError):
        raise APIError()

# GET HISTORY FROM API
def get_history(start_date: str, 
                end_date: str, 
                base: str, 
                targets: list[str]| None):

    params: dict[str, Any] = {"base": base.upper()}

    if targets:
        params["symbols"] = ",".join(target.upper() for target in targets)

    try:
        response = httpx.get(f"{BASE_URL}/{start_date}..{end_date}",
                             params=params,
                             timeout=TIMEOUT)

        response.raise_for_status()

        return response.json()

    except (httpx.HTTPStatusError, httpx.RequestError):
        raise APIError()


# GET ALL CURRENCIES AVAILABLE FROM API
def get_currencies():
    response = httpx.get(f"{BASE_URL}/currencies")

    response.raise_for_status()

    return response.json()