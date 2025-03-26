import requests

CHANNEL_ID = 2892539

url = f"https://api.thingspeak.com/channels/{CHANNEL_ID}/feeds/last.json"
response = requests.get(url)

if response.ok:
    data = response.json()
    print("Latest Sensor Data:")
    print(f"Temperature: {data['field1']} °C")
    print(f"Humidity: {data['field2']} %")
    print(f"CO₂: {data['field3']} ppm")
else:
    print("Failed to retrieve data")
