"""
Stock Market Risk & Return Analyzer
Step 1: Raw data loading and cleaning using NumPy only

This script:
- Loads raw stock price data from CSV
- Cleans missing and invalid values
- Produces a clean NumPy array ready for analysis
"""

import numpy as np
# Load raw data
data = np.genfromtxt("raw_stock_prices.csv", delimiter=",", skip_header=1, dtype=str)

# Strip whitespace
clean_data = np.char.strip(data)

# Remove rows with missing values
valid_cells = clean_data != ""
rows_without_missing = np.all(valid_cells, axis=1)
filtered_data = clean_data[rows_without_missing]

# Convert to float
numeric_data = filtered_data.astype(float)

# Remove rows with invalid prices
valid_price_cells = numeric_data > 0
valid_price_rows = np.all(valid_price_cells, axis=1)
clean_prices = numeric_data[valid_price_rows]

# Final validation
print(clean_prices.shape)
print(clean_prices.min() > 0)
print(clean_prices)

np.save("clean_prices.npy", clean_prices)
print("Clean prices saved successfully.")