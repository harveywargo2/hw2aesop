import requests
import pandas as pd
from dataclasses import dataclass, field


@dataclass(init=True, repr=True, eq=True)
class GuruFinancialHistory:
    """Class for Gurufocus Financial History Output"""
    token: str
    ticker: str
    ddr_dict: dict = field(init=False, repr=False, default=None)
    ddr_fin_parameters_dict: dict = field(init=False, repr=False, default=None)
    ddr_fin_annuals_dict: dict = field(init=False, repr=False, default=None)
    ddr_fin_quarterly_dict: dict = field(init=False, repr=False, default=None)
    ddr_fin_annuals_df: object = field(init=False, repr=False, default=None)
    ddr_fin_quarterly_df: object = field(init=False, repr=False, default=None)


    def __post_init__(self):
        self.ddr_dict = self._guru_api()
        self.ddr_fin_parameters_dict = self._fin_parameters()
        self.ddr_fin_annuals_dict = self._fin_annuals()
        self.ddr_fin_quarterly_dict = self._fin_quarterly()
        self.ddr_fin_annuals_df = self._fin_annuals_df()
        self.ddr_fin_quarterly_df = self._fin_quarterly_df()


    def _guru_api(self):

        url = f'https://api.gurufocus.com/public/user/{self.token}/stock/{self.ticker}/financials'

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


    def _fin_parameters(self):
        data = self.ddr_dict['financials']['financial_template_parameters']
        return data


    def _fin_annuals(self):
        data = self.ddr_dict['financials']['annuals']
        return data


    def _fin_quarterly(self):
        data = self.ddr_dict['financials']['quarterly']

        return data


    def _fin_annuals_df(self):
        data = self.ddr_fin_annuals_dict
        df_0 = pd.DataFrame()
        df_1 = pd.json_normalize(data)

        for item, value in df_1.items():
            series_explode = pd.Series(value, name=item).explode(ignore_index=True)
            df_0 = pd.concat([df_0, series_explode.to_frame()], axis=1)

        return df_0


    def _fin_quarterly_df(self):
        data = self.ddr_fin_quarterly_dict
        df_0 = pd.DataFrame()
        df_1 = pd.json_normalize(data)

        for item, value in df_1.items():
            series_explode = pd.Series(value, name=item).explode(ignore_index=True)
            df_0 = pd.concat([df_0, series_explode.to_frame()], axis=1)

        return df_0


@dataclass(init=True, repr=True, eq=True)
class GuruOperatingData:
    """Class for Gurufocus Operating Data Output"""
    token: str
    ticker: str
    ddr_dict: dict = field(init=False, repr=False, default=None)

    def _guru_api(self):

        url = f'https://api.gurufocus.com/public/user/{self.token}/stock/{self.ticker}/financials'

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

