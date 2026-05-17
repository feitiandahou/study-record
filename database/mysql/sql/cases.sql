-- 1. Find the total order amount per user.
SELECT o.user_id, SUM(o.total_amount) AS total_spent
FROM orders AS o
GROUP BY o.user_id;

-- 2. Find users whose total spending is greater than 500.
SELECT o.user_id, SUM(o.total_amount) AS total_spent
FROM orders AS o
GROUP BY o.user_id
HAVING SUM(o.total_amount) > 500;

-- 3. Find the latest two paid orders.
SELECT id, user_id, total_amount, created_at
FROM orders
WHERE status = 'paid'
ORDER BY created_at DESC
LIMIT 2;

-- 4. Count orders by city.
SELECT u.city, COUNT(*) AS order_count
FROM orders AS o
JOIN users AS u ON u.id = o.user_id
GROUP BY u.city;

-- 5. Explain practice target.
EXPLAIN
SELECT id, user_id, total_amount, created_at
FROM orders
WHERE status = 'paid'
ORDER BY created_at DESC
LIMIT 2;