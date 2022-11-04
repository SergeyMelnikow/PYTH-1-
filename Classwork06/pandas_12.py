import matplotlib.pyplot as plt
import pandas as pd
f = pd.read_csv("telecom_churn.csv")
df=f.groupby("Customer service calls").agg({"Churn":"mean"})
plt.plot(df)
plt.show()