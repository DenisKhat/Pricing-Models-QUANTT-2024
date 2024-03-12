from ib_insync import *
import pandas as pd
import os


def main(path, year):
    """
    Args:
        path: The path to the folder where the CSV file will be saved.
        year: The year to filter the historical stock data by.

    Description:
        Retrieves historical stock data for AMD stock from the IBKR API, filters it based
        on the specified year, and saves it to a CSV file in the given folder path.

    Params:
        path (str): The path to the folder where the CSV file will be saved.
        year (int): The year to filter the historical stock data by.
    """
    # Connect to IBKR API Client
    ib = IB()
    ib.connect('127.0.0.1', 7497, 1, readonly=True)

    # Initialize object for AMD stock
    amdContract = Stock('AMD', 'SMART', 'USD')  # conID=4391

    # Request historical stock data
    amdHistStockData = ib.reqHistoricalData(amdContract, '', '6 Y',
                                            '1 min', 'MIDPOINT', True)
    df = util.df(amdHistStockData)
    
    # Drops unneeded columns
    df = df.drop(columns=['volume', 'average', 'barCount'])
    df['date'] = pd.to_datetime(df['date'])

    # Filters by the search year
    df = df[df['date'].dt.year == year]

    # Saves to a csv file within the folder
    savePath = os.path.join(path, 'AMD_' + str(year) + '.csv')
    df.to_csv(savePath, index=False)
    print(f"Data saved to {savePath}")

    # Closes the IBKR API Client connection
    ib.disconnect()


if __name__ == "__main__":
    dataTimeframe = [2019, 2020, 2021, 2022, 2023]
    path = 'AMD Historical Stock Data'

    if not os.path.exists(path):
        os.makedirs(path)

    # This allows the var stockDataYears to be a single year if needed
    if type(stockDataYears) is list:
        for year in stockDataYears:
            main(path, year)
    else:
        main(path, stockDataYears)