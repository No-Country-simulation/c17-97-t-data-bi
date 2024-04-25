import data_collection
import pandas as pd

data = data_collection.main()

customer_df = data['customer_df']
geolocation_df = data['geolocation_df']
order_items_df = data['order_items_df']
order_payments_df = data['order_payments_df']
order_reviews_df = data['order_reviews_df']
orders_df = data['orders_df']
products_df = data['products_df']
sellers_df = data['sellers_df']

# A list is created with the names of the variables
datasets = ["customer_df", "geolocation_df", "order_items_df", "order_payments_df",
        "order_reviews_df", "orders_df", "products_df", "sellers_df"]

def expDatasets():
    # A function is created to obtain the information of each dataset
    def getInfoDataset(df):
        return {
            "dataset": df.name,
            "n_rows": df.shape[0],
            "n_cols": df.shape[1],
            "null_amount": df.isnull().sum().sum(),
            "q_null_columns": df.isnull().sum(axis=0).gt(0).sum(),
            "null_columns": ", ".join(df.columns[df.isnull().sum(axis=0).gt(0)].tolist()),
        }

    # The information of each dataset is obtained and a list of dictionaries is created
    info_datasets = []
    for dataset in datasets:
        df = globals()[dataset]
        df.name = dataset
        info_datasets.append(getInfoDataset(df))

    # A DataFrame is created from the list of dictionaries
    df_info_datasets = pd.DataFrame(info_datasets)
    df_info_datasets.style.set_table_styles([{"selector": "th", "props": [("text-align", "center"), ("font-weight", "bold")]}])

    return df_info_datasets

def expColumns():
    # Define an empty list to store the table data
    table_data = []

    # Iterate through each dataset
    for dataset_name in datasets:
        data = eval(dataset_name)

        # Get column information for the current dataset
        for col in data.columns:
            # Count null values and calculate null percentage
            null_count = data[col].isnull().sum()
            null_perc = round((null_count / len(data)) * 100, 4)

            # Get data type and number of unique entries (categorical count)
            data_type = data[col].dtype
            categorical_count = data[col].nunique()

            # Append data for the current column to the table_data list
            table_data.append({
                "dataset_name": dataset_name,
                "columns_name": col,
                "nulls": null_count,
                "nulls_percentage": str(null_perc) + "%",
                "data_type": data_type,
                "total_categorical": categorical_count
            })

    # Create the pandas DataFrame from the table_data list
    df = pd.DataFrame(table_data)
    return df


def main():
    print(expDatasets())
    print(expColumns())
    

if __name__ == "__main__":
    main()