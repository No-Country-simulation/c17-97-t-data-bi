from c17_97_t_data_bi.utils.paths import make_dir_function
import pandas as pd

def main():
    raw_data_dir = make_dir_function(["data", "raw"])
    data = {}
    data['customer_df'] = pd.read_csv(raw_data_dir("olist_customers_dataset.csv"))
    data['geolocation_df'] = pd.read_csv(raw_data_dir("olist_geolocation_dataset.csv"))
    data['order_items_df'] = pd.read_csv(raw_data_dir("olist_order_items_dataset.csv"))
    data['order_payments_df'] = pd.read_csv(raw_data_dir("olist_order_payments_dataset.csv"))
    data['order_reviews_df'] = pd.read_csv(raw_data_dir("olist_order_reviews_dataset.csv"))
    data['orders_df'] = pd.read_csv(raw_data_dir("olist_orders_dataset.csv"))
    data['products_df'] = pd.read_csv(raw_data_dir("olist_products_dataset.csv"))
    data['sellers_df'] = pd.read_csv(raw_data_dir("olist_sellers_dataset.csv"))
    
    return data
    
if __name__ == "__main__":
    main()