import data_collection
import pandas as pd
import numpy as np
import os
import warnings
warnings.filterwarnings("ignore")

data = data_collection.main()

customer_df = data['customer_df']
geolocation_df = data['geolocation_df']
order_items_df = data['order_items_df']
order_payments_df = data['order_payments_df']
order_reviews_df = data['order_reviews_df']
orders_df = data['orders_df']
products_df = data['products_df']
sellers_df = data['sellers_df']

def featureEnginering():
    # We remove the 'review_comment_title' column
    order_reviews_df.drop('review_comment_title', axis=1, inplace=True)
    # We replace the NaN values of 'review_comment_message' with 'Unspecified'
    order_reviews_df['review_comment_message'].fillna("Unspecified", inplace=True)
    # Modified 'review_creation_date' in datetime
    order_reviews_df['review_creation_date'] = pd.to_datetime(order_reviews_df['review_creation_date'])
    # Modified 'review_answer_timestamp' in datetime
    order_reviews_df['review_answer_timestamp'] = pd.to_datetime(order_reviews_df['review_answer_timestamp'])
    # Survey response time in hours
    order_reviews_df['answer_hour'] = order_reviews_df['review_answer_timestamp'].dt.hour
    # Modified 'review_creation_date' in datetime
    order_reviews_df['review_creation_date'] = pd.to_datetime(order_reviews_df['review_creation_date'])
    # Survey response time in days
    order_reviews_df['day_of_month'] = order_reviews_df['review_creation_date'].dt.day

    # We eliminate the rows that contain NaN in 'products'
    products_df.dropna(axis=0, inplace=True)

    # We use the fill() method to replace NULL values with the value of the previous row
    orders_df['order_delivered_customer_date'] = orders_df['order_delivered_customer_date'].fillna(method='ffill')
    # Modified 'order_purchase_timestamp' in datetime
    orders_df['datetime'] =  pd.to_datetime(orders_df['order_purchase_timestamp'])
    # Rows with missing NaN values are deleted
    orders_df.dropna(axis=0, inplace=True)
    # We create two columns separating only the dates.
    orders_df['delivered_time'] = pd.to_datetime(orders_df['order_delivered_customer_date'].str[:10], format='%Y-%m-%d').dt.date
    orders_df['estimated_time'] = pd.to_datetime(orders_df['order_estimated_delivery_date'].str[:10], format='%Y-%m-%d').dt.date
    # We create a new column with the difference in days of 'estimated time' and 'delivered time'.
    orders_df['diff_days'] = orders_df['delivered_time'] - orders_df['estimated_time']
    orders_df['diff_days'] = pd.to_timedelta(orders_df['diff_days'])
    orders_df['diff_days'] = orders_df['diff_days'].dt.days
    # We create a new column with the number of weeks spent per year.
    orders_df['weekly'] = pd.to_datetime(orders_df['order_delivered_customer_date']).dt.isocalendar().week
    # We create a new column with the year and month of 'order_delivered_customer_date'.
    orders_df['yearly'] = pd.to_datetime(orders_df['order_delivered_customer_date']).dt.to_period('M')
    orders_df['yearly'] = orders_df['yearly'].astype(str)
    # Convert an 'object' to an object of type 'datetime'.
    orders_df["order_purchase_timestamp"] = pd.to_datetime(orders_df["order_purchase_timestamp"])

    # A new column is created in the order payments dataset called 'value_log' that contains the logarithm values of the payment value.
    order_payments_df['value_log'] = order_payments_df['payment_value'].apply(lambda x: np.log(x) if x > 0 else 0)

    # We add a new column that contains only 10 digits of seller_id
    sellers_df['seller_id_small'] = sellers_df['seller_id'].str[-10:]

def mergingDatasets():
    total_orders_df = orders_df.merge(order_items_df, on='order_id', how='inner')
    product_orders_df = total_orders_df.merge(products_df, on='product_id', how='inner')
    seller_products_df = product_orders_df.merge(sellers_df, on='seller_id', how='inner')
    payments_df = seller_products_df.merge(order_payments_df, on='order_id', how='inner')
    customer_order_df = payments_df.merge(customer_df, on='customer_id', how='inner')
    olist_df = customer_order_df.merge(order_reviews_df, on='order_id', how='inner')

    return olist_df

def removeColumns(df) -> None:
    columns_to_delete = ['customer_id', 'order_status', 'order_approved_at', 
                       'order_delivered_carrier_date', 'order_delivered_customer_date', 
                       'order_estimated_delivery_date', 'delivered_time', 'estimated_time', 
                       'yearly', 'order_item_id', 'shipping_limit_date', 'product_name_lenght', 
                       'product_description_lenght', 'product_photos_qty', 'product_weight_g', 
                       'product_length_cm', 'product_height_cm', 'product_width_cm', 
                       'customer_state', 'review_id', 'review_comment_message', 
                       'review_answer_timestamp']
    
    df.drop(columns=columns_to_delete, inplace=True)

    return df

def main():
    featureEnginering()
    # print(mergingDatasets().info())
    print(removeColumns(mergingDatasets()).info())
    datasets = {
        'customer_df': customer_df,
        'geolocation_df': geolocation_df,
        'order_items_df': order_items_df,
        'order_payments_df': order_payments_df,
        'order_reviews_df': order_reviews_df,
        'orders_df': orders_df,
        'products_df': products_df,
        'sellers_df': sellers_df,
        'olist_df': removeColumns(mergingDatasets())
    }

    directory = 'data/processed'

    if not os.path.exists(directory):
        os.makedirs(directory)

    for names, df in datasets.items():
        csv_file_path = os.path.join(directory, f'{names}.csv')
        df.to_csv(csv_file_path, index=False)

if __name__ == "__main__":
    main()



