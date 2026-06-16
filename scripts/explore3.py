import pandas as pd
df_2019 = pd.read_csv("data/Divvy_Trips_2019_Q1.csv")
df_2020 = pd.read_csv("data/Divvy_Trips_2020_Q1.csv")
print("2019 sample row:")
print(df_2019.iloc[0])
print()
print("2020 sample row:")
print(df_2020.iloc[0])
