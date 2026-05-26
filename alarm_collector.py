import requests
import urllib3
import pandas as pd

urllib3.disable_warnings()

# =========================
# CONFIG
# =========================

API_KEY = "429c705b60a03b2c5aabb4cf9c0c4eac"
BASE_URL = "https://10.1.100.26:8061"

# =========================
# API URL
# =========================

url = f"{BASE_URL}/api/json/alarm/listAlarms?apiKey={API_KEY}"

print("Request URL:")
print(url)

# =========================
# REQUEST
# =========================

response = requests.get(url, verify=False)

print("Status Code:", response.status_code)

# =========================
# RESPONSE
# =========================

data = response.json()

# Jika API mengembalikan error
if isinstance(data, dict) and "error" in data:

    print("API ERROR:")
    print(data["error"])

else:

    # Convert ke DataFrame
    df = pd.DataFrame(data)

    # Export CSV
    df.to_csv("data/alarm.csv", index=False)

    print("Berhasil export data/alarm.csv")