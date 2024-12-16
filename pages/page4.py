# pages/page4.py
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

def run():
    st.title("Predictions & Visualizations")

    # Load dataset
    st.markdown("### Dataset Overview")
    df = pd.read_csv("PRSA_Data_Aotizhongxin_20130301-20170228.csv")
    st.write(df.head())

    # Preprocess data
    st.markdown("### Select Features for Prediction")
    feature_cols = ["PM10", "SO2", "NO2", "CO", "O3", "TEMP", "PRES", "RAIN", "WSPM"]
    target_col = "PM2.5"

    X = df[feature_cols]
    y = df[target_col]
    X = X.fillna(X.mean())
    y = y.fillna(y.mean())

    # Split data into train-test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    # Train model
    model = GradientBoostingRegressor()
    model.fit(X_train, y_train)

    # Predictions
    st.markdown("### Make Predictions")
    predictions = model.predict(X_test)

    # Display example predictions
    st.write("#### Example Predictions (First 10)")
    results_df = pd.DataFrame({
        "Actual": y_test[:10].values,
        "Predicted": predictions[:10]
    }).reset_index(drop=True)
    st.dataframe(results_df)

    # Prediction Metrics
    st.markdown("### Prediction Performance")
    mse = mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)
    st.write(f"**Mean Squared Error (MSE):** {mse:.2f}")
    st.write(f"**R-squared (R2):** {r2:.2f}")

    # Visualization: Actual vs Predicted
    st.markdown("### Visualization: Actual vs Predicted")
    plt.figure(figsize=(10, 6))
    plt.scatter(y_test, predictions, alpha=0.6, color="blue", label="Predicted vs Actual")
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], "r--", label="Perfect Prediction")
    plt.title("Actual vs Predicted PM2.5 Concentration", fontsize=16)
    plt.xlabel("Actual PM2.5", fontsize=14)
    plt.ylabel("Predicted PM2.5", fontsize=14)
    plt.legend()
    st.pyplot(plt)

    # Visualization: Error Distribution
    st.markdown("### Visualization: Error Distribution")
    residuals = y_test - predictions
    plt.figure(figsize=(10, 6))
    plt.hist(residuals, bins=30, color="purple", edgecolor="black", alpha=0.7)
    plt.axvline(0, color="red", linestyle="--", label="Zero Error Line")
    plt.title("Residual Distribution", fontsize=16)
    plt.xlabel("Residual Value (Actual - Predicted)", fontsize=14)
    plt.ylabel("Frequency", fontsize=14)
    plt.legend()
    st.pyplot(plt)

    # Interactive Prediction Input
    st.markdown("### Interactive Prediction Tool")
    user_input = {}
    for feature in feature_cols:
        user_input[feature] = st.number_input(f"Enter {feature} value:", value=float(X[feature].mean()))

    # Predict for user input
    if st.button("Predict PM2.5 Concentration"):
        user_data = np.array([list(user_input.values())])
        user_prediction = model.predict(user_data)
        st.write(f"**Predicted PM2.5 Concentration:** {user_prediction[0]:.2f}")

if __name__ == "__main__":
    run()