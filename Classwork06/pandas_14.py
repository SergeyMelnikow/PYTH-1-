import pandas as pd
f = pd.read_csv("telecom_churn.csv")
Dm=f["Total day minutes"].sum()
Dc=f["Total day calls"].sum()
Em=f["Total eve minutes"].sum()
Ec=f["Total eve calls"].sum()
Nm=f["Total night minutes"].sum()
Nc=f["Total night calls"].sum()
df = pd.DataFrame({"День": [Dm,Dc,Dm/Dc], "Вечер": [Em, Ec, Em/Ec], "Ночь": [Nm, Nc, Nm/Nc]}, index = ["число минут", "число звонков", "среднее время звонка"])
print(df)