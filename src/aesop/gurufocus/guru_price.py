import aesop as ap
import pandas as pd
from dataclasses import dataclass, field


@dataclass(init=True, repr=True, eq=True)
class GuruPriceHistory:
    """Class for Gurufocus Price History Output"""
    token: str
    ticker: str
    ddr_list: list = field(init=False, repr=False, default=None)
    ddr_df: object = field(init=False, repr=False, default=None)


    def __post_init__(self):
        self.ddr_list = self._guru_api()
        self.ddr_df = self._raw_df()


    def _guru_api(self):

        url = f'https://api.gurufocus.com/public/user/{self.token}/stock/{self.ticker}/price'

        api_call = ap.guru_api_get(url, ticker=self.ticker, timeout=10)
        return api_call


    def _raw_df(self):
        lst = self.ddr_list
        df = pd.DataFrame(lst)
        return df