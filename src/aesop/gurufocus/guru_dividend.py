import requests
import pandas as pd
from dataclasses import dataclass, field


@dataclass(init=True, repr=True, eq=True)
class GuruDividendHistory:
    """Class for Gurufocus Dividend History Output"""
    token: str
    ticker: str
    ddr_list: dict = field(init=False, repr=False, default=None)
    ddr_df: object = field(init=False, repr=False, default=None)


    def __post_init__(self):
        self.ddr_list = self._guru_api()
        self.ddr_df = self._raw_df()


    def _guru_api(self):
        url = f'https://api.gurufocus.com/public/user/{self.token}/stock/{self.ticker}/dividend'

        try:

            response = requests.get(url, timeout=10)
            response.raise_for_status()

            return response.json()

        except requests.exceptions.Timeout:
            print(f"Request timed out for ticker {self.ticker}")

        except requests.exceptions.HTTPError as e:
            print(f"HTTP error for ticker {self.ticker}: {e}")

        except requests.exceptions.RequestException as e:
            print(f"Request failed for ticker {self.ticker}: {e}")

        except ValueError:
            print(f"Invalid JSON response for ticker {self.ticker}")

        return {}


    def _raw_df(self):
        lst = self.ddr_list
        df = pd.DataFrame(lst)

        return df

