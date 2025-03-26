import requests
import datetime

CHANNEL_ID = 2892539
FIELD_NUMBER = 1


end_time = datetime.datetime.utcnow()
start_time = end_time - datetime.timedelta(hours=5)

url = f"https://api.thingspeak.com/channels/{CHANNEL_ID}/fields/{FIELD_NUMBER}.json"
params = {
    "start": start_time.isoformat(),
    "end": end_time.isoformat(),
    "timezone": "UTC"
}

response = requests.get(url, params=params)

if response.ok:
    feeds = response.json()["feeds"]
    print("Last 5 hours of temperature readings:")
    for entry in feeds:
        print(f"{entry['created_at']}: {entry['field1']} °C")
else:
    print("Failed to retrieve data")
