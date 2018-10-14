import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from alpha_vantage.timeseries import TimeSeries
from datetime import datetime
from time import sleep

with open('ALPHA_VANTAGE_API_KEY', 'r') as f:
    API_KEY = f.read()[:-1]      # get API key, ignore the \n at the end

ts = TimeSeries(key=API_KEY, output_format='pandas')    # create instance with API key

# make indexing columns of alpha_vantage response easier
OPEN   = "1. open"
HIGH   = "2. high"
LOW    = "3. low"
CLOSE  = "4. close"
ADJ_CLOSE = "5. adjusted close"

class Controversy:
    """Class for storing controversy data

    @param[in] company (str):       Colloquial name for the company.
    @param[in] stocks  (list[str]): List of relevant stock abbreviations for company.
    @param[in] date    (datetime):  Date of controversy.
    @param[in] summary (str):       One line summary of the controversy.
    @param[in] source: (str):       URL of article confirming controversy and date of the controversy.
    @param[in] notes:  (str):       Any relevant notes about the company/controversy not contained in the other parameters.

    @param[out] stock_data_dfs:    (list[pd.DataFrame]): List of DataFrames containing the actual stock data corresponding to each
                                              stock abbreviation listed in stocks.
    """

    def __init__(self, company, stocks, date, summary, source, notes=None):
        """init for Controversy
        """
        self.company = company
        self.stocks = stocks
        self.date = date
        self.summary = summary
        self.source = source
        self.notes = notes if notes is not None else ""

        # get all the data on hand for each stock, as pd dataframes
        self.stock_data_dfs = []
        print("Fetching stock data for the company {}".format(self.company))
        for stock in self.stocks:
            print("Fetching data for stock {}".format(stock))
            self.stock_data_dfs.append(ts.get_daily_adjusted(symbol=stock, outputsize='full')[0])
            sleep(60)           # sleep a minute to avoid over-calling the API
        print()
