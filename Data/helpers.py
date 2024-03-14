from datetime import datetime, timedelta
import holidays
import pandas as pd
import os


def get_week_dates(date):
    # Find Monday of the current week
    start_of_week = date - timedelta(days=date.weekday())
    # Generate dates for the week up to and including the current date
    return [start_of_week + timedelta(days=i) for i in range(date.weekday() + 1)]


def nyse_holidays(year):
    # Initialize US holidays for the specified year
    us_holidays = holidays.US(years=year)
    # NYSE specific adjustments (if any) should be added here
    # Example: us_holidays.pop('2024-07-04') if July 4th falls on a weekend but observed differently by NYSE
    return us_holidays


def getTradingDays(current_date):
    week_dates = get_week_dates(current_date)
    holiday_dates = nyse_holidays(current_date.year)

    # Filter out the holidays from the week's dates
    trading_days = [date for date in week_dates if date not in holiday_dates]

    # Format dates in 'YYYY-MM-DD'
    trading_days_formatted = [date.strftime('%Y-%m-%d') for date in trading_days]
    del trading_days_formatted[-1]
    return trading_days_formatted


def checkExpiries(currentDate):
    savedExpiries = pd.read_csv('expirations.csv')
    # Convert 'Expiration Date' back to datetime for comparison and manipulation
    savedExpiries['Expiry Date'] = pd.to_datetime(savedExpiries['Expiry Date'])
    if currentDate > savedExpiries.iloc[0]['Expiry Date']:
        # Remove the first value from the dataframe
        savedExpiries = savedExpiries.drop(savedExpiries.index[0]).reset_index(drop=True)

        # Determine the date after the 4th indexed value
        fourth_index_date = savedExpiries.iloc[4]['Expiry Date']  # Adjusted to the 4th index
        week_after_fourth = fourth_index_date + timedelta(weeks=1)

        # Find the last business day of that week (Friday or Thursday if Friday is a holiday)
        if week_after_fourth.weekday() > 4:  # If the date is Saturday or Sunday
            last_business_day_fourth = week_after_fourth + timedelta(days=(4 - week_after_fourth.weekday() + 7))
        else:
            last_business_day_fourth = week_after_fourth + timedelta(days=(4 - week_after_fourth.weekday()))

        # Insert the new date after the 4th indexed value
        new_row_fourth = pd.DataFrame({'Expiry Date': [last_business_day_fourth]}, index=[4.5])
        savedExpiries = pd.concat([savedExpiries.loc[:4], new_row_fourth, savedExpiries.loc[5:]]).reset_index(drop=True)
        savedExpiries['Expiry Date'] = savedExpiries['Expiry Date'].dt.strftime('%Y-%m-%d')
        savedExpiries.to_csv('expirations.csv')


def saveCsv(df, path, fileName):
    """
    Saves the given DataFrame to a CSV file in the specified path.

    Args:
        df (pandas.DataFrame): The DataFrame to be saved.
        path (str): The path where the file should be saved. If the folder does not exist, it will be created.
        fileName (str): The name of the file to be saved.

    """
    # Save the DataFrame to CSV in the specified path
    if path is None:
        df.to_csv(fileName)
    else:
        # Check if the folder exists, if not, create it
        if not os.path.exists(path):
            os.makedirs(path)
        df.to_csv(os.path.join(path, fileName))
