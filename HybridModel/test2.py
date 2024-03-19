import numpy as np
import scipy.integrate as integrate

# Heston model parameters
params = {
    'S0': 138.56,  # Spot price
    'V0': 0.513,  # Initial variance
    'r': 0.0535,  # Risk-free rate
    'kappa': 2.0,  # Mean reversion rate
    'theta': 0.04,  # Long-term variance
    'xi': 0.1,  # Volatility of volatility
    'rho': -0.7  # Correlation coefficient between asset return and volatility
}


# Characteristic function of the Heston model
def heston_char_func(u, T, params):
    kappa, theta, xi, rho, V0, r = params['kappa'], params['theta'], params['xi'], params['rho'], params['V0'], params[
        'r']
    lambda_ = -rho * xi * u * 1j
    d = np.sqrt((lambda_ + kappa) ** 2 + (xi ** 2) * (u ** 2 + u * 1j))
    g = (kappa + lambda_ - d) / (kappa + lambda_ + d)

    C = kappa * (2 * np.log((1 - g * np.exp(-d * T)) / (1 - g)) + d * T * (1 - np.exp(-d * T)) / (
                1 - g * np.exp(-d * T)))
    D = ((kappa + lambda_ - d) / (xi ** 2)) * ((1 - np.exp(-d * T)) / (1 - g * np.exp(-d * T)))

    char_func = np.exp(C * theta + D * V0 + 1j * u * r * T)
    return char_func


# Heston model option price (Fourier transform method, simplified)
def heston_option_price(T, K, params, call=True, upper_bound=100, limit=100):
    S0 = params['S0']
    integrand = lambda u: (np.exp(-1j * u * np.log(K)) * heston_char_func(u - (1j * 0.5), T, params) / (
                1j * u * heston_char_func(-1j * 0.5, T, params))).real
    integral, err = integrate.quad(integrand, 0, upper_bound, limit=limit)

    if call:
        price = S0 - (np.sqrt(K) / np.pi) * integral
    else:  # put
        price = (np.sqrt(K) / np.pi) * integral - S0 + K * np.exp(-params['r'] * T)

    return price


# Example usage
T = (1*0.1643835616438356)  # Time to maturity
K = 170  # Strike price
price_call = heston_option_price(T, K, params, call=True)
print(f"Call Option Price: {price_call}")
