import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import classification_report, accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
import numpy as np

def set_black_background_and_sidebar():
    st.markdown(
        """
        <style>
        /* General background styling for the app */
        .stApp {
            background-color: black;
            color: white;
        }

        /* Sidebar styling */
        .css-1v3fvcr {
            background-color: black !important; /* Black background */
        }
        .css-1v3fvcr, .css-1v3fvcr div, .css-1v3fvcr div span, .css-1v3fvcr div label {
            color: black !important; 
        }

        /* Change the background color of the sidebar */
        .sidebar .sidebar-content {
            background-color: #31333F;
        }
        /* Change the text color of the sidebar */
        .sidebar .sidebar-content {
            color: blue;
        }

        [data-testid="stSidebarContent"] { color: white; background-color: black; }
        [data-testid="stHeader"] { color: white; background-color: black; }
        /* Button and interactive elements styling */
        .stButton > button {
            background-color: #333333; /* Dark gray buttons */
            color: white; /* White text */
        }

        /* Styling headers and text elements globally */
        h1, h2, h3, h4, h5, h6, p, div, span, label {
            color: white;
        }

        /* Styling dataframes */
        .st-dataframe {
            background-color: #222222;
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


# Set page configuration
st.set_page_config(page_title="Beijing Air Quality Analysis", layout="wide")

def main():
    # Apply custom CSS
    set_black_background_and_sidebar()

    # Sidebar navigation
    st.sidebar.title("Navigation")
    options = [
        "Home",
        "Data Overview",
        "Exploratory Data Analysis",
        "Modeling and Prediction",
        "About the Project"
    ]
    choice = st.sidebar.radio("Go to", options)

    # Sample DataFrame for demonstration
    df = pd.DataFrame({
        'Station': ['A', 'B', 'C', 'D'],
        'PM2.5': [50, 80, 120, 30],
        'AQI': [80, 100, 150, 40],
        'Status': ['Good', 'Moderate', 'Unhealthy', 'Good']
    })

    if choice == "Home":
        st.title("Welcome to Beijing Air Quality Analysis")
        st.markdown("---")
        st.write(
            "This application allows you to explore, analyze, and model air quality data from Beijing. "
            "Use the navigation panel on the left to switch between sections."
        )
        st.image("https://images.unsplash.com/photo-1643902433280-8f8807b7f743?w=600&auto=format&fit=crop&q=60", use_container_width=True)

    elif choice == "Data Overview":
        st.title("Data Overview")
        st.markdown("---")
        st.write("### Dataset Summary")
        st.write(df.describe())

        st.write("### Sample Data")
        st.dataframe(df)

    elif choice == "Exploratory Data Analysis":
        st.title("Exploratory Data Analysis")
        st.markdown("---")

        st.write("### PM2.5 Levels Distribution")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.barplot(x='Station', y='PM2.5', data=df, ax=ax)
        ax.set_title("PM2.5 Levels by Station")
        st.pyplot(fig)

    elif choice == "Modeling and Prediction":
        st.title("Modeling and Prediction")
        st.markdown("---")

        st.write("### Sample Modeling Section")
        st.write("This section can be used to train and evaluate machine learning models.")

    elif choice == "About the Project":
        st.title("About the Project")
        st.markdown("---")
        st.write(
            "This project leverages the Beijing Multi-Site Air Quality dataset to analyze pollution trends, "
            "build machine learning models for prediction, and provide an interactive platform for exploration."
        )
        st.image("https://images.unsplash.com/photo-1611273426858-450d8e3c9fce?w=600&auto=format&fit=crop&q=60", use_container_width=True)

if __name__ == "__main__":
    main()
