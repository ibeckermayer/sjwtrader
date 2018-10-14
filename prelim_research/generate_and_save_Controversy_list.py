"""Script to generate a list of Controversy objects for each controversy in the .csv.
Due to API call limits for alpha_vantage, I'm forced to limit my calls to once per minute
(see __init__ in model/Controversy). For that reason, it makes most sense to just do this
once and then serialize (meaning save to hard disk) the list of controversy objects, and
then write a different script that loads those objects and creates graphs from them.
"""

import pandas as pd
import pickle
from datetime import datetime
from model.Controversy import Controversy

DATA = "data/controversy_data.csv"
ENCODING = "ISO-8859-1"
PIK = "data/controversies.pickle"

def date_to_datetime(date):
    """format all the date strings into MM/DD/YYYY and then return datetime

    @param date (str): string in M/D/Y format where M and D can be 1 or 2 digits

    @return (datetime): string converted to datetime
    """
    date_as_list = date.split('/')  # break into a list
    mmddyyyy = ""

    for i in range(len(date_as_list)):
        if len(date_as_list[i]) < 2:
            date_as_list[i] = '0' + date_as_list[i]  # add a preceding 0 if necessary
        if i == len(date_as_list) - 1:
            date_as_list[i] = '20' + date_as_list[i]  # everything in this century
        mmddyyyy += date_as_list[i]                  # add to string
        if i < len(date_as_list) - 1:
            mmddyyyy += '/'     # add '/' if appropriate

    return datetime.strptime(mmddyyyy, "%m/%d/%Y")

if __name__ == "__main__":
    df = pd.read_csv(DATA, encoding=ENCODING)

    controversies = []              # list to hold all the controversies
    for index, row in df.iterrows():  # convert each row into Controversy and add to list
        controversies.append(Controversy(row["Company"],
                                         row["Stock"].split('-'),
                                         date_to_datetime(row["Date_Of_Controversy_m/d/y"]),
                                         row["Summary"],
                                         row["Source"],
                                         row["Notes"]))

    with open(PIK, "wb") as f:
        pickle.dump(controversies, f)
