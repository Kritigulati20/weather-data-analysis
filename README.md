# Weather Data Analysis using Python, NumPy, Pandas and Matplotlib

## Project Overview
This project analyzes a historical weather dataset using Python. It performs data cleaning, statistical analysis using NumPy, and creates visualizations using Matplotlib.

## Features
- Load weather dataset from CSV
- Clean missing values
- Remove duplicate records
- Calculate average, minimum and maximum temperature
- Find hottest and coldest day
- Calculate average humidity
- Calculate maximum wind speed
- Count hot days and freezing days
- Generate multiple graphs

## Technologies Used
- Python
- NumPy
- Pandas
- Matplotlib

## Dataset
Historical Weather Dataset (96,453 records)

## Graphs Generated
- Temperature Histogram
- Temperature Line Graph
- Humidity vs Temperature Scatter Plot
- Average Temperature by Weather Type

## Project Structure

```
weatherdataanalysis/
│
├── data/
│   └── weather.csv
│
├── graphs/
│   ├── temperature_histogram.png
│   ├── temperature_line.png
│   ├── humidity_vs_temperature.png
│   └── average_temperature_by_weather.png
│
├── src/
│   ├── analysis.py
│   └── visualization.py
│
├── main.py
├── README.md
└── requirements.txt
```

## How to Run

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the analysis:

```bash
python main.py
```

Run the visualizations:

```bash
python src/visualization.py
```