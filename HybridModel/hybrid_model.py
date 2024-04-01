# Hybrid model based on the Monte-Carlo Simulation base code (No data collection or processing)
import numpy as np
from numpy.random import sample
import pandas as pd


def hybrid_model(init_price, rfr, maturity, sample_returns, timeSteps=30, simulations=5000):
    dt = maturity / timeSteps / 252
    num_samples = sample_returns.size
    sample_returns = np.repeat([sample_returns], simulations, axis=0)
    sample_returns = sample_returns.transpose()
    # print(sample_returns.shape)
    # sample_returns must be given as a numpy array.
    N = np.sqrt(252)  # Conversion param to put variance into correct units.

    prices = np.zeros((timeSteps + 1, simulations)) # add one, as we keep original.
    sim_returns = np.zeros((timeSteps, simulations))

    prices[0] = init_price
    returns = np.concatenate((sample_returns), axis=0)
    volatility = returns.std(axis=0) * N
    drift = returns.mean(axis=0) * 252
    for time in range(timeSteps):
        if time % 100 == 0:
            print(f"Timestep {time} completed")
            # volatility = returns.std(axis=0) * N
        returns = np.concatenate((sample_returns, sim_returns[:time]), axis=0)
        # drift = returns.mean(axis=0) * 252
        # print(volatility[0:2])
        z = np.random.standard_normal(simulations)  # array of n standard normal samples.
        prices[time + 1] = prices[time] * np.exp((drift - 0.5 * volatility ** 2) * dt + volatility * np.sqrt(dt) * z)
        sim_returns[time] = (prices[time + 1] / prices[time]) - 1
        admissable_prices = prices[-1][prices[-1] > init_price]
    avg_price =  (np.sum(admissable_prices) / admissable_prices.size) *  (np.exp(-rfr * (maturity/252)))
    return avg_price, np.max(prices[:, -1]), np.min(prices[:, -1]) #np.maximum(prices[-1]), np.minimum(prices[-1])
  


    # avg_gain = (np.exp(-rfr * maturity/252) * np.sum(np.maximum(prices[-1] - strike, 0))) / simulations
    
    # return avg_gain

    # I won't allow manual maturity, as this code needs timesteps to be in days.
    # 0Will calculate maturity based off time steps.
    # A modification of the montecarlo code to update the volatility, drift based off the new time.

    # Similarly, need the sample to re-calculate volatility and spread.
