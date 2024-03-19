import numpy as np
import matplotlib.pyplot as plt


def heston_model_paths(S0, V0, r, kappa, theta, xi, rho, T, dt, paths):
    """
    Generate paths for the Heston model.

    Parameters:
    S0 : float - initial stock price
    V0 : float - initial variance
    r : float - risk-free rate
    kappa : float - rate of reversion
    theta : float - long-run variance
    xi : float - volatility of volatility
    rho : float - correlation between asset return and volatility
    T : float - time to maturity
    dt : float - time step
    paths : int - number of paths to simulate

    Returns:
    S : ndarray - simulated paths for the asset price
    V : ndarray - simulated paths for the variance
    """
    # Time points
    N = round(T / dt)
    t = np.linspace(0, T, N)

    # Initialize arrays
    S = np.zeros((N, paths))
    V = np.zeros((N, paths))
    S[0] = S0
    V[0] = V0

    # Generate random Brownian Motion
    dwS = np.random.normal(0, np.sqrt(dt), (N - 1, paths))
    dwV = np.random.normal(0, np.sqrt(dt), (N - 1, paths))
    dwV = rho * dwS + np.sqrt(1 - rho ** 2) * dwV

    for i in range(1, N):
        # Ensure that variance stays positive
        V[i] = V[i - 1] + kappa * (theta - np.maximum(V[i - 1], 0)) * dt + xi * np.sqrt(np.maximum(V[i - 1], 0)) * dwV[
            i - 1]
        S[i] = S[i - 1] * np.exp(
            (r - 0.5 * np.maximum(V[i - 1], 0)) * dt + np.sqrt(np.maximum(V[i - 1], 0)) * dwS[i - 1])

    return S, V


# Parameters for AMD
S0 = 138.56  # Initial AMD stock price
V0 = 0.513  # Initial volatility (variance of the stock log returns)
r = 0.0535  # Risk-free rate
kappa = 2.0  # Rate of reversion
theta = 0.04  # Long-run variance
xi = 0.1  # Volatility of volatility
rho = -0.7  # Correlation between stock and volatility
T = 1  # Time to maturity in years
dt = 1 / 252  # Daily time step
paths = 10  # Number of simulated paths

# Generate paths
S, V = heston_model_paths(S0, V0, r, kappa, theta, xi, rho, T, dt, paths)

# Plot the first few paths
plt.figure(figsize=(14, 7))
for i in range(paths):
    plt.plot(S[:, i])
plt.title('Simulated AMD Stock Price Paths by Heston Model')
plt.xlabel('Time Days')
plt.ylabel('Stock Price')
plt.show()
