# 💳 Finance Transactions Analysis with Python + SQLite

This notebook connects to a local SQLite database and visualizes key financial metrics.

---

## 🛠️ Setup

```python
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to database
conn = sqlite3.connect("finance_transactions.db")
```

---

## 📊 1. Total Spend by Category

```python
query1 = '''
SELECT category, ROUND(SUM(amount), 2) AS total_spent
FROM transactions
GROUP BY category
ORDER BY total_spent;
'''
df1 = pd.read_sql(query1, conn)

df1.plot(kind='barh', x='category', y='total_spent', legend=False, color='skyblue')
plt.title("Total Spend by Category")
plt.xlabel("Amount Spent")
plt.ylabel("Category")
plt.grid(True)
plt.tight_layout()
plt.show()
```

---

## 📈 2. Monthly Net Cash Flow

```python
query2 = '''
SELECT substr(date, 1, 7) AS month, SUM(amount) AS net_cash_flow
FROM transactions
GROUP BY month
ORDER BY month;
'''
df2 = pd.read_sql(query2, conn)

df2.plot(kind='line', x='month', y='net_cash_flow', marker='o')
plt.title("Monthly Net Cash Flow")
plt.xlabel("Month")
plt.ylabel("Net Cash Flow")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

---

## 🧍 3. Top 5 Spending Accounts

```python
query3 = '''
SELECT account_id, SUM(amount) AS net_spent
FROM transactions
GROUP BY account_id
ORDER BY net_spent
LIMIT 5;
'''
df3 = pd.read_sql(query3, conn)

df3.plot(kind='bar', x='account_id', y='net_spent', color='tomato')
plt.title("Top 5 Spending Accounts")
plt.xlabel("Account ID")
plt.ylabel("Net Spent")
plt.grid(True)
plt.tight_layout()
plt.show()
```

---

## ⚠️ 4. Suspicious Withdrawals > 900

```python
query4 = '''
SELECT * FROM transactions
WHERE transaction_type = 'withdrawal' AND amount < -900;
'''
df4 = pd.read_sql(query4, conn)
df4.head()
```

---

## ✅ Close Connection

```python
conn.close()
```
