# Directory structure:
# project_name/
#   |- app.py          # Main file to run the Streamlit app
#   |- pages/
#        |- page1.py   # Introduction & Data Description
#        |- page2.py   # Exploratory Data Analysis
#        |- page3.py   # Model Training & Evaluation
#        |- page4.py   # Predictions & Visualizations

# app.py
import streamlit as st
from streamlit_option_menu import option_menu
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
def main():

    
    st.set_page_config(page_title="PM2.5 Prediction App", layout="wide")

    # Add custom CSS
    add_custom_css()
    
    # Navigation menu
    with st.sidebar:
        selected = option_menu(
            "Main Menu",
            ["Introduction", "EDA", "Model Training", "Predictions"],
            icons=["house", "bar-chart", "cpu", "line-chart"],
            menu_icon="cast",
            default_index=0,
        )

    # Page selection
    if selected == "Introduction":
        import pages.page1 as page1
        page1.run()
    elif selected == "EDA":
        import pages.page2 as page2
        page2.run()
    elif selected == "Model Training":
        import pages.page3 as page3
        page3.run()
    elif selected == "Predictions":
        import pages.page4 as page4
        page4.run()

if __name__ == "__main__":
    main()

