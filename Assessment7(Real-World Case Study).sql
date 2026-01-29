CREATE DATABASE ecommerce_db;
use ecommerce_db;

CREATE TABLE customers (
     customer_id INT PRIMARY KEY,
     name VARCHAR(100) NOT NULL,
     city VARCHAR(50)
);

CREATE TABLE orders (
     order_id INT PRIMARY KEY,
     customer_id INT,
     order_date DATE,
     amount DECIMAL(10, 2),
     FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE products (
     product_id INT PRIMARY KEY,
     product_name VARCHAR(100) NOT NULL,
     price DECIMAL(10, 2)
);

CREATE TABLE order_items(
     order_id INT,
     product_id INT,
     quality INT,
     PRIMARY KEY (order_id, product_id),
     FOREIGN KEY (order_id) REFERENCES orders(order_id),
     FOREIGN KEY (product_id) REFERENCEs products(product_id)
);

INSERT INTO  customers (customer_id, name, city) VALUES
(1, 'Krish patel', 'GUJARAT'),
(2, 'Yash patel', 'RAJKOT'),
(3, 'Tax Barot', 'SURAT'),
(4, 'Aryan Patel', 'AHMEDABAD'),
(5, 'Dhruv Tandel', 'VADODARA');

INSERT INTO products (product_id, product_name, price) VALUES
(101, 'Laptop', 55000),
(102, 'Smartphone', 25000),
(103, 'Headphones', 3000),
(104, 'Keyboard', 1500),
(105, 'Mouse', 800);

INSERT INTO  orders  (order_id, customer_id, order_date, amount) VALUES
(1001, 1, '2024-01-15', 58000),
(1002, 2, '2024-01-20', 25000),
(1003, 3, '2024-02-10', 3000),
(1004, 3, '2024-02-18', 27000),
(1005, 5, '2024-03-05', 56500);

INSERT INTO order_items (order_id, product_id, quality) VALUES
(1001, 101, 1),
(1001, 104, 2),
(1002, 102, 1),
(1003, 103, 1),
(1004, 102, 1),
(1004, 105, 2),
(1005, 101, 1),
(1005, 105, 2);

--Total orders per customer
SELECT 
    c.customer_id,
    c.name,
    COUNT(o.order_id) AS total_orders
FROM customers c
LEFT JOIN orders o
    ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name;

--Customers who never placed an order
SELECT
     c.customer_id,
     c.name
FROM customers c
LEFT JOIN orders o
    ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;

--Highest selling product
SELECT
    p.product_id,
    p.product_name,
    SUM(oi.quality) AS total_quantity_sold
FROM products p
JOIN order_items oi
    ON p.product_id = oi.product_id
GROUP BY p.product_id, p.product_name
ORDER BY total_quantity_sold DESC;

--Monthly sales report
SELECT 
    YEAR(order_date) AS order_year,
    MONTH(order_date) AS order_month,
    SUM(amount) AS total_sales
FROM orders
GROUP BY
   YEAR(order_date),
   MONTH(order_date)
ORDER BY 
   order_year,
   order_month;

--Customers with total purchase > ₹50,000
SELECT 
    c.customer_id,
    c.name,
    SUM(o.amount) AS total_purchase
FROM customers c
JOIN orders o 
   ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name
HAVING SUM(o.amount) > 50000;

--Top 3 cities by revenue
SELECT 
    c.city,
    SUM(o.amount) AS total_revenue
FROM customers c
JOIN orders o 
   ON c.customer_id = o.customer_id
GROUP BY c.city
ORDER BY total_revenue DESC;
      




