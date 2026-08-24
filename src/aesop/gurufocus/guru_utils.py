import requests


def guru_api_get(url: str, ticker: str, timeout: int = 10) -> dict:
    """Shared GET + error handling for all Gurufocus API calls."""
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        print(f"Request timed out for ticker {ticker}")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error for ticker {ticker}: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed for ticker {ticker}: {e}")
    except ValueError:
        print(f"Invalid JSON response for ticker {ticker}")
    return {}

