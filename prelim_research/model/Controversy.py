from datetime import datetime

class Controversy:
    """Class for storing controversy data

    @param company (str):       Colloquial name for the company.
    @param stock   (list[str]): List of relevant stock abbreviations for company.
    @param date    (datetime):  Date of controversy.
    @param summary (str):       One line summary of the controversy.
    @param source: (str):       URL of article confirming controversy and date of the controversy.
    @param notes:  (str):       Any relevant notes about the company/controversy not contained in the other parameters.
    """
    with open('ALPHA_VANTAGE_API_KEY', 'r') as f:
        API_KEY = f.read()[:-1]      # get API key, ignore the \n at the end

    def __init__(self, company, stock, date, summary, source, notes=None):
        """init for Controversy
        """
        self.company = company
        self.stock = stock
        self.date = date
        self.summary = summary
        self.source = source
        self.notes = notes if notes is not None else ""
