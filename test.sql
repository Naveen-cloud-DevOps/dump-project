-- Create database if not exists
CREATE DATABASE IF NOT EXISTS dev;

-- Use the database
USE dev;

CREATE TABLE orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    address TEXT,
    product VARCHAR(50),
    order_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
