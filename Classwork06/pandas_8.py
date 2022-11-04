import pandas as pd
f = pd.read_csv("telecom_churn.csv")
df=f[["State","Total day calls","Total eve calls"]]
df=df.groupby(['State']).mean()
df["Д>В"]=df["Total day calls"]>df["Total eve calls"]
print(df)