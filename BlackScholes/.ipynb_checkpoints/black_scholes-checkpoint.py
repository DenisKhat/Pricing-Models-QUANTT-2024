import numpy as np
import pandas as pd
import yfinance as yf
import datetime
from scipy.stats import norm
from pandas.tseries.holiday import USFederalHolidayCalendar
from pandas.tseries.offsets import CustomBusinessDay
# Allows all columns to display when testing with yfinance
pd.options.display.width = 0


def optionPrice(price, strike, rate, volatility, expires, _type="call"):
    """
    Returns the price of an option, using the Black-Scholes-Merton formula.
    When applying, make sure the time dependant inputs (expires, rate, and volatility) all use the same time units (years, months, etc...).
    
    Args:
        price [float]: the current price of the underlying asset.
        strike [float]: the strike price of the option.
        rate [float]: the current risk free rate of the market.
        volatility [float]: the volatility of the underlying asset's returns
        expires [float]: time until option expires.
        _type [string]: type of the option (put/call). default = call

    Returns [float]:
        The price of the option. 
    """
    d1 = (np.log(price/strike) + (rate + volatility**2/2)*expires) / (volatility*np.sqrt(expires))
    d2 = d1 - volatility * np.sqrt(expires)

    if _type == "call":
        return price * norm.cdf(d1) - strike * np.exp(-rate * expires) * norm.cdf(d2)
    elif _type == "put":
        return strike * np.exp(-rate * expires) * norm.cdf(-d2) - price * norm.cdf(-d1)
    else:
        raise Exception("The provided option type is not valid (put/call)")


def getLastBusinessDay(date):
    previousDay = CustomBusinessDay(calendar=USFederalHolidayCalendar())
    return date - 1 * previousDay


# https://pypi.org/project/yfinance/ < library I used for Yahoo Finance data
# https://algotrading101.com/learn/yfinance-guide/ < good for figuring out it's basics

# risk-free rate can be pulled from https://finance.yahoo.com/quote/%5EIRX?p=%5EIRX
# https://ycharts.com/indicators/3_month_t_bill < good to double-check the YF one is "accurate"

# YTM = (expiration date at 4pm - current datetime) / 365

# volatility = variance of the AMD daily close price from Jan 1, 2023 - Jan 1, 2024
def main():
    """
    previousDay = CustomBusinessDay(calendar=USFederalHolidayCalendar())
    today = pd.Timestamp('2024-01-19')
    #today = pd.Timestamp.today()
    result = today - 1 * previousDay
    print(result)
    choice = input("Pricing today or historical options? (1/2)")
    if choice == "1":
        date = input("What date? (YYYY-MM-DD)")
        lastBD = getLastBusinessDay(date)
    else:
        lastBD = getLastBusinessDay(pd.Timestamp.today())

    lastBD = getLastBusinessDay(pd.Timestamp.today())
    AMD = yf.Ticker("AMD")

    for i, item in enumerate(AMD.options):
        print(f"{i+1}. {item}")

    # As you can see below, I currently have specific settings chosen just for
    # testing the final data being pulled to the program
    #expiry = AMD.options[int(input("Which expiration date? Ex: `1`"))-1]
    expiry = AMD.options[int(1)-1]
    #direction = input("Call or put? [1/2]")
    #strike = float(input("Strike price? Ex: `125`)"))
    strike = float(125)
    optChain = AMD.option_chain(expiry)

    for i in range(0, len(optChain.calls)):
        if optChain.calls.values[i][2] == strike:
            print(f"HOORAY! {i+1}. {optChain.calls.values[i][2]}")
            break

    #print(optChain.underlying["regularMarketOpen"])
    #print(optChain.calls.loc.where(optChain.calls['strike'] == strike))
    #print(optChain.calls.loc[:, "strike"])

    print(optChain)
    print("DONE")
    print(optChain[0])
    print("DONE")
    print(optChain[1])
    print("DONE")
    print(optChain[2])
    #need the 39th index of the underlying column for open price
    """


if __name__ == "__main__":
    main()
    print("Done")
    """
    AMD = yf.Ticker("AMD")
    print(AMD.options)
    print("Done")

    optChain = AMD.option_chain(AMD.options[0])
    print(optChain.calls)
    print("Done")

    print(optionPrice(price=140, strike=100, rate=0.1, expires=1, volatility=0.3, _type="put"))
    """
    #print("Completed")


