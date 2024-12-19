# Beijing Air Quality Analysis and Prediction

## 🌟 Overview
This project focuses on analyzing and predicting air quality in Beijing using machine learning models and exploratory data analysis (EDA). The dataset contains hourly air pollution data from 12 monitoring sites in Beijing, covering the period from March 1, 2013, to February 28, 2017.

Key features of this project include:
- Exploratory Data Analysis (EDA)
- Handling missing values and data preprocessing
- Building machine learning models for prediction
- Interactive Streamlit application for data visualization and model interaction

---

## 📂 Project Structure
├── app.py # Main Streamlit application 
├── pages/ │ 
  ├── page1.py # Introduction page │ 
  ├── page2.py # EDA visualizations │ 
  ├── page3.py # Modeling and prediction │ 
  ├── page4.py # Project details 
├── data/ │ 
  ├── PRSA_Data_Aotizhongxin_20130301-20170228.csv │ 
  ├── PRSA_Data_Changping_20130301-20170228.csv │ 
  ├── ... # Other datasets 
├── README.md # Project documentation 
├── requirements.txt # Python dependencies


---

## 📊 Dataset Details
- **Source**: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Beijing+PM2.5+Data)
- **Time Period**: March 1, 2013, to February 28, 2017
- **Features**:
  - **Air Quality Parameters**: PM2.5, PM10, SO2, NO2, CO, O3
  - **Meteorological Data**: Temperature, Pressure, Dew Point, Rainfall, Wind Speed, Wind Direction
- **Sites**: Data from 12 monitoring stations in Beijing

---

## 🚀 How to Run the Project
1. Clone this repository:
   ```bash
   git clone https://github.com/Peiris94-dev/Beijing-Multi-Site-Air-Quality-Analysis.git
   cd Beijing-Multi-Site-Air-Quality-Analysis
