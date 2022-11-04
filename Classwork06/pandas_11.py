import pandas as pd
f = pd.read_csv("telecom_churn.csv")
f["Number of clients"]=1
df = f.groupby("Customer service calls").agg({"Number of clients": "count"})
print(df)