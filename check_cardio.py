import pandas as pd

df = pd.read_csv("cardio_data.csv")
print(df["Cardio_Label"].value_counts())