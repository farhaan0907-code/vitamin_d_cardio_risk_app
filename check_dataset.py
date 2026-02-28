import pandas as pd

df = pd.read_csv("vitamin_d_data.csv")

print("First 5 rows:")
print(df.head())

print("\nClass Distribution:")
print(df["VitD_Label"].value_counts())