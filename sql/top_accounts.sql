SELECT account_id, SUM(amount) AS net_spent
FROM transactions
GROUP BY account_id
ORDER BY net_spent
LIMIT 5;
