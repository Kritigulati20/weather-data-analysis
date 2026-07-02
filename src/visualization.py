import pandas as pd
import matplotlib.pyplot as plt

# Read dataset
weather_data = pd.read_csv("../data/weather.csv")

# Remove duplicates
weather_data = weather_data.drop_duplicates()

# Fill missing values
weather_data["Precip Type"] = weather_data["Precip Type"].fillna("Unknown")

plt.figure(figsize=(10,6))

plt.hist(weather_data["Temperature (C)"], bins=30)

plt.title("Distribution of Temperature")
plt.xlabel("Temperature (°C)")
plt.ylabel("Frequency")

plt.show()

# ====================================
# Temperature Line Graph
# ====================================

plt.figure(figsize=(12, 6))

plt.plot(weather_data["Temperature (C)"][:500])

plt.title("Temperature Variation (First 500 Records)")
plt.xlabel("Record Number")
plt.ylabel("Temperature (°C)")

plt.savefig("../graphs/temperature_line.png")
plt.show()
plt.close()

# ====================================
# Humidity vs Temperature Scatter Plot
# ====================================

plt.figure(figsize=(8, 6))

plt.scatter(
    weather_data["Humidity"],
    weather_data["Temperature (C)"],
    alpha=0.3
)

plt.title("Humidity vs Temperature")
plt.xlabel("Humidity")
plt.ylabel("Temperature (°C)")

plt.savefig("../graphs/humidity_vs_temperature.png")
plt.show()
plt.close()

# ====================================
# Average Temperature by Weather Type
# ====================================

average_temp = weather_data.groupby("Summary")["Temperature (C)"].mean()

plt.figure(figsize=(12, 6))

average_temp.head(10).plot(kind="bar")

plt.title("Average Temperature by Weather Type")
plt.xlabel("Weather Summary")
plt.ylabel("Average Temperature (°C)")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("../graphs/average_temperature_by_weather.png")
plt.show()
plt.close()