# 📊 NumPy Stock Risk & Return Analyzer

This project demonstrates an **end-to-end stock market analysis pipeline built using pure NumPy**, starting from **raw, messy CSV data** and progressing through **data cleaning, return calculation, risk analysis, and correlation-based portfolio insights**.

The primary goal is to strengthen **core NumPy fundamentals** by avoiding Pandas and working directly with arrays, boolean masking, slicing, and vectorized computations.

---

## 🚀 Project Objectives
- Work with **real-world–like raw financial data**
- Perform **data loading, cleaning, and analysis using NumPy only**
- Apply **boolean masking, slicing, and vectorization**
- Build a strong foundation for **risk & return analysis**
- Develop analytical thinking for **portfolio-level insights**

---

## 📂 Project Structure
numpy-stock-risk-analyzer/
│
├── data_cleaning.py # Raw data loading & cleaning pipeline
├── returns_analysis.py # Returns, risk, and correlation analysis
├── raw_stock_prices.csv # Raw input dataset
├── clean_prices.npy # Cleaned NumPy array (persisted output)
├── .gitignore
└── README.md

---

## 📊 Dataset Description

**File:** `raw_stock_prices.csv`

- Dataset size: **~2000 trading days × 4 stocks** (with headers)
- Each **row** represents one trading day  
- Each **column** represents a stock  

| Column   | Description                  |
|----------|------------------------------|
| Stock_A  | Closing price of Stock A     |
| Stock_B  | Closing price of Stock B     |
| Stock_C  | Closing price of Stock C     |
| Stock_D  | Closing price of Stock D     |

### Raw data intentionally includes:
- Missing values
- Extra whitespace
- Zero prices
- Negative prices

This simulates **real-world dirty financial data** commonly encountered in practice.

---

## ✅ Work Completed

### 1️⃣ Raw Data Loading
- Loaded CSV data using `numpy.genfromtxt`
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
- Persisted cleaned data as `clean_prices.npy` for reuse

**Final cleaned dataset:**
- Shape: **slightly fewer than 2000 rows × 4 stocks** (after cleaning)
- Minimum price: `> 0`
- Data is safe for numerical analysis

---

### 4️⃣ Daily Returns & Risk Analysis
- Loaded cleaned prices from `clean_prices.npy`
- Correctly aligned time-series data using slicing
- Calculated **daily returns** using vectorized NumPy operations
- Performed sanity checks (min/max values, NaN, Inf)
- Computed:
  - Mean daily return per stock
  - Volatility (standard deviation of returns)
  - Risk-adjusted return (return ÷ volatility)

---

### 5️⃣ Correlation & Diversification Analysis
- Computed correlation matrix using **daily returns**
- Identified highly correlated stock pairs
- Evaluated diversification benefits using low-correlation assets

---

## 🧠 NumPy Concepts Applied
- `np.genfromtxt`
- Vectorized string operations (`np.char.strip`)
- Boolean masking
- `np.any` and `np.all` with `axis`
- Safe type conversion using `astype(float)`
- Time-series slicing
- Vectorized arithmetic operations
- Correlation analysis using `np.corrcoef`

---

## 📌 Portfolio Insights Summary
- **Stock A** is the most volatile and carries the highest risk.
- **Stock C** is the most stable, with the lowest volatility.
- **Stock C** provides the best **risk-adjusted return**.
- **Stock B and Stock D** are highly correlated and tend to move together.
- **Low-correlated pairs**, such as Stock A and Stock B, improve diversification.

**Overall conclusion:**  
> Stock C emerges as the most balanced investment, offering stable performance, low risk, and strong risk-adjusted returns.

---

## 🏁 Project Status
✅ **Completed**

This project successfully demonstrates:
- Real-world data cleaning using NumPy
- Time-series return calculation
- Risk and volatility measurement
- Risk–return tradeoff analysis
- Correlation-based diversification insights
- Scalability on large time-series datasets (~2000 rows)

---

## 📌 Note
During the learning phase, data loading, cleaning, and analysis logic are intentionally kept in **simple, readable scripts**.  
The project is complete and serves as a solid foundation for further financial analytics and portfolio analysis.
