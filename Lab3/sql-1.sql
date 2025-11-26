-- Table deleting
-- Delete existing tables if they exist
DROP TABLE IF EXISTS Customers;
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Shippings;





-- Create the job_positions table
CREATE TABLE job_positions (
    position_id INT PRIMARY KEY,
    position_name VARCHAR(255)
);

-- Create the locations table
CREATE TABLE locations (
    location_id INT PRIMARY KEY,
    location_name VARCHAR(255)
);

-- Create the customers table
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(255)
);

-- Create the sales_order table with a foreign key to customers
CREATE TABLE sales_order (
    order_id INT PRIMARY KEY,
    customer_id INT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Create the products table
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(255)
);

-- Create the prices table with a foreign key to products
CREATE TABLE prices (
    product_id INT,
    list_price DECIMAL,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Create the employees table
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(255),
    job_title VARCHAR(255)
);

-- Create the departments table
CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(255)
);



-- Insert data into job_positions
INSERT INTO job_positions VALUES (1, 'Manager'), (2, 'Salesperson'), (3, 'Analyst'), (4, 'Developer'), (5, 'Consultant');

-- Insert data into locations
INSERT INTO locations VALUES (1, 'New York'), (2, 'San Francisco'), (3, 'Los Angeles'), (4, 'Chicago'), (5, 'Austin');

-- Insert data into customers
INSERT INTO customers VALUES (1, 'John Doe'), (2, 'Jane Smith'), (3, 'Emily Davis'), (4, 'Michael Brown'), (5, 'Sarah Johnson');

-- Insert data into sales_order
INSERT INTO sales_order VALUES (1, 1), (2, 2), (3, 3), (4, 4), (5, 5);

-- Insert data into products
INSERT INTO products VALUES (1, 'Laptop'), (2, 'Mouse'), (3, 'Keyboard'), (4, 'Monitor'), (5, 'Printer');

-- Insert data into prices
INSERT INTO prices VALUES (1, 1000.00), (2, 20.00), (3, 50.00), (4, 200.00), (5, 150.00);

-- Insert data into employees
INSERT INTO employees VALUES (1, 'Alice', 'Manager'), (2, 'Bob', 'Salesperson'), (3, 'Charlie', 'Analyst'), (4, 'David', 'Developer'), (5, 'Eve', 'Consultant');

-- Insert data into departments
INSERT INTO departments VALUES (1, 'IT'), (2, 'HR'), (3, 'Finance'), (4, 'Sales'), (5, 'Marketing');





-- a)
SELECT * FROM job_positions;

-- b)
SELECT * FROM locations ORDER BY location_id DESC;

-- c)
SELECT sales_order.order_id, customers.customer_name 
FROM sales_order 
JOIN customers ON sales_order.customer_id = customers.customer_id;

-- d)
SELECT products.product_name, prices.list_price 
FROM products 
LEFT JOIN prices ON products.product_id = prices.product_id;

-- e)
SELECT sales_order.order_id, customers.customer_name 
FROM sales_order 
JOIN customers ON sales_order.customer_id = customers.customer_id;

-- f)
SELECT products.product_name, prices.list_price 
FROM products 
LEFT JOIN prices ON products.product_id = prices.product_id;