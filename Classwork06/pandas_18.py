import pandas as pd
f = pd.read_csv("telecom_churn.csv")
print(f.loc[[100,102,104],["State","Churn"]])