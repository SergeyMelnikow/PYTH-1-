import pandas as pd
f = pd.read_csv("telecom_churn.csv")
df=f.groupby(['Churn']).agg({'Total day charge':'sum'})
print(df)
print("У оставшихся больше")