import numpy as np

# Number of trading days
num_days = 2000

# Number of stocks
num_stocks = 4

start_prices = np.array([100.0, 120.0, 90.0, 150.0])

print(start_prices.shape)

prices = np.zeros((num_days,num_stocks))

prices[0] = start_prices

print("Prices shape:", prices.shape)
print("First day prices:", prices[0])

# Generate random daily returns
daily_returns = np.random.uniform(
    low=-0.02,
    high=0.02,
    size=(num_days, num_stocks)
)
print(daily_returns.shape)

print("Daily returns shape:", daily_returns.shape)
print("Sample daily returns:\n", daily_returns[:5])

for t in range(1, num_days):
    prices[t] = prices[t - 1] * (1 + daily_returns[t])

print("\nFirst 5 days of prices:\n", prices[:5])
print("\nLast 5 days of prices:\n", prices[-5:])

# Convert prices to string to simulate raw CSV data
raw_data = prices.astype(str)

# Save as raw CSV with headers
np.savetxt(
    "raw_stock_prices.csv",
    raw_data,
    delimiter=",",
    fmt="%s",
    header="Stock_A,Stock_B,Stock_C,Stock_D",
    comments=""
)

print("raw_stock_prices.csv with headers generated successfully")

