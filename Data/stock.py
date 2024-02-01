from ib_insync import *
import pandas as pd
import os


def main(path, year):
    # Connect to IBKR API Client
    ib = IB()
    ib.connect('127.0.0.1', 7497, 1, readonly=True)

    # Initialize object for AMD stock
    amdContract = Stock('AMD', 'SMART', 'USD')  # conID=4391
    print(amdContract)

    # Request
    amdHistStockData = ib.reqHistoricalData(amdContract, '', '10 Y',
                                            '1 day', 'MIDPOINT', True)
    df = util.df(amdHistStockData)
    df = df.drop(columns=['volume', 'average', 'barCount'])
    df['date'] = pd.to_datetime(df['date'])
    df = df[df['date'].dt.year == year]
    print(df.head())
    savePath = os.path.join(path, 'AMD_' + str(year) + '.csv')
    df.to_csv(savePath, index=False)
    ib.disconnect()


if __name__ == "__main__":
    stockDataYears = [2019, 2020, 2021, 2022, 2023]
    path = 'AMD Historical Stock Data'

    if not os.path.exists(path):
        os.makedirs(path)

    if type(stockDataYears) is list:
        for year in stockDataYears:
            main(path, year)
    else:
        main(path, year)