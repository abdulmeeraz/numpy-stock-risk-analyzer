# 📊 NumPy Stock Risk & Return Analyzer

This project focuses on building a **stock market data analysis pipeline using pure NumPy**, starting from **raw, messy CSV data** and performing **professional-grade data cleaning** before analysis.

The goal is to strengthen **NumPy fundamentals** by avoiding Pandas and working close to how data is handled internally.

---

## 🚀 Project Objective
- Work with **raw real-world–like financial data**
- Perform **data loading and cleaning using NumPy only**
- Understand and apply **boolean masking, vectorization, and array logic**
- Build a clean foundation for future **risk & return analysis**

---

## 📂 Project Structure (Current)
numpy-stock-risk-analyzer/
│
├── data_cleaning.py
├── raw_stock_prices.csv
├── .gitignore
└── README.md


---

## 📊 Dataset Description

**File:** `raw_stock_prices.csv`

- Each **row** represents one trading day  
- Each **column** represents a stock  

| Column | Description |
|------|------------|
| Stock_A | Closing price of Stock A |
| Stock_B | Closing price of Stock B |
| Stock_C | Closing price of Stock C |
| Stock_D | Closing price of Stock D |

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
- Verified array shape and data type

### 2️⃣ Data Cleaning Strategy
- Defined a valid stock price as **price > 0**
- Chose **row-wise cleaning** for time-series integrity
- Decided to drop rows with missing or invalid prices

### 3️⃣ Data Cleaning Implementation
Implemented a full cleaning pipeline using NumPy:
- Removed extra whitespace using `np.char.strip`
- Detected missing values using boolean masking
- Dropped rows containing missing values
- Safely converted string data to `float`
- Detected and removed rows with zero or negative prices
- Performed sanity checks on cleaned data

### ✔ Final Cleaned Data
- Shape: `(5, 4)`
- Minimum price: `> 0`
- Data is now safe for numerical analysis

---

## 🧠 NumPy Concepts Used
- `np.genfromtxt`
- Vectorized string operations (`np.char.strip`)
- Boolean masking
- `np.any` and `np.all` with `axis`
- Safe type conversion using `astype(float)`
- Array slicing and validation

---

## ⏭️ Next Steps
- Calculate daily returns using NumPy
- Analyze volatility (risk)
- Study correlations between stocks
- Extract analytical insights

---

## 📌 Note
The data loading and cleaning logic is currently implemented in a **single script** for clarity during learning.  
The project will be modularized into separate files as analysis features are added.
