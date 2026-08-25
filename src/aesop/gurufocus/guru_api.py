import requests
import aesop as ap
from dataclasses import dataclass, field


@dataclass(init=True, repr=True, eq=True)
class GuruStockSummaryData:
    """Class for Gurufocus Stock Summary Data Output"""
    token: str
    ticker: str
    ddr_dict: dict = field(init=False, repr=False, default=None)
    ddr_general_dict: dict = field(init=False, repr=False, default=None)
    ddr_chart_dict: dict = field(init=False, repr=False, default=None)
    ddr_ratio_dict: dict = field(init=False, repr=False, default=None)
    ddr_guru_dict: dict = field(init=False, repr=False, default=None)
    ddr_insider_dict: dict = field(init=False, repr=False, default=None)
    ddr_company_dict: dict = field(init=False, repr=False, default=None)
    ddr_estimate_dict: dict = field(init=False, repr=False, default=None)


    def __post_init__(self):
        self.ddr_dict = self._guru_api()
        self.ddr_general_dict = self._general()
        self.ddr_chart_dict = self._chart()
        self.ddr_ratio_dict = self._ratio()
        self.ddr_guru_dict = self._guru()
        self.ddr_insider_dict = self._insider()
        self.ddr_company_dict = self._company()
        self.ddr_estimate_dict = self._estimate()


    def _guru_api(self):

        url = f'https://api.gurufocus.com/public/user/{self.token}/stock/{self.ticker}/summary'

        api_call = ap.guru_api_get(url, ticker=self.ticker, timeout=10)
        return api_call


    def _general(self):
        data = self.ddr_dict['summary']['general']
        return data


    def _chart(self):
        data = self.ddr_dict['summary']['chart']
        return data


    def _ratio(self):
        data = self.ddr_dict['summary']['ratio']
        return data


    def _guru(self):
        data = self.ddr_dict['summary']['guru']
        return data


    def _insider(self):
        data = self.ddr_dict['summary']['insider']
        return data


    def _company(self):
        data = self.ddr_dict['summary']['company_data']
        return data


    def _estimate(self):
        data = self.ddr_dict['summary']['estimate']
        return data


@dataclass(init=True, repr=True, eq=True)
class GuruOperatingData:
    """Class for Gurufocus Operating Data Output"""
    token: str
    ticker: str
    ddr_dict: dict = field(init=False, repr=False, default=None)

    def __post_init__(self):
        self.ddr_dict = self._guru_api()


    def _guru_api(self):

        url = f'https://api.gurufocus.com/public/user/{self.token}/stock/{self.ticker}/operating_data'

        api_call = ap.guru_api_get(url, ticker=self.ticker, timeout=10)
        return api_call


@dataclass(init=True, repr=True, eq=True)
class GuruStockFilingsData:
    """Class for Gurufocus Stock Filings Data Output"""
    token: str
    ticker: str
    ddr_dict: dict = field(init=False, repr=False, default=None)

    def __post_init__(self):
        self.ddr_dict = self._guru_api()


    def _guru_api(self):

        url = f'https://api.gurufocus.com/public/user/{self.token}/stock/{self.ticker}/filings'

        api_call = ap.guru_api_get(url, ticker=self.ticker, timeout=10)
        return api_call


@dataclass(init=True, repr=True, eq=True)
class GuruStockSegmentsData:
    """Class for Gurufocus Stock Segments Data Output"""
    token: str
    ticker: str
    ddr_dict: dict = field(init=False, repr=False, default=None)

    def __post_init__(self):
        self.ddr_dict = self._guru_api()


    def _guru_api(self):

        url = f'https://api.gurufocus.com/public/user/{self.token}/stock/{self.ticker}/segments_data'

        api_call = ap.guru_api_get(url, ticker=self.ticker, timeout=10)
        return api_call


@dataclass(init=True, repr=True, eq=True)
class GuruInsiderTradesData:
    """Class for Gurufocus Insider Trades Output"""
    token: str
    ticker: str
    ddr_dict: dict = field(init=False, repr=False, default=None)

    def __post_init__(self):
        self.ddr_dict = self._guru_api()


    def _guru_api(self):

        url = f'https://api.gurufocus.com/public/user/{self.token}/stock/{self.ticker}/insider'

        api_call = ap.guru_api_get(url, ticker=self.ticker, timeout=10)
        return api_call


@dataclass(init=True, repr=True, eq=True)
class GuruExecutivesData:
    """Class for Gurufocus Executives Output"""
    token: str
    ticker: str
    ddr_list: dict = field(init=False, repr=False, default=None)

    def __post_init__(self):
        self.ddr_list = self._guru_api()


    def _guru_api(self):

        url = f'https://api.gurufocus.com/public/user/{self.token}/stock/{self.ticker}/executives'

        api_call = ap.guru_api_get(url, ticker=self.ticker, timeout=10)
        return api_call