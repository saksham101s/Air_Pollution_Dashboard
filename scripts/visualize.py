import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the processed dataset
df = pd.read_csv(r"E:\Air Pollution Dashboard\data\cleaned_air_pollution_data.csv")


# Ensure 'date' column is in datetime format if available
if 'date' in df.columns:
    df['date'] = pd.to_datetime(df['date'])

# ==============================
# 1. AQI Category Distribution
# ==============================
plt.figure(figsize=(8, 5))
sns.countplot(x='aqi_category', data=df, palette="viridis", order=df['aqi_category'].value_counts().index)
plt.title("Overall AQI Category Distribution")
plt.xlabel("AQI Category")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()

# ==============================
# 2. AQI Trend Over Time
# ==============================
if 'date' in df.columns:
    plt.figure(figsize=(12, 6))
    sns.lineplot(x='date', y='aqi_value', data=df, hue='city', legend=False, alpha=0.6)
    plt.title("Air Quality Index Over Time")
    plt.xlabel("Date")
    plt.ylabel("AQI Value")
    plt.xticks(rotation=45)
    plt.show()

# ==============================
# 3. Correlation Heatmap
# ==============================
plt.figure(figsize=(10, 6))
aqi_features = ['pm2.5_aqi_value', 'co_aqi_value', 'ozone_aqi_value', 'no2_aqi_value', 'aqi_value']
corr_matrix = df[aqi_features].corr()

sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Matrix of Air Pollutants")
plt.show()

# ==============================
# 4. Compare AQI Across Cities
# ==============================
plt.figure(figsize=(12, 6))
sns.boxplot(x='city', y='aqi_value', data=df, palette="Set2")
plt.title("AQI Distribution Across Cities")
plt.xlabel("City")
plt.ylabel("AQI Value")
plt.xticks(rotation=90)
plt.show()
