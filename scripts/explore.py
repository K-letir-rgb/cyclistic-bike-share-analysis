import pandas as pd
df_2019 = pd.read_csv("data/Divvy_Trips_2019_Q1.csv")
df_2020 = pd.read_csv("data/Divvy_Trips_2020_Q1.csv")
print("2019 Q1 shape:", df_2019.shape)
print("2019 Q1 columns:", df_2019.columns.tolist())
print()
print("2020 Q1 shape:", df_2020.shape)
print("2020 Q1 columns:", df_2020.columns.tolist())
