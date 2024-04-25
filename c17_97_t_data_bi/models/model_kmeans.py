from c17_97_t_data_bi.utils.paths import make_dir_function
import pandas as pd
import numpy as np
from scipy import stats
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import warnings
warnings.filterwarnings("ignore")

raw_data_dir = make_dir_function(["data", "processed"])
olist_df = pd.read_csv(raw_data_dir("olist_df.csv"))

def RFMTechnique():
    # R
    # Group the DataFrame by the customer's unique identifier and find the most recent purchase date for each customer using the max() function on the 'order_purchase_timestamp' column.
    recency = olist_df.groupby(by='customer_unique_id', as_index=False)['order_purchase_timestamp'].max()
    # Renamed 'order purchase timestamp' for clarity
    recency.rename(columns={"order_purchase_timestamp":"last_purchase_date"}, inplace=True)
    # Converted to dt.date format
    recency["last_purchase_date"] = pd.to_datetime(recency["last_purchase_date"])
    # Recency is calculated by subtracting each customer's most recent purchase date from the overall most recent purchase date
    recent_date = pd.to_datetime(olist_df['order_purchase_timestamp']).max()
    recency['Recency'] = recency['last_purchase_date'].apply(lambda x: (recent_date - x).days)
    # F
    # Group the DataFrame by the unique customer identifier 'customer_unique_id' and count the number of unique values in the 'order_id' column for each customer, representing the frequency of purchases for each customer.
    frequency = olist_df.groupby(["customer_unique_id"]).agg({"order_id":"nunique"}).reset_index()
    frequency.rename(columns={"order_id":"Frequency"}, inplace=True)
    # M
    # Group the DataFrame by the customer's unique identifier 'customer_unique_id' and add the value of the 'payment_value' column for each customer, representing the total monetary value spent by each.
    monetary = olist_df.groupby('customer_unique_id', as_index=False)['payment_value'].sum()
    monetary.columns = ['customer_unique_id', 'Monetary']
    # Merge
    rf = recency.merge(frequency, on='customer_unique_id')
    rfm = rf.merge(monetary, on='customer_unique_id').drop(columns='last_purchase_date')
    return rfm

def replaceAndModifyBiases(rfm):
    # Remove zeros from data and replace with value 1 before logarithmic transformation
    rfm[rfm.columns[1:]] = rfm[rfm.columns[1:]].applymap(lambda x: 1 if x == 0 else x)

    def check_skew(df_skew, column):
        skew = stats.skew(df_skew[column])
        # A bias hypothesis test is performed to evaluate whether the distribution is significantly asymmetric.
        skewtest = stats.skewtest(df_skew[column])
        print("{}'s --> Skew: {}, : {}".format(column, skew, skewtest))
        return

    for col in rfm.columns[1:]:
        check_skew(rfm, col)

    # Apply the logarithmic function (logn)
    rfm_log = rfm.copy()
    # We only transform 'Frequency' and 'Monetary' since 'Recency' does not improve with the transformation
    for c in rfm.columns[2:]:
        rfm_log[c] = np.log10(rfm_log[c])
    
    print(" ")
    
    for col in rfm.columns[1:]:
        check_skew(rfm_log, col)
    
    return rfm, rfm_log

def scaleAndKmeans(rfm, rfm_log):
    # Initialize and adjust the scaler
    scaler = StandardScaler()
    # Fits scaler to transformed RFM data
    scaler.fit(rfm_log.drop("customer_unique_id", axis=1))
    # Scale data
    RFM_table_scaled = scaler.transform(rfm_log.drop("customer_unique_id", axis=1))
    # Create a DataFrame with the scaled data (Excluding 'customer unique id')
    RFM_table_scaled = pd.DataFrame(RFM_table_scaled, columns=rfm_log.columns[1:])
    
    # Initialization of 'distortions' variables or better known as WCSS
    distortions = []
    # It's tested with different K
    K = range(1,10)
    for k in K:
        # K-means model training
        kmeanModel = KMeans(n_clusters=k)
        kmeanModel.fit(RFM_table_scaled)
        distortions.append(kmeanModel.inertia_)

    # Elbow Method Chart
    plt.figure(figsize=(9,8))
    plt.plot(K, distortions, 'g*-')
    plt.xlabel('k Values')
    plt.ylabel('WCSS')
    plt.title('The Elbow Method showing the optimal k')
    plt.show()

    # Train the model on 4 clusters
    kmean_model = KMeans(n_clusters=4, random_state=5)
    kmean_y = kmean_model.fit_predict(RFM_table_scaled)
    # Add the labels to the Dataframe
    rfm['Cluster'] = kmean_model.labels_

    # Function to display the average and count using the agg() method to use different functions
    def rfm_values(df):
        df_new = df.groupby(['Cluster']).agg({
                'Recency': 'mean',
                'Frequency': 'mean',
                'Monetary': ['mean', 'count']
            }).round(2)

        return df_new
    
    print(rfm_values(rfm))

def main():
    rfm, rfm_log = replaceAndModifyBiases(RFMTechnique())
    scaleAndKmeans(rfm, rfm_log)
  
if __name__ == "__main__":
    main()