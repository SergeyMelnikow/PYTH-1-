import pandas as pd
df=pd.DataFrame({'A':[1,3,6,8,9,4,3,5],'B':[1,5,7,7,9,1,3,5]})
df['C']=(df['A'])**2+(df['B'])**2
df['D']=df[['A','B','C']].apply(lambda x: x.mean(), axis=1 )
print(df)