import pandas as pd

# Load the dataset
file_path = r"E:\Air Pollution Dashboard\data\air_pollution_data.csv" 
df = pd.read_csv(file_path)
print(df.columns)

# Display basic info
print("Dataset Overview:")
print(df.info())
print("\nFirst 5 rows:")
print(df.head())

# Convert date column to datetime format
# df['date'] = pd.to_datetime(df['date'])

# Handle missing values
df.fillna(method='ffill', inplace=True)  # Forward fill missing data

# Rename columns for consistency
df.rename(columns=lambda x: x.strip().lower().replace(" ", "_"), inplace=True)

# Save cleaned data
cleaned_file_path = r"E:\Air Pollution Dashboard\data\cleaned_air_pollution_data.csv"
df.to_csv(cleaned_file_path, index=False)

print(f"Cleaned dataset saved to {cleaned_file_path}")
