from ib_insync import *
import pandas as pd
import os
from datetime import datetime
pd.set_option('display.max_columns', None)


def tempSampleData(ib, contract):
    """
    Args:
        ib: InteractiveBrokers - The instance of the Interactive Brokers API connection.
        contract: Contract - The contract for which to retrieve historical data.

    Returns:
        pandas.DataFrame - The historical data for the specified contract.

    """
    optionsData = ib.reqHistoricalData(contract, endDateTime='',
                                       durationStr='1 D',barSizeSetting='1 min',
                                       whatToShow='MIDPOINT', useRTH=True)
    return optionsData


def saveCsv(df, path, fileName):
    """
    Saves the given DataFrame to a CSV file in the specified path.

    Args:
        df (pandas.DataFrame): The DataFrame to be saved.
        path (str): The path where the file should be saved. If the folder does not exist, it will be created.
        fileName (str): The name of the file to be saved.

    """
    # Check if the folder exists, if not, create it
    if not os.path.exists(path):
        os.makedirs(path)
    # Save the DataFrame to CSV in the specified path
    df.to_csv(os.path.join(path, fileName))


def main(path, expirations, strikes):
    """
    Connects to the Interactive Brokers (IBKR) API Client, retrieves AMD options data
    for given expiration dates and strikes, and saves the data as CSV files.
    *.

    Args:
        path (str): The base path for saving the CSV files.
        expirations (list[str]): A list of expiration dates for the options contracts.
        strikes (list[float]): A list of strike prices for the options contracts.

    """
    # Connect to IBKR API Client
    ib = IB()
    ib.connect('127.0.0.1', 7497, 1, readonly=True)

    # Folder to save CSV files, named after the current date
    currentDate = datetime.now().strftime("%Y-%m-%d")
    basePath = os.path.join(path, currentDate)

    for expiration in expirations:
        for strike in strikes:
            for right in ['C', 'P']:  # C for Call, P for Put
                contract = Option('AMD', expiration, strike, right, 'SMART')
                optionsData = tempSampleData(ib, contract)
                df = pd.DataFrame(optionsData)
                df = df.drop(columns=['volume', 'average', 'barCount'])

                # Define folder path and file name
                formattedExpiration = expiration[:4] + "-" + expiration[4:6] + "-" + expiration[6:]
                folderPath = os.path.join(basePath, formattedExpiration)
                fileName = f"AMD {formattedExpiration} {strike} {right}.csv"

                # Save the DataFrame as a CSV
                saveCsv(df, folderPath, fileName)
                print(f"Saved: {fileName} in {folderPath}")

    # Closes the IBKR API Client connection
    ib.disconnect()


if __name__ == "__main__":
    path = 'AMD Historical Options Data'
    expirations = ['20240209', '20240216', '20240223', '20240301', '20240308',
                   '20240315', '20240419', '20240517', '20240621', '20240719',
                   '20240920', '20241220', '20250117', '20250620', '20251219',
                   '20260116']
    strikes = [140.0, 145.0, 150.0, 155.0, 160.0, 165.0, 170.0, 175.0, 180.0,
               185.0, 190.0, 195.0, 200.0]

    if not os.path.exists(path):
        os.makedirs(path)

    main(path, expirations, strikes)