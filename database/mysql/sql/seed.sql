INSERT INTO users (username, city, created_at) VALUES
('alice', 'Shanghai', '2026-01-10 09:00:00'),
('bob', 'Beijing', '2026-01-11 10:00:00'),
('carol', 'Shanghai', '2026-01-12 11:00:00'),
('dave', 'Shenzhen', '2026-01-13 12:00:00');

INSERT INTO products (name, category, price, stock, created_at) VALUES
('Mechanical Keyboard', 'device', 399.00, 50, '2026-01-01 08:00:00'),
('Mouse', 'device', 129.00, 120, '2026-01-02 08:00:00'),
('Monitor', 'device', 1299.00, 30, '2026-01-03 08:00:00'),
('Notebook', 'office', 19.90, 500, '2026-01-04 08:00:00');

INSERT INTO orders (user_id, total_amount, status, created_at) VALUES
(1, 528.00, 'paid', '2026-02-01 10:00:00'),
(2, 1299.00, 'paid', '2026-02-02 11:00:00'),
(1, 39.80, 'shipped', '2026-02-03 12:00:00'),
(3, 129.00, 'created', '2026-02-04 13:00:00');

INSERT INTO order_items (order_id, product_id, quantity, item_price) VALUES
(1, 1, 1, 399.00),
(1, 2, 1, 129.00),
(2, 3, 1, 1299.00),
(3, 4, 2, 19.90),
(4, 2, 1, 129.00);