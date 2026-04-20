import requests
import pandas as pd
from datetime import datetime

API_KEY = "50eac6a47d10831cbe3fb32d5abae06f"

lat = 26.4499   # Ajmer
lon = 74.6399

# time range (last 2 days example)
start = int(datetime(2024, 4, 1).timestamp())
end = int(datetime(2024, 4, 3).timestamp())

url = f"http://api.openweathermap.org/data/2.5/air_pollution/history?lat={lat}&lon={lon}&start={start}&end={end}&appid={API_KEY}"

response = requests.get(url)
data = response.json()

records = []

for item in data['list']:
    records.append({
        "datetime": datetime.fromtimestamp(item['dt']),
        "AQI": item['main']['aqi'],
        "PM2.5": item['components']['pm2_5'],
        "PM10": item['components']['pm10'],
        "CO": item['components']['co'],
        "NO2": item['components']['no2'],
        "O3": item['components']['o3']
    })

df = pd.DataFrame(records)

df.to_csv("aqi_history.csv", index=False)

print("Dataset created with", len(df), "rows")
