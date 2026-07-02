import pandas as pd
import numpy as np

from pathlib import Path
import pandas as pd
import numpy as np

# Get the project root folder
BASE_DIR = Path(__file__).resolve().parent.parent

# Build the full path to the dataset
weather_file = BASE_DIR / "data" / "weather.csv"

# Read the dataset
weather_data = pd.read_csv(weather_file)

# Display the first 5 rows
print("\n===== First 5 Rows =====")
print(weather_data.head())

# Display the last 5 rows
print("\n===== Last 5 Rows =====")
print(weather_data.tail())

# Display the shape (rows and columns)
print("\n===== Shape of Dataset =====")
print(weather_data.shape)

# Display column names
print("\n===== Column Names =====")
print(weather_data.columns)

# Display information about the dataset
print("\n===== Dataset Information =====")
weather_data.info()

# Display statistical summary
print("\n===== Statistical Summary =====")
print(weather_data.describe())

# ==============================
# Check for missing values
# ==============================
print("\n===== Missing Values =====")
print(weather_data.isnull().sum())

# ==============================
# Check for duplicate rows
# ==============================
print("\n===== Duplicate Rows =====")
print(weather_data.duplicated().sum())

# ====================================
# Remove duplicate rows
# ====================================

weather_data = weather_data.drop_duplicates()

# ====================================
# Replace missing values in Precip Type
# ====================================

weather_data["Precip Type"] = weather_data["Precip Type"].fillna("Unknown")

# ====================================
# Check again after cleaning
# ====================================

print("\n===== Missing Values After Cleaning =====")
print(weather_data.isnull().sum())

print("\n===== Duplicate Rows After Cleaning =====")
print(weather_data.duplicated().sum())

print("\n===== Shape After Cleaning =====")
print(weather_data.shape)

# ==============================
# Convert Temperature column to NumPy array
# ==============================

temperature = weather_data["Temperature (C)"].to_numpy()

print(type(temperature))

# Days with temperature greater than 30°C
hot_days = temperature[temperature > 30]

print("\n===== Hot Days =====")
print("Number of days above 30°C:", len(hot_days))

freezing_days = temperature[temperature < 0]

print("\n===== Freezing Days =====")
print("Number of freezing days:", len(freezing_days))

print("\n===== Hottest Temperature =====")
print(np.max(temperature))

print("\n===== Coldest Temperature =====")
print(np.min(temperature))

humidity = weather_data["Humidity"].to_numpy()

print("\n===== Average Humidity =====")
print(np.mean(humidity))

wind_speed = weather_data["Wind Speed (km/h)"].to_numpy()

print("\n===== Maximum Wind Speed =====")
print(np.max(wind_speed))

hottest_index = np.argmax(temperature)

print("\n===== Hottest Day =====")
print("Temperature:", temperature[hottest_index])
print("Date:", weather_data["Formatted Date"].iloc[hottest_index])

coldest_index = np.argmin(temperature)

print("\n===== Coldest Day =====")
print("Temperature:", temperature[coldest_index])
print("Date:", weather_data["Formatted Date"].iloc[coldest_index])