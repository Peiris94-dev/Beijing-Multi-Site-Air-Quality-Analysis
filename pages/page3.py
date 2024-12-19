# pages/page3.py
import streamlit as st
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def add_custom_css():
    # CSS for black background
    st.markdown(
        """
        <style>
        /* Set the background to black */
        body {
            background-color: black;
            color: white; /* Ensure text is visible on a black background */
        }

        /* Modify headers and links for better visibility */
        h1, h2, h3, h4, h5, h6 {
            color: #00FF00; /* Green text for headers */
        }

        a {
            color: #1E90FF; /* Blue text for links */
        }

        /* Info and button sections styling */
        .st-info {
            background-color: #333333; /* Dark gray background for info boxes */
            color: white;
        }

        button {
            background-color: #444444; /* Dark gray buttons */
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def run():
    # Add custom CSS
    add_custom_css()
    st.title("Model Training & Evaluation")
    st.markdown("### Gradient Boosting Regressor Model")

    # Load and preprocess data
    st.markdown("#### Dataset Overview")
    df = pd.read_csv("PRSA_Data_Aotizhongxin_20130301-20170228.csv")
    st.write(df.head())

    # Define features and target variable
    X = df[["PM10", "SO2", "NO2", "CO", "O3", "TEMP", "PRES", "RAIN", "WSPM"]]
    y = df["PM2.5"]

    # Handle missing values
    st.markdown("#### Handling Missing Values")
    X = X.fillna(X.mean())
    y = y.fillna(y.mean())
    st.write("Missing values filled with column mean.")

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    st.markdown("#### Training and Testing Split")
    st.write(f"Training Data: {X_train.shape[0]} samples")
    st.write(f"Testing Data: {X_test.shape[0]} samples")

    # Train model
    model = GradientBoostingRegressor()
    st.markdown("#### Model Training")
    model.fit(X_train, y_train)
    st.write("Gradient Boosting Regressor model trained successfully!")

    # Evaluate model
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)

    st.markdown("### Model Performance")
    st.write(f"**Mean Squared Error (MSE):** {mse:.2f}")
    st.write(f"**R-squared (R2):** {r2:.2f}")

    # Feature Importance Visualization
    st.markdown("### Feature Importance")
    feature_importance = model.feature_importances_
    feature_names = X.columns
    feature_df = pd.DataFrame({
        "Feature": feature_names,
        "Importance": feature_importance
    }).sort_values(by="Importance", ascending=False)

    st.write("#### Feature Importance Table")
    st.dataframe(feature_df)

    st.markdown("#### Feature Importance Bar Chart")
    plt.figure(figsize=(10, 6))
    plt.barh(feature_df["Feature"], feature_df["Importance"], color="skyblue")
    plt.title("Feature Importance", fontsize=16)
    plt.xlabel("Importance", fontsize=14)
    plt.ylabel("Feature", fontsize=14)
    plt.gca().invert_yaxis()
    st.pyplot(plt)

    # Predicted vs Actual Values
    st.markdown("### Predicted vs Actual Values")
    plt.figure(figsize=(10, 6))
    plt.scatter(y_test, predictions, alpha=0.6, color="purple")
    plt.plot(
        [y_test.min(), y_test.max()],
        [y_test.min(), y_test.max()],
        "r--",
        label="Perfect Prediction Line"
    )
    plt.title("Predicted vs Actual PM2.5 Concentration", fontsize=16)
    plt.xlabel("Actual PM2.5", fontsize=14)
    plt.ylabel("Predicted PM2.5", fontsize=14)
    plt.legend()
    st.pyplot(plt)

    # Residual Analysis
    st.markdown("### Residual Analysis")
    residuals = y_test - predictions
    st.markdown("#### Residual Scatter Plot")
    plt.figure(figsize=(10, 6))
    plt.scatter(range(len(residuals)), residuals, alpha=0.6, color="green")
    plt.axhline(0, color="red", linestyle="--", label="Zero Residual Line")
    plt.title("Residual Scatter Plot", fontsize=16)
    plt.xlabel("Sample Index", fontsize=14)
    plt.ylabel("Residual", fontsize=14)
    plt.legend()
    st.pyplot(plt)

    st.markdown("#### Residual Distribution")
    plt.figure(figsize=(10, 6))
    plt.hist(residuals, bins=30, color="orange", edgecolor="black", alpha=0.7)
    plt.title("Residual Distribution", fontsize=16)
    plt.xlabel("Residual Value", fontsize=14)
    plt.ylabel("Frequency", fontsize=14)
    st.pyplot(plt)

    st.markdown(
        """
        The Gradient Boosting Regressor performs well on this dataset. 
        Residuals appear normally distributed, and feature importance highlights the most influential variables.
        """
    )

if __name__ == "__main__":
    run()
