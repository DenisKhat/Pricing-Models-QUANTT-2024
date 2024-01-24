# Montecarlo Simulation base code (No data collection or processing)
import numpy as np
import pandas as pd


def montecarlo(price, strike, maturity, rfr, volatility, timeSteps=50, simulations=10000):
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
    dates = pd.date_range(start="2022-01-01", end="2023-01-01", freq='B')
    dummy_prices = strike * np.exp(np.cumsum(np.random.normal(0, volatility,
    size=len(dates))))
    
    historical_data = pd.DataFrame(data={'Date': dates, 'Price':dummy_prices}) 
    historical_data.set_index('Date', inplace=True)
    daily_returns = historical_data['Price'].pct_change().dropna()
    estimated_drift = np.mean(daily_returns) * 252 
    estimated_volatility = np.std(daily_returns) * np.sqrt(252)
    
    dt = maturity / timeSteps
    S = np.zeros((timeSteps + 1, simulations ))
    S[0] = strike
    
    
    for time in range(1, timeSteps + 1): 
        z = np.random.standard_normal(simulations) #just a normal distribution
        S[time] = S[time - 1] * np.exp((estimated_drift - 0.5 * estimated_volatility ** 2) * dt + estimated_volatility * np.sqrt(dt) * z)
        
        # Calculating the Monte Carlo estimator for option
    
    
    CO = (np.exp(-rfr * maturity) * np.sum(np.maximum(S[-1] - strike, 0))) / simulations
    return CO  


result = montecarlo(100, 105, 1, 0.05, 0.2)
print(result)
    
    
    
    
    
    
    
    
    