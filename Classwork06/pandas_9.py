import pandas as pd
f = pd.read_csv("telecom_churn.csv")
f[(f['International plan']=='Yes') & (f['Voice mail plan']=='Yes')]=1
f[(f['International plan']!=1) | (f['Voice mail plan']!=1)]=0
print(f.mean()[1])