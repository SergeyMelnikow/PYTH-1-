import pandas as pd
f = pd.read_csv("telecom_churn.csv")
df=f.groupby("Area code").agg({"Total day charge":"mean"})
print(df)