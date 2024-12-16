# pages/page1.py
import streamlit as st

def run():
    # Page Title
    st.title("Introduction")
    
    # Project Overview
    st.markdown(
        """
        ## 🌟 Project Overview
        This project aims to predict the **PM2.5 concentration** in Beijing from 2013 to 2017 using advanced machine learning techniques. 
        Understanding PM2.5 levels is crucial for environmental planning and improving air quality.
        """
    )
    
    # Dataset Information
    st.markdown(
        """
        ## 📊 Dataset Information
        - **Source**: Beijing Environmental Monitoring Center
        - **Time Period**: March 1, 2013, to February 28, 2017
        - **Features**: 
            - Air pollutant levels (PM2.5, PM10, SO2, NO2, CO, O3)
            - Meteorological data (Temperature, Pressure, Wind Speed, Rainfall)
        - **Sites**: Data from **12 monitoring stations** across Beijing.
        
        Missing values in the dataset are denoted as `NA` and have been handled appropriately during preprocessing.
        """
    )
    
    # Dataset Link
    st.markdown(
        """
        ### 📥 Download Dataset
        You can download the dataset used in this project [here](https://archive.ics.uci.edu/ml/datasets/Beijing+PM2.5+Data).
        """
    )

    # Key Objectives Section
    st.markdown(
        """
        ## 🎯 Key Objectives
        - Perform **exploratory data analysis (EDA)** to gain insights into PM2.5 trends and their correlation with other factors.
        - Build and evaluate **regression models** to predict PM2.5 concentrations.
        - Visualize results for better understanding and actionable insights.
        """
    )

    # Interactive Section: Why is PM2.5 Important?
    st.markdown("### 🤔 Why is PM2.5 Important?")
    if st.button("Learn More"):
        st.write(
            """
            PM2.5 particles are fine particulate matter with a diameter of less than 2.5 micrometers.
            - **Health Impact**: Can penetrate deep into the lungs and even enter the bloodstream, causing respiratory and cardiovascular issues.
            - **Environmental Impact**: Reduces visibility and contributes to haze.
            """
        )

    # Fun Fact Section
    st.markdown("### 🌍 Did You Know?")
    st.info(
        "PM2.5 particles are approximately 30 times smaller than the diameter of a human hair!"
    )

    # Sidebar Image
    st.image(
        "https://www.preventionweb.net/sites/default/files/styles/landscape_16_9/public/inline-images/image_to_show_air_pollution_caused_by_large_scale_fires_in_indonesia_-_gar_2022_ch11-b-5.jpg?itok=xvIS_pK5",
        caption="Smog in Beijing (Source: Wikimedia Commons)",
        use_container_width =True,
    )

    # Feedback Section
    st.markdown("## 📝 Feedback")
    st.text_area("Have suggestions? Share your feedback here:")

if __name__ == "__main__":
    run()
