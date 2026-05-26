import pandas as pd

# =========================
# NETWORK
# =========================

network_df = pd.read_csv("data/network.csv")

# Ambil kolom aman saja
network_dashboard = network_df[[
    "category",
    "vendorName",
    "statusStr"
]]

# Simpan
network_dashboard.to_csv(
    "data/dashboard_network.csv",
    index=False
)

print("dashboard_network.csv selesai")


# =========================
# ALARM
# =========================

alarm_df = pd.read_csv("data/alarm.csv")

print(alarm_df.columns)

# Ambil kolom aman
alarm_dashboard = alarm_df[[
    "severityString",
    "category",
    "entity"
]]

# Simpan
alarm_dashboard.to_csv(
    "data/dashboard_alarm.csv",
    index=False
)

print("dashboard_alarm.csv selesai")


# =========================
# AVAILABILITY
# =========================

availability_df = pd.read_csv("data/availability.csv")

# Ambil kolom aman
availability_dashboard = availability_df[[
    "Period",
    "Availability"
]]

# Simpan
availability_dashboard.to_csv(
    "data/dashboard_availability.csv",
    index=False
)

print("dashboard_availability.csv selesai")