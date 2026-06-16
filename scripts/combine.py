import pandas as pd

df_2019 = pd.read_csv("data/Divvy_Trips_2019_Q1.csv")
df_2020 = pd.read_csv("data/Divvy_Trips_2020_Q1.csv")

df_2019 = df_2019.rename(columns={
    "trip_id": "ride_id",
    "start_time": "started_at",
    "end_time": "ended_at",
    "from_station_id": "start_station_id",
    "from_station_name": "start_station_name",
    "to_station_id": "end_station_id",
    "to_station_name": "end_station_name",
    "usertype": "member_casual"
})

df_2019["member_casual"] = df_2019["member_casual"].replace({
    "Subscriber": "member",
    "Customer": "casual"
})

common_cols = ["ride_id", "started_at", "ended_at", "start_station_id",
                "start_station_name", "end_station_id", "end_station_name",
                "member_casual"]

df_2019_trimmed = df_2019[common_cols]
df_2020_trimmed = df_2020[common_cols]

combined = pd.concat([df_2019_trimmed, df_2020_trimmed], ignore_index=True)

combined["started_at"] = pd.to_datetime(combined["started_at"])
combined["ended_at"] = pd.to_datetime(combined["ended_at"])

combined["ride_length"] = (combined["ended_at"] - combined["started_at"]).dt.total_seconds() / 60
combined["day_of_week"] = combined["started_at"].dt.day_name()

print("Combined shape before cleaning:", combined.shape)

combined = combined[(combined["ride_length"] > 0) & (combined["ride_length"] <= 1440)]

print("Combined shape after cleaning:", combined.shape)
print()

print("member_casual value counts:")
print(combined["member_casual"].value_counts())
print()

print("ride_length stats (cleaned):")
print(combined["ride_length"].describe())
print()

print("Average ride_length by member_casual:")
print(combined.groupby("member_casual")["ride_length"].mean())
print()

print("Ride count by member_casual and day_of_week:")
print(combined.groupby(["member_casual", "day_of_week"])["ride_id"].count())

combined.to_csv("outputs/combined_cleaned.csv", index=False)
print()
print("Saved to outputs/combined_cleaned.csv")
