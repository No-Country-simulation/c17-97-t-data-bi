CREATE DATABASE IF NOT EXISTS ecommerce;
USE ecommerce;

-- Dimension Tables --

CREATE TABLE customer (
	customer_id VARCHAR(50),
    customer_unique_id VARCHAR(50),
    customer_zip_code_prefix INT NOT NULL,
    customer_city VARCHAR(50),
    customer_state VARCHAR(30)
);

CREATE TABLE sellers (
	seller_id VARCHAR(50),
    seller_zip_code_prefix INT,
    seller_city VARCHAR(50),
    seller_state VARCHAR(50),
    seller_id_small VARCHAR(30)
);

CREATE TABLE products (
	product_id VARCHAR(50),
    product_category_name VARCHAR(50),
    product_name_lenght INT,
    product_description_lenght INT,
    product_photos_qty INT,
    product_weight_g FLOAT,
    product_lenght_cm FLOAT,
    product_height_cm FLOAT,
    product_width_cm FLOAT
);

CREATE TABLE geolocation (
	zip_code_prefix INT,
    lat FLOAT,
    lng FLOAT,
    city VARCHAR(50),
    state VARCHAR(50)
);

-- Fact Tables --

CREATE TABLE order_items (
	order_id VARCHAR(50),
	order_item_id INT,
    product_id VARCHAR(50),
    seller_id VARCHAR(50),
    shipping_limit_date DATETIME,
    price FLOAT,
    freight_value FLOAT
);

CREATE TABLE order_payments (
	order_id VARCHAR(50),
    payment_sequential INT,
    payment_type VARCHAR(30),
    payment_installments INT,
    payment_value FLOAT,
    value_log FLOAT
);

CREATE TABLE order_reviews (
	review_id VARCHAR(50),
    order_id VARCHAR(50),
    review_score INT,
    review_comment_message VARCHAR(500),
    review_creation_date DATETIME,
    review_answer_timestamp DATETIME
);

CREATE TABLE order_info (
	order_id VARCHAR(50),
    customer_id VARCHAR(50),
    order_status VARCHAR(30),
    order_purchase_timestamp DATETIME,
    order_approved_at DATETIME,
    order_delivered_carrier_date DATETIME,
    order_delivered_customer_date DATETIME,
    order_estimated_delivery_date DATETIME,
    datetime DATETIME,
    delivered_time DATE,
    estimated_time DATE,
    diff_days INT,
    weekly INT,
    yearly VARCHAR(30)
);

DROP TABLE order_payments;
