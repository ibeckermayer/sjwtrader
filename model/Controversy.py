import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from matplotlib import rcParams
from alpha_vantage.timeseries import TimeSeries
from datetime import datetime, timedelta
from time import sleep

# Make the dates stay in the scope of the figure
rcParams.update({'figure.autolayout': True})

with open('ALPHA_VANTAGE_API_KEY', 'r') as f:
    API_KEY = f.read()[:-1]      # get API key, ignore the \n at the end

ts = TimeSeries(key=API_KEY, output_format='pandas')    # create instance with API key

# make indexing columns of alpha_vantage response easier
ADJ_CLOSE = "5. adjusted close"

class Controversy:
    """Class for storing controversy data

    @param[in] company (str):       Colloquial name for the company.
    @param[in] stocks  (list[str]): List of relevant stock abbreviations for company.
    @param[in] date    (datetime):  Date of controversy.
    @param[in] summary (str):       One line summary of the controversy.
    @param[in] source: (str):       URL of article confirming controversy and date of the controversy.
    @param[in] notes:  (str):       Any relevant notes about the company/controversy not contained in the other parameters.

    @param[out] dfs:    (list[pd.DataFrame]): List of DataFrames containing the actual stock data corresponding to each
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
        self.dfs = []
        print("Fetching stock data for the company {}".format(self.company))
        for stock in self.stocks:
            print("Fetching data for stock {}".format(stock))
            self.dfs.append(ts.get_daily_adjusted(symbol=stock, outputsize='full')[0])
            sleep(60)           # sleep a minute to avoid over-calling the API
        print()

    def get_N_day_plot(self, N):
        """Generates a plot for relevant stock data three days either side of the controversy

        @return (plt.figure) figure containing the plots
        """
        # setup figure formatting
        f = plt.figure()
        ax = f.add_subplot(1,1,1)
        ax.xaxis_date()
        plt.xticks(rotation=70)
        fmt = '${x:.2f}'
        tick = mtick.StrMethodFormatter(fmt)
        ax.yaxis.set_major_formatter(tick)
        ax.set_xlabel("Date")
        ax.set_ylabel("Price")
        for i in range(len(self.dfs)):
            df = self.dfs[i]
            df = df[df[ADJ_CLOSE] != 0]  # drop any points where adj_closed == 0, appears to be noise
            stock = self.stocks[i]
            date = self.date
            df = df.reset_index()    # take date index and make it a column, now have normal integer indexing
            # loop for if the self date is on a weekend
            # if so, keep going back one day
            con_index = None
            delt_days = 0
            while con_index is None and delt_days < len(df):
                try:
                    con_index = df[df["date"] ==
                                   (date - timedelta(days=delt_days)).strftime("%Y-%m-%d")].index[0]  # find the index corresponding to controversy date
                except:
                    delt_days+=1
                    pass
            if delt_days == len(df):
                print("No data for these dates")
            three_day_df = df[(con_index-N)-delt_days:(con_index+N+1)+delt_days]  # get the data within N days
            dates = matplotlib.dates.date2num([datetime.strptime(d, "%Y-%m-%d") for d in three_day_df["date"].values])
            adjusted_close = three_day_df[ADJ_CLOSE].values
            ax.plot(matplotlib.dates.date2num(date),
                    max(adjusted_close), 's',
                    marker='v', color='r',
                    label = "Date of Controversy")
            ax.plot(matplotlib.dates.date2num(date),
                    min(adjusted_close), 's',
                    marker='^', color='r')
            ax.plot([matplotlib.dates.date2num(date)]*2,
                    [max(adjusted_close), min(adjusted_close)],
                    marker=',', color='r')
            ax.plot(dates, adjusted_close, linestyle='-', marker=',', label=stock)
            plt.title("Stock price {} days either side of controversy".format(N))
            plt.legend(bbox_to_anchor=(1.04,1), loc="upper left")

        return f

        for i in range(len(controversy.dfs)):
            df = controversy.dfs[i]
            df = df[df[ADJ_CLOSE] != 0]  # drop any points where adj_closed == 0, appears to be noise
            stock = controversy.stocks[i]
            date = controversy.date
            df = df.reset_index()    # take date index and make it a column, now have normal integer indexing
            # loop for if the controversy date is on a weekend
            # if so, keep going back one day
            con_index = None
            delt_days = 0
            while con_index is None and delt_days < len(df):
                try:
                    con_index = df[df["date"] ==
                                   (date - timedelta(days=delt_days)).strftime("%Y-%m-%d")].index[0]  # find the index corresponding to controversy date
                except:
                    delt_days+=1
                    pass
            if delt_days == len(df):
                print("No data for these dates")
