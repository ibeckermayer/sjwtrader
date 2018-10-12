import pandas as pd
from datetime import datetime
from model.Controversy import Controversy

# The actual format of the Date_Of_Controversy... column is MM/DD/YYYY, despite the name of the column.
# My fucking student Excel liscense expired the day that I'm writing this so I can't change the label in the spreadsheet
# Such is the life of a starving artist (pronounced 'arteeeest')
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

df = pd.read_csv("data/controversy_data.csv", encoding = "ISO-8859-1")

controversies = []              # list to hold all the controversies
for index, row in df.iterrows():  # convert each row into Controversy and add to list
    controversies.append(Controversy(row["Company"],
                                     row["Stock"],
                                     date_to_datetime(row["Date_Of_Controversy (DD/MM/YYYY)"]),
                                     row["Summary"],
                                     row["Source"],
                                     row["Notes"]))
