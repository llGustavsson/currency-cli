from unittest.mock import MagicMock, patch

import httpx
import pytest

from app.api import APIError, get_history, get_rates


# TESTS FOR RATES
@patch("httpx.get")
def test_get_rates(mock_get):
    mock_response = MagicMock()
    mock_response.raise_for_status.return_value = None
    mock_response.json.return_value = {"amount": 1.0,
                                       "base": "USD",
                                       "date": "2026-08-02",
                                       "rates": {"EUR": 0.88, "BRL": 5.20}}

    mock_get.return_value = mock_response

    result = get_rates(base="USD", targets=["EUR","BRL"])

    assert result["base"] == "USD"
    assert "EUR" in result["rates"]
    assert "BRL" in result["rates"]

    mock_get.assert_called_once()

@patch("httpx.get")
def test_get_rates_fail(mock_get):
    mock_response = MagicMock()
    mock_response.status_code = 404
    mock_response.raise_for_status.side_effect = httpx.HTTPStatusError(message="Not Found",
                                                                       request=MagicMock(),
                                                                       response=mock_response)

    mock_get.return_value = mock_response

    with pytest.raises(APIError):
        get_rates(base="INVALID", targets=None)


# TESTS FOR HISTORY 
@patch("httpx.get")
def test_get_history(mock_get):
    mock_response = MagicMock()
    mock_response.raise_for_status.return_value = None
    mock_response.json.return_value = {"amount": 1.0, 
                                       "base": "EUR",
                                       "start_date": "2026-08-17",
                                       "end_date": "2026-08-24",
                                       "rates": {"2026-08-17": {"BRL": 6.05}}}

    mock_get.return_value = mock_response

    result = get_history(start_date="2026-08-17",
                         end_date="2026-08-24",
                         base="EUR",
                         targets="BRL")

    assert result["base"] == "EUR"
    assert "2026-08-17" in result["rates"]

@patch("httpx.get")
def test_get_history_fail(mock_get):
    mock_response = MagicMock()
    mock_response.status_code = 404
    mock_response.raise_for_status.side_effect = httpx.HTTPStatusError(message="Not Found",
                                                                        request=MagicMock(),
                                                                        response=mock_response)

    mock_get.return_value = mock_response

    with pytest.raises(APIError):
        get_history(start_date="invalid", 
                    end_date="invalid", 
                    base="EUR", 
                    targets="BRL")
