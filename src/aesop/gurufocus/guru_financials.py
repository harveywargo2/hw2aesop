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


    def __post_init__(self):
        self.ddr_dict = self._guru_api()
        self.ddr_fin_parameters_dict = self._fin_parameters()
        self.ddr_fin_annual_dict = self._fin_annuals()
        self.ddr_fin_quarter_dict = self._fin_quarterly()



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

