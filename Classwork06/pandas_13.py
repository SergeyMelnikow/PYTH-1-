import pandas as pd
f = pd.read_csv("telecom_churn.csv")
print(f["Total intl minutes"].sum()/f["Total intl calls"].sum())