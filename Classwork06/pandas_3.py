import pandas as pd
f = pd.read_csv("telecom_churn.csv")
print(f['Total day calls'].mean())