# Dataset Overview

In this file you will find all the relevant information about the dataset, source, tables and fields completely explained for better data understanding and quality of work. Please refer to the following index when navigating this section.

- [Dataset Overview](#dataset-overview)
  - [General Information](#general-information)
  - [Dataset Schema](#dataset-schema)
  - [Datasets Description](#datasets-description)
  - [Fields Description](#fields-description)
    - [Customers](#customers)
    - [Sellers](#sellers)
    - [Products](#products)
    - [Geolocation](#geolocation)
    - [Order Items](#order-items)
    - [Order Payments](#order-payments)
    - [Order Reviews](#order-reviews)
    - [Orders Info](#orders-info)

## General Information

* **Name:** Brazilian E-Commerce Public Dataset by Olist
* **Source:** Kaggle - [More Information](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce?select=olist_order_items_dataset.csv)
* **Datasets Quantity:** 8
* **Authors:** Olist, Andre Sionek, Dabague, Francisco Magioli
* **Tags:** Business, Data Visualization, Exploratory Data Analysis, Brazil, eCommerce

## Dataset Schema

The following image contains relevant information about the relations and keys between each dataset used.

![Dataset Schema](https://i.imgur.com/HRhd2Y0.png)

## Datasets Description

This table is a comprehensive reference of types and description for each dataset used in this project.

| Dataset         | Type            | Description                                                   |
| --------------- | --------------- | ------------------------------------------------------------- |
| Customers       | Dimension Table | Customers relevant information                                |
| Sellers         | Dimension Table | Information about sellers that fulfilled orders made at Olist |
| Products        | Dimension Table | Information about products sold by Olist                      |
| Geolocation     | Dimension Table | Relevant information about Brazilian Zip Codes                |
| Orders Items    | Fact Table      | Information about items purchased within each order           |
| Orders Payments | Fact Table      | Information about order payment options and value             |
| Orders Reviews  | Fact Table      | Information about reviews made by the customer (via Email)    |
| Orders Info.    | Fact Table      | General information about each order                          |

## Fields Description

In this section all columns in each dataset will be described for clarity. Please refer to the following tables for understanding the dimensional and factual data in this dataset.

### Customers

| Column                   | Description                            |
| ------------------------ | -------------------------------------- |
| customer_id              | Customer id key to other datasets      |
| customer_zip_code_prefix | First five digits of customer zip code |
| customer city            | Customer city name                     |
| customer state           | Customer state name                    |

### Sellers

| Column                 | Description                       |
| ---------------------- | --------------------------------- |
| seller_id              | Seller unique identifier          |
| seller_zip_code_prefix | First 5 digits of seller zip code |
| seller_city            | Seller city name                  |
| seller_state           | Seller state name                 |

### Products

| Column                     | Description                                     |
| -------------------------- | ----------------------------------------------- |
| product_id                 | Unique product identifier                       |
| product_category_name      | Product category, in english                    |
| product_name_lenght        | Number of characters in the product name        |
| product_description_lenght | Number of characters in the product description |
| product_photos_qty         | Number of product published photos              |
| product_weight_g           | Product weight measured in grams                |
| product_lenght_cm          | Product length measured in centimeters          |
| product_width_cm           | Product width measured in centimeters           |

### Geolocation

| Column          | Description                |
| --------------- | -------------------------- |
| zip_code_prefix | First 5 digits of zip code |
| lat             | Latitude coordinates       |
| lng             | Longitude coordinates      |
| city            | City name                  |
| state           | State name                 |

### Order Items

| Column              | Description                                                                |
| ------------------- | -------------------------------------------------------------------------- |
| order_item_id       | Sequential number containing number of items included in the same order    |
| product_id          | Unique product identifier                                                  |
| seller_id           | Unique seller identifier                                                   |
| shipping_limit_date | Seller shipping deadline for handling the order over the logistics partner |
| price               | Unitary item price                                                         |
| freight_value       | Freight value per item                                                     |

### Order Payments

| Column               | Description                                                       |
| -------------------- | ----------------------------------------------------------------- |
| order_id             | Unique order identifier                                           |
| payment_sequential   | Sequence and quantity of payment methods used for paying an order |
| payment_type         | Payment method chosen by the customer                             |
| payment_installments | Number of installments chosen by the customer                     |
| payment_value        | Order transaction value                                           |

### Order Reviews

| Column                  | Description                                                             |
| ----------------------- | ----------------------------------------------------------------------- |
| review_id               | Unique review identifier                                                |
| order_id                | Unique order identifier                                                 |
| review_score            | Note ranging from 1 to 5 given by the customer on a satisfaction survey |
| review_comment_title    | Comment title from the review left by the customer, in Portuguese       |
| review_comment_message  | Comment message from the review left by the customer, in Portuguese     |
| review_creation_date    | Date in which the satisfaction survey was sent to the customer          |
| review_answer_timestamp | Shows satisfaction survey answer timestamp                              |

### Orders Info

| Column                        | Description                                                        |
| ----------------------------- | ------------------------------------------------------------------ |
| order_id                      | Unique order identifier                                            |
| customer_id                   | Unique customer identifier                                         |
| order_status                  | Order status (delivered, shipped, etc.)                            |
| order_purchase_timestamp      | Order purchase date and time                                       |
| order_approved_at             | Payment approval timestamp                                         |
| order_delivered_carrier_date  | Order posting date and time, when handled by the logistics partner |
| order_delivered_customer_date | Order delivery date to the customer                                |
| order_estimated_delivery_date | Order delivery date estimated at the purchase moment               |