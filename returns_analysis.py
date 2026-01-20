import numpy as np

import numpy as np

# -----------------------------
# Load cleaned stock prices
# -----------------------------
clean_prices = np.load("clean_prices.npy")

print("Clean prices shape:", clean_prices.shape)
print("Sample prices:\n", clean_prices[:3])

# -----------------------------
# Align prices for daily returns
# -----------------------------
previous_prices = clean_prices[:-1]
current_prices = clean_prices[1:]

# -----------------------------
# Calculate daily returns
# -----------------------------
daily_returns = (current_prices - previous_prices) / previous_prices

print("\nDaily returns shape:", daily_returns.shape)
print("Sample daily returns:\n", daily_returns[:3])

# -----------------------------
# Sanity checks
# -----------------------------
print("\nMin return:", daily_returns.min())
print("Max return:", daily_returns.max())
print("Contains NaN:", np.isnan(daily_returns).any())
print("Contains Inf:", np.isinf(daily_returns).any())

# -----------------------------
# Mean daily return per stock
# -----------------------------
avg_daily_returns = np.mean(daily_returns, axis=0)
print("\nAverage daily return per stock:\n", avg_daily_returns)

# ------------------------------------
# Volatility of daily return per stock
# ------------------------------------
volatility = np.std(daily_returns,axis=0) 
print("\nVolatility of daily return per stock:\n", volatility)

# ---------------------
# risk adjusted returns
# ---------------------
risk_adjusted_return = avg_daily_returns / volatility
print("risk adjusted returns :\n",risk_adjusted_return)

# --------------------
# Correlation Analysis
# --------------------
correlation_matrix = np.corrcoef(daily_returns.T)
print("Correlation Analysis :\n",correlation_matrix)




