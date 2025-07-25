 HEAD
# finance-sql-analysis
SQL-based personal finance transaction analysis using SQLite on Linux

# 💳 Finance Transactions Analysis Using SQL (SQLite + Linux)

This project explores synthetic financial transaction data using SQL via SQLite on a Linux environment. It focuses on analyzing personal finance behaviors, identifying trends in income and expenses, and flagging suspicious transaction activity.

---

## 📊 Dataset Overview

- **Source**: Synthetic dataset (generated locally)
- **Rows**: 500 transactions
- **Tool**: SQLite (accessed via `sqlite3` in Linux terminal)

### `transactions` Table

| Column            | Description                          |
|------------------|--------------------------------------|
| `transaction_id` | Unique transaction ID                |
| `account_id`     | Account number                       |
| `date`           | Transaction date (`YYYY-MM-DD`)      |
| `amount`         | Negative = expense, Positive = income|
| `transaction_type`| deposit, withdrawal, transfer, etc. |
| `merchant`       | Vendor or transaction target         |
| `category`       | groceries, rent, salary, etc.        |
| `city`           | Where the transaction occurred       |
| `channel`        | ATM, Mobile, Online, In-Branch       |

---

## 🧠 Key Questions & Insights

### 🧾 1. Total Spend by Category
```sql
SELECT category, ROUND(SUM(amount), 2) AS total_spent
FROM transactions
GROUP BY category
ORDER BY total_spent;
```

### 📈 2. Monthly Net Cash Flow
```sql
SELECT substr(date, 1, 7) AS month, SUM(amount) AS net_cash_flow
FROM transactions
GROUP BY month
ORDER BY month;
```

### 🧍 3. Top 5 Spending Accounts
```sql
SELECT account_id, SUM(amount) AS net_spent
FROM transactions
GROUP BY account_id
ORDER BY net_spent
LIMIT 5;
```

### ⚠️ 4. Suspicious Withdrawals
```sql
SELECT * FROM transactions
WHERE transaction_type = 'withdrawal' AND amount < -900;
```

---

## 🧰 Tools Used

- Linux Terminal
- SQLite (`sqlite3`)
- SQL
- [Optional] Python for data generation
- [Optional] DB Browser or DBeaver

---

## 📁 Files in this Repo

| File/Folders            | Description                          |
|-------------------------|--------------------------------------|
| `finance_transactions.db` | SQLite database (500 transactions) |
| `sql/`                  | Reusable SQL query scripts           |
| `README.md`             | This project description             |

---

## 📌 How to Run It

```bash
sqlite3 finance_transactions.db
.read sql/spending_by_category.sql
```
>>>>>>> cae1eb2 (Initial commit: finance SQL project)
