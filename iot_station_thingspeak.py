import time
import random
import requests

API_KEY = "SEBSS77M57TKLXE1"
THING_ID = "station-001"

def generate_sensor_data():
    return {
        "temperature": round(random.uniform(-50, 50), 2),
        "humidity": round(random.uniform(0, 100), 2),
        "co2": random.randint(300, 2000)
    }

while True:
    data = generate_sensor_data()
    payload = {
        "api_key": API_KEY,
        "field1": data["temperature"],
        "field2": data["humidity"],
        "field3": data["co2"]
    }
    response = requests.post("https://api.thingspeak.com/update", data=payload)
    if response.status_code == 200:
        print(f"Published: {data}")
    else:
        print("Failed to publish:", response.status_code)
    time.sleep(15)
