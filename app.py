import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load("bike_demand_model.pkl")

# Page config
st.set_page_config(page_title="🚴 Bike Demand Predictor", layout="wide")

# Sidebar - Input parameters
st.sidebar.header("Input Parameters")

season = st.sidebar.selectbox("Season", ["Spring", "Summer", "Fall", "Winter"])
holiday = st.sidebar.selectbox("Holiday", ["No", "Yes"])
workingday = st.sidebar.selectbox("Working Day", ["No", "Yes"])
weather = st.sidebar.selectbox("Weather", [
    "Clear / Few Clouds",
    "Mist / Cloudy",
    "Light Snow / Rain",
    "Heavy Rain / Snow"
])
temp = st.sidebar.number_input("Temperature (°C)", 0.0, 50.0, 20.0)
atemp = st.sidebar.number_input("Feels Like Temp (°C)", 0.0, 50.0, 20.0)
humidity = st.sidebar.number_input("Humidity (%)", 0, 100, 50)
windspeed = st.sidebar.number_input("Wind Speed", 0.0, 100.0, 10.0)
year = st.sidebar.selectbox("Year", [2011, 2012])
month = st.sidebar.slider("Month", 1, 12, 6)
day = st.sidebar.slider("Day", 1, 31, 15)
dayofweek = st.sidebar.selectbox("Day of Week", [
    "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
])
hour = st.sidebar.slider("Hour of Day", 0, 23, 12)

# Mapping categorical inputs to numeric values
season_map = {"Spring": 1, "Summer": 2, "Fall": 3, "Winter": 4}
holiday_map = {"No": 0, "Yes": 1}
workingday_map = {"No": 0, "Yes": 1}
weather_map = {
    "Clear / Few Clouds": 1,
    "Mist / Cloudy": 2,
    "Light Snow / Rain": 3,
    "Heavy Rain / Snow": 4
}
dayofweek_map = {
    "Monday": 0, "Tuesday": 1, "Wednesday": 2,
    "Thursday": 3, "Friday": 4, "Saturday": 5, "Sunday": 6
}

# Prepare the feature vector
features = np.array([[
    season_map[season],
    holiday_map[holiday],
    workingday_map[workingday],
    weather_map[weather],
    temp,
    atemp,
    humidity,
    windspeed,
    year,
    month,
    day,
    dayofweek_map[dayofweek],
    hour
]])

# Main panel
st.title("🚴 Bike Sharing Demand Predictor")
st.markdown("Predict daily bike rental counts based on weather and seasonal conditions.")

if st.button("Predict Demand"):
    prediction = model.predict(features)[0]
    st.success(f"Predicted Bike Demand: **{int(prediction)} rentals**")

# Hide Streamlit's default menu, footer, and GitHub/star links
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

