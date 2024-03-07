# Montecarlo Simulation base code (No data collection or processing)
import numpy as np
from numpy.random import sample
import pandas as pd


def montecarlo(price, strike, maturity, rfr, volatility, drift, timeSteps=50, simulations=10000):
    '''
    Runs a simulation to find the expected option price using montecarlo simulation
    
    Parameters:
    
        price (float) - Initial stock price
        strike (float) - strike price
        maturity (float) - time to maturity in years
        rfr (float) - risk free rate
        volatility (float) - volatility
        timeSteps (int) - number of time steps (variable)
        simulations (int) - number of simulations the montecarlo will run (variable)
    
    Returns:
        estimated option price (float)
    
    '''
    
    
    # if there was actual input data, dummy data for testing purposes
    # dates = pd.date_range(start="2022-01-01", end="2023-01-01", freq='B')
    # dummy_prices = strike * np.exp(np.cumsum(np.random.normal(0, volatility,
    # size=len(dates)))) -Don't need these dummy prices anymore.
    
    #historical_data = pd.DataFrame(data={'Date': dates, 'Price':dummy_prices}) 
    #historical_data.set_index('Date', inplace=True)
    #daily_returns = historical_data['Price'].pct_change().dropna()
    #estimated_drift = np.mean(daily_returns) * 252 
    #estimated_volatility = np.std(daily_returns) * np.sqrt(252)
    
    dt = maturity / timeSteps
    S = np.zeros((timeSteps + 1, simulations ))
    S[0] = price
    
    
    for time in range(1, timeSteps + 1):
        z = np.random.standard_normal(simulations) #just a normal distribution
        S[time] = S[time - 1] * np.exp((drift - 0.5 * volatility ** 2) * dt + volatility * np.sqrt(dt) * z)
        
        # Calculating the Monte Carlo estimator for option
    
    
    CO = (np.exp(-rfr * maturity) * np.sum(np.maximum(S[-1] - strike, 0))) / simulations
    return CO  

def montecarlo_rolling(init_price, strike, rfr, sample_returns, timeSteps=30, simulations=5000):
    num_samples = sample_returns.size
    sample_returns = np.tile(sample_returns, simulations).reshape((num_samples, simulations))
    #sample_returns must be given as a numpy array.
    N = np.sqrt(252) # Conversion param to put variance into correct units.
    dt = 1/252 #length of timeStep, in (trading) years. Using 1 trading day.

    prices = np.zeros((timeSteps + 1, simulations)) # add one, as we keep original.
    sim_returns = np.zeros((timeSteps,simulations))

    prices[0] = init_price
     
    for time in range(timeSteps):
        returns = np.concatenate((sample_returns, sim_returns[:time]),axis=0)
        drift = returns.mean() * 252
        volatility = returns.std() * N
        z = np.random.standard_normal(simulations) # array of n standard normal samples.
        prices[time + 1] = prices[time] * np.exp((drift - 0.5 * volatility ** 2) * dt + volatility * np.sqrt(dt) * z)
        sim_returns[time] = (prices[time + 1] / prices[time]) - 1

    avg_gain = (np.exp(-rfr * timeSteps/252) * np.sum(np.maximum(prices[-1] - strike, 0))) / simulations
    
    return avg_gain

    # I won't allow manual maturity, as this code needs timesteps to be in days. Will calculate maturity based off time steps.
    # A modification of the montecarlo code to update the volatility, drift based off the new time.
    
    # Similarly, need the sample to re-calculate volatility and spread.

  





if __name__ == "__main__":
    # result = montecarlo(100, 105, 1, 0.0388, 0.5)
    # print(result)
    pass
        
    
    
    
    
    
    
    
    
