import requests
import urllib3
import pandas as pd
import time

urllib3.disable_warnings()

API_KEY = "429c705b60a03b2c5aabb4cf9c0c4eac"
BASE_URL = "https://10.1.100.26:8061"

# Ambil semua device
device_url = f"{BASE_URL}/api/json/device/listDevices?apiKey={API_KEY}"

response = requests.get(device_url, verify=False)

devices = response.json()

availability_data = []

# Loop semua device
for device in devices:

    device_name = device.get("displayName")

    try:

        avail_url = (
            f"{BASE_URL}/api/json/device/getAvailabilityGraphData"
            f"?apiKey={API_KEY}"
            f"&isFluidic=true"
            f"&name={device_name}"
        )

        avail_response = requests.get(avail_url, verify=False)

        avail_json = avail_response.json()

        uptime_data = avail_json.get("uptimeData", [])

        # Jika dictionary
        if isinstance(uptime_data, dict):

            for period, availability in uptime_data.items():

                availability_data.append({
                    "Device": device_name,
                    "Period": period,
                    "Availability": availability
                })

        # Jika list
        elif isinstance(uptime_data, list):

            for item in uptime_data:

                if isinstance(item, dict):

                    availability_data.append({
                        "Device": device_name,
                        "Period": item.get("name"),
                        "Availability": item.get("availability")
                    })

        print(f"Berhasil: {device_name}")

        time.sleep(0.5)

    except Exception as e:

        print(f"Gagal: {device_name} -> {e}")

# Convert ke DataFrame
df = pd.DataFrame(availability_data)

# Export CSV
df.to_csv("data/availability.csv", index=False)

print("Selesai export availability.csv")