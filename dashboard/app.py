import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("data/cleaned_air_pollution_data.csv")

# Streamlit app layout
st.title("🌍 Air Pollution Dashboard")

# Dropdown to select a city
city = st.selectbox("Select a city:", df["city"].unique())

# Filter data for the selected city
city_data = df[df["city"] == city]

# Display data summary
st.write(f"### Pollution Data for {city}")
st.dataframe(city_data)

# Pollution Level Trends
st.write(f"## AQI Trends in {city}")

fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(data=city_data, y="pm2.5_aqi_value", x=city_data.index, label="PM2.5 AQI", color="red")
sns.lineplot(data=city_data, y="no2_aqi_value", x=city_data.index, label="NO2 AQI", color="blue")
sns.lineplot(data=city_data, y="co_aqi_value", x=city_data.index, label="CO AQI", color="green")
sns.lineplot(data=city_data, y="ozone_aqi_value", x=city_data.index, label="Ozone AQI", color="purple")

ax.set_xlabel("Index")
ax.set_ylabel("AQI Value")
ax.set_title(f"AQI Levels in {city}")
ax.legend()

# Display the plot in Streamlit
st.pyplot(fig)

# Show AQI category distribution
st.write("### AQI Category Distribution")

fig, ax = plt.subplots(figsize=(8, 4))
sns.countplot(x="aqi_category", data=city_data, palette="viridis", order=city_data["aqi_category"].value_counts().index)
ax.set_title(f"AQI Categories in {city}")
ax.set_xlabel("AQI Category")
ax.set_ylabel("Count")
plt.xticks(rotation=45)

st.pyplot(fig)

# Footer
st.write("📊 Data powered by Air Pollution Monitoring")

