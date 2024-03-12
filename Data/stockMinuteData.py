from ib_insync import *
import pandas as pd
import os
# IMPLEMENT 1m bar gathering for AMD 2023
# Will need to gather the data per day individually for this to work
# Use business day library from test file to ensure requests are for valid business days

def main(path, year):
    # Connect to IBKR API Client
    ib = IB()
    ib.connect('127.0.0.1', 7497, 1, readonly=True)

    # Initialize object for AMD stock
    amdContract = Stock('AMD', 'SMART', 'USD')  # conID=4391

if __name__ == "__main__":
    dataTimeframe = 2023
    path = 'AMD Historical Stock Data/' + str(dataTimeframe)

    if not os.path.exists(path):
        os.makedirs(path)

    main(path, dataTimeframe)