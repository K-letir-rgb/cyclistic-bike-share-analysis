import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

combined = pd.read_csv("outputs/combined_cleaned.csv")

day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Chart 1: Average ride length by rider type
avg_length = combined.groupby("member_casual")["ride_length"].mean()

plt.figure(figsize=(6, 5))
avg_length.plot(kind="bar", color=["#1d9e75", "#378add"])
plt.title("Average Ride Length: Members vs Casual Riders")
plt.ylabel("Average Ride Length (minutes)")
plt.xlabel("Rider Type")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("outputs/avg_ride_length.png", dpi=150)
plt.close()
print("Saved avg_ride_length.png")

# Chart 2: Ride count by day of week, split by rider type
ride_counts = combined.groupby(["day_of_week", "member_casual"])["ride_id"].count().unstack()
ride_counts = ride_counts.reindex(day_order)

plt.figure(figsize=(9, 5))
ride_counts.plot(kind="bar", color=["#378add", "#1d9e75"])
plt.title("Ride Count by Day of Week: Members vs Casual Riders")
plt.ylabel("Number of Rides")
plt.xlabel("Day of Week")
plt.xticks(rotation=45)
plt.legend(title="Rider Type")
plt.tight_layout()
plt.savefig("outputs/rides_by_day.png", dpi=150)
plt.close()
print("Saved rides_by_day.png")
