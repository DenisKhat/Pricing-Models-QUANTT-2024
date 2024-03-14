from ib_insync import *
import pandas as pd
import os
from datetime import datetime
# IMPLEMENT 1m bar gathering for AMD 2023
# Will need to gather the data per day individually for this to work
# Use business day library from test file to ensure requests are for valid business days


def main(path):
    # Connect to IBKR API Client
    ib = IB()
    ib.connect('127.0.0.1', 7497, 1, readonly=True)

    # Initialize object for AMD stock
    amdContract = Stock('AMD', 'SMART', 'USD')  # conID=4391

    dt = ''
    barsList = []
    while True:
        bars = ib.reqHistoricalData(
            amdContract,
            endDateTime=dt,
            durationStr='1 D',
            barSizeSetting='1 min',
            whatToShow='MIDPOINT',
            useRTH=True,
            formatDate=1)
        if not bars:
            break

        barsList.append(bars)
        dt = bars[0].date
        print(dt)
        if dt:  # Check if dt is not an empty string
            current_date = dt.replace(tzinfo=None)
            end_date = datetime(year=2023, month=1, day=1)
            if current_date <= end_date:
                break

    # save to CSV file
    allBars = [b for bars in reversed(barsList) for b in bars]
    df = util.df(allBars)
    df = df.drop(columns=['volume', 'average', 'barCount'])
    savePath = os.path.join(path, 'AMD_2023_To_Present_1m.csv')
    df.to_csv(savePath, index=False)


if __name__ == "__main__":
    path = 'AMD Historical Stock Data/'

    if not os.path.exists(path):
        os.makedirs(path)

    main(path)
