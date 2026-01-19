# 📊 NumPy Stock Risk & Return Analyzer

This project focuses on building a **stock market data analysis pipeline using pure NumPy**, starting from **raw, messy CSV data** and progressing through **data cleaning and time-series return analysis**.

The objective is to strengthen **core NumPy skills** by avoiding Pandas and working directly with arrays, boolean masking, and vectorized operations.

---

## 🚀 Project Objectives
- Work with **real-world–like raw financial data**
- Perform **data loading, cleaning, and analysis using NumPy only**
- Apply **boolean masking, slicing, and vectorization**
- Build a solid foundation for **risk & return analysis**

---

## 📂 Project Structure (Current)
numpy-stock-risk-analyzer/
│
├── data_cleaning.py
├── returns_analysis.py
├── raw_stock_prices.csv
├── clean_prices.npy
├── .gitignore
└── README.md


---

## 📊 Dataset Description

**File:** `raw_stock_prices.csv`

- Each **row** represents one trading day  
- Each **column** represents a stock  

| Column   | Description                  |
|----------|------------------------------|
| Stock_A  | Closing price of Stock A     |
| Stock_B  | Closing price of Stock B     |
| Stock_C  | Closing price of Stock C     |
| Stock_D  | Closing price of Stock D     |

### Raw data intentionally contains:
- Missing values
- Extra whitespace
- Zero prices
- Negative prices

This simulates **real-world dirty financial data**.

---

## ✅ Progress Completed So Far

### 1️⃣ Raw Data Loading
- Loaded CSV using `numpy.genfromtxt`
- Preserved missing values and formatting issues
- Verified array shape and data types

---

### 2️⃣ Data Cleaning Strategy
- Defined a valid stock price as **price > 0**
- Applied **row-wise cleaning** to preserve time-series integrity
- Dropped rows containing missing or invalid prices

---

### 3️⃣ Data Cleaning Implementation
Implemented a full cleaning pipeline using NumPy:
- Removed extra whitespace using `np.char.strip`
- Detected missing values using boolean masking
- Dropped rows with missing values
- Safely converted string data to `float`
- Removed rows with zero or negative prices
- Saved cleaned data as `clean_prices.npy` for reuse

**Final cleaned data:**
- Shape: `(5, 4)`
- Minimum price: `> 0`
- Data ready for numerical analysis

---

### 4️⃣ Daily Returns Calculation
- Loaded cleaned prices from `clean_prices.npy`
- Correctly aligned time-series data using slicing
- Calculated **daily returns** using vectorized NumPy operations
- Performed sanity checks (min/max values, NaN, Inf)
- Computed **mean daily return per stock**

---

## 🧠 NumPy Concepts Used
- `np.genfromtxt`
- Vectorized string operations (`np.char.strip`)
- Boolean masking
- `np.any` and `np.all` with `axis`
- Safe type conversion using `astype(float)`
- Time-series slicing
- Vectorized arithmetic operations

---

## ⏭️ Next Steps
- Calculate volatility (risk) using standard deviation
- Analyze correlations between stocks
- Perform basic portfolio-level analysis
- Extract and interpret financial insights

---

## 📌 Note
During the learning phase, data loading, cleaning, and analysis logic are kept in **simple, readable scripts**.  
The project will be modularized further as additional analytical components are added.
