from ib_insync import *
import pandas as pd
import os
import sys
import traceback
from datetime import datetime, timedelta
from helpers import getTradingDays, checkExpiries, saveCsv

pd.set_option('display.max_columns', None)


# Use business day library from test file to ensure automated requests are for valid business days.
# Could even have it check if there is already a folder for the previous day, if not
# it'd keep working backwards until it grabs the required data for all the missing days.
# This could be a good way to run it once a week on (for instance) Thursday night or Friday early morning 🤔


def getData(ib, contract, date):

    if date < datetime.now():
        endDateTime = date.strftime("%Y%m%d") + ' 16:15:00'
        optionsData = ib.reqHistoricalData(contract, endDateTime, durationStr='1 D',
                                           barSizeSetting='1 min', whatToShow='MIDPOINT', useRTH=True)
    else:
        optionsData = ib.reqHistoricalData(contract, endDateTime='', durationStr='1 D',
                                           barSizeSetting='1 min', whatToShow='MIDPOINT', useRTH=True)
    return optionsData


def main(ib, path, expirations, strikes, date):
    for expiration in expirations:
        for strike in strikes:
            for right in ['C', 'P']:  # C for Call, P for Put
                try:
                    contract = Option('AMD', expiration, strike, right, 'SMART')
                    optionsData = getData(ib, contract, date)
                    df = pd.DataFrame(optionsData)
                    df = df.drop(columns=['volume', 'average', 'barCount'])

                    # Define folder path and file name
                    formattedExpiration = expiration[:4] + "-" + expiration[4:6] + "-" + expiration[6:]
                    folderPath = os.path.join(path, formattedExpiration)
                    fileName = f"AMD {formattedExpiration} {strike} {right}.csv"

                    # Save the DataFrame as a CSV
                    saveCsv(df, folderPath, fileName)
                    print(f"Saved: {fileName} in {folderPath}")
                # Some contracts, especially close to expiry and far OTM have no data to pull (i.e. all values are 0)
                except Exception as error:
                    print("An error occurred:", error)


# Automate expiry dates by reading and writing to a file
# Could get official expiry dates but one way to meta-game it is by adding the next friday after Mar 22 onwards
# ^ needs to use the business day util thing
# Maybe make a logging system for output, so I can see what happens if anything goes wrong?

# Check what dates have had data pulled (based on if the folder exists) BEFORE deleting any expiry dates
# based on the current date
if __name__ == "__main__":
    # Connect to IBKR API Client
    ib = IB()
    ib.connect('127.0.0.1', 7497, 1, readonly=True)
    # strikes = [140.0, 145.0, 150.0, 155.0, 160.0, 165.0, 170.0, 175.0, 180.0,
    #            185.0, 190.0, 195.0, 200.0]
    # df = pd.DataFrame(strikes, columns=['Strike Price'])
    # print(df)
    # saveCsv(df, None, 'strikes.csv')
    #
    # expirations = ['2024-02-09', '2024-02-16', '2024-02-23', '2024-03-01', '2024-03-08',
    #                '2024-03-15', '2024-04-19', '2024-05-17', '2024-06-21', '2024-07-19',
    #                '2024-09-20', '2024-12-20', '2025-01-17', '2025-06-20', '2025-12-19',
    #                '2026-01-16']
    # df = pd.DataFrame(expirations, columns=['Expiry Date'])
    # print(df)
    # saveCsv(df, None, 'expirations.csv')

    # Friday, March 29 IS THE ONLY US HOLIDAY TO COINCIDE WITH QUANTT TIMELINE
    path = 'AMD Historical Options Data'
    logsPath = 'Logs'

    if not os.path.exists(path):
        os.makedirs(path)

    if not os.path.exists(logsPath):
        os.makedirs(logsPath)

    # Generate a log filename based on the current date
    currentDate = datetime.now().strftime("%Y-%m-%d")
    logFilename = f"{currentDate}.txt"
    logFilePath = os.path.join(logsPath, logFilename)

    with open(logFilePath, 'a') as logFile:
        originalStdout = sys.stdout
        originalStderr = sys.stderr

        try:
            sys.stdout = logFile
            sys.stderr = logFile
            checkExpiries(datetime.now() - timedelta(days=1))
            print("Expiries are current")

            savedExpiries = pd.read_csv('expirations.csv')
            savedExpiries['Expiry Date'] = savedExpiries['Expiry Date'].str.replace("-", "")
            expirations = savedExpiries['Expiry Date'].tolist()
            print(f"Expiries: {expirations}")

            savedStrikes = pd.read_csv('strikes.csv')
            strikes = savedStrikes['Strike Price'].tolist()
            print(f"Strikes: {strikes}")

            days = getTradingDays(datetime.now())
            print(f"Days: {days}")

            for day in days:
                savePath = os.path.join(path, day)
                if not os.path.exists(savePath):
                    print(f"Saving: {day} data in {savePath}")
                    os.makedirs(savePath)
                    day += ' 09:30:00'
                    dayDateTime = datetime.strptime(day, '%Y-%m-%d %H:%M:%S')
                    main(ib, savePath, expirations, strikes, dayDateTime)
                    print("--------------------------------------------------\n\n\n")
            EOD = datetime.strptime(datetime.now().strftime("%Y%m%d") +
                                    ' 16:15:00', "%Y%m%d %H:%M:%S")
            if EOD < datetime.now():
                currentPath = os.path.join(path, datetime.now().strftime("%Y-%m-%d"))
                print(f"Saving: {datetime.now().strftime("%Y-%m-%d")} data in {currentPath}")
                main(ib, currentPath, expirations, strikes, datetime.now())

        except Exception:
            # Print the stack trace to the log file
            traceback.print_exc()

        finally:
            # Restore the original stdout and stderr
            sys.stdout = originalStdout
            sys.stderr = originalStderr
    # Closes the IBKR API Client connection
    ib.disconnect()
