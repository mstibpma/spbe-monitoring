import requests
import urllib3
import pandas as pd

urllib3.disable_warnings()

# URL API
url = "https://10.1.100.26:8061/api/json/device/listDevices?apiKey=429c705b60a03b2c5aabb4cf9c0c4eac"

# Request API
response = requests.get(url, verify=False)

# Convert JSON
data = response.json()

# Ambil data device
devices = data

# Convert ke DataFrame
df = pd.DataFrame(devices)

# Simpan ke CSV
df.to_csv("network.csv", index=False)

print("Berhasil export network.csv")