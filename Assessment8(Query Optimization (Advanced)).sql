--Add index to improve search on orders.customer_id
CREATE NONCLUSTERED INDEX idx_orders_customer_id
ON orders(customer_id);

SELECT * FROM orders WHERE customer_id = 1;

--Use EXPLAIN to analyze query

SET STATISTICS PROFILE ON;
SELECT c.name, o.amount
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id;
SET STATISTICS PROFILE OFF;

--Optimize a slow JOIN query
CREATE NONCLUSTERED INDEX orders_customer_id
ON orders(customer_id);
SELECT c.name, o.order_date, o.amount
FROM orders o
JOIN customers c 
ON o.customer_id =  c.customer_id
WHERE o.customer_id = 1;

--Explain when index should not be used Pending
SELECT *
from orders
where order_date between '2024-01-01' and '2024-04-04';

select * from customers
where city in ('Gujarat', 'Surat');