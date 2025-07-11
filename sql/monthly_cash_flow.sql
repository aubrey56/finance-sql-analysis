SELECT substr(date, 1, 7) AS month, ROUND(SUM(amount), 2) AS net_cash_flow
FROM transactions
GROUP BY month
ORDER BY month;

