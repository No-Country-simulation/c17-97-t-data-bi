from c17_97_t_data_bi.utils.paths import make_dir_function
import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, mean_absolute_percentage_error
from xgboost import XGBRegressor
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
import warnings
warnings.filterwarnings("ignore")

raw_data_dir = make_dir_function(["data", "processed"])
raw_data_dir_model = make_dir_function(["models"])

def load_data():
    olist_df = pd.read_csv(raw_data_dir("olist_df.csv"))
    # Extraction of numerical values
    df_numeric = olist_df.select_dtypes(include=['int', 'float'])
    
    return df_numeric

def preprocess_data(df_numeric):
    # Data transformation and scaling
    X = df_numeric.drop(['payment_value'], axis=1)
    y = df_numeric['payment_value']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    return X_train_scaled, X_test_scaled, y_train, y_test

def neuralNetwork(X_train_scaled, X_test_scaled, y_train, y_test):
    model = Sequential()
    model.add(Dense(64, activation='relu', input_shape=(X_train_scaled.shape[1],)))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(1, activation='linear'))

    model.compile(optimizer=Adam(), loss='mean_squared_error')

    # Load the weights of the trained model
    model.load_weights(raw_data_dir_model("model_weights.h5"))

    # Make predictions with the loaded model
    predictions = model.predict(X_test_scaled).flatten()

    mse = mean_squared_error(y_test, predictions)
    mae = mean_absolute_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)
    mape = mean_absolute_percentage_error(y_test, predictions) * 100
    rmse = np.sqrt(mse)
    mpe = np.mean((y_test - predictions) / y_test) * 100

    print(f'MSE: {mse}')
    print(f'MAE: {mae}')
    print(f'R^2: {r2}')
    print(f'MAPE: {mape}%')
    print(f'RMSE: {rmse}')
    print(f'MPE: {mpe}%')

    return predictions

def xgboost(X_train_scaled, X_test_scaled, y_train, y_test):
    xgb_model = XGBRegressor()
    xgb_model.fit(X_train_scaled, y_train)
    xgb_predicciones = xgb_model.predict(X_test_scaled)

    mse_xgb = mean_squared_error(y_test, xgb_predicciones)
    mae_xgb = mean_absolute_error(y_test, xgb_predicciones)
    r2_xgb = r2_score(y_test, xgb_predicciones)

    print(f"MSE: {mse_xgb}")
    print(f"MAE: {mae_xgb}")
    print(f"R^2: {r2_xgb}")

    return xgb_predicciones

def linearRegression(X_train_scaled, X_test_scaled, y_train, y_test):
    lr_model = LinearRegression()
    lr_model.fit(X_train_scaled, y_train)
    lr_predicciones = lr_model.predict(X_test_scaled)

    mse_lr = mean_squared_error(y_test, lr_predicciones)
    mae_lr = mean_absolute_error(y_test, lr_predicciones)
    r2_lr = r2_score(y_test, lr_predicciones)

    print(f"MSE: {mse_lr}")
    print(f"MAE: {mae_lr}")
    print(f"R^2: {r2_lr}")

    return lr_predicciones

def randomForestRegressor(X_train_scaled, X_test_scaled, y_train, y_test):
    rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
    rf_model.fit(X_train_scaled, y_train)
    rf_predicciones = rf_model.predict(X_test_scaled)

    mse_rf = mean_squared_error(y_test, rf_predicciones)
    mae_rf = mean_absolute_error(y_test, rf_predicciones)
    r2_rf = r2_score(y_test, rf_predicciones)

    print(f"MSE: {mse_rf}")
    print(f"MAE: {mae_rf}")
    print(f"R^2: {r2_rf}")

    return rf_predicciones

def main():
    neuralNetwork(preprocess_data(load_data()))
    xgboost(preprocess_data(load_data()))
    linearRegression(preprocess_data(load_data()))
    randomForestRegressor(preprocess_data(load_data()))

if __name__ == "__main__":
    main()