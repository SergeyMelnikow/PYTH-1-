import pandas as pd
f = pd.read_csv("telecom_churn.csv")
df=f.groupby(['State']).agg({"Total day calls":"mean"})
print(df)