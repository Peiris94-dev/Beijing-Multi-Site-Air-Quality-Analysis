# pages/page4.py
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

def run():
    st.title("Interactive Prediction Tool")
  
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
