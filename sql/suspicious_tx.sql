SELECT * FROM transactions
WHERE transaction_type = 'withdrawal' AND amount < -900;
