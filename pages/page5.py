import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split

# Function to train the model and return the trained model and feature columns
def train_model():
    df = pd.read_csv("PRSA_Data_Aotizhongxin_20130301-20170228.csv")

    feature_cols = ["PM10", "SO2", "NO2", "CO", "O3", "TEMP", "PRES", "RAIN", "WSPM"]
    target_col = "PM2.5"

    X = df[feature_cols]
    y = df[target_col]
    X = X.fillna(X.mean())
    y = y.fillna(y.mean())

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    model = GradientBoostingRegressor()
    model.fit(X_train, y_train)

    return model, feature_cols

# Main function to run the Streamlit page
def run():
    st.title("Interactive Prediction Tool")

    # Train the model (only once using caching to avoid re-training each time)
    @st.cache_data
    def get_trained_model():
        return train_model()

    model, feature_cols = get_trained_model()

    # User Inputs
    st.markdown("### Enter Feature Values")
    user_input = {}
    for feature in feature_cols:
        user_input[feature] = st.number_input(f"Enter {feature} value:", value=0.0)

    # Prediction Button
    if st.button("Predict PM2.5 Concentration"):
        user_data = np.array([list(user_input.values())])
        prediction = model.predict(user_data)
        st.write(f"**Predicted PM2.5 Concentration:** {prediction[0]:.2f}")

if __name__ == "__main__":
    run()
