import numpy as np
import pandas as pd 
from scipy.stats import norm

def optionPrice(price, strike, rate, volatility, expires, _type="call"):
    """
    Returns the price of an option, using the black scholes formula.
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


print(optionPrice(price=140, strike=100, rate=0.1, expires=1, volatility=0.3, _type="put"))


