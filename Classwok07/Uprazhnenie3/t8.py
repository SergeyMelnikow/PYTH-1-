import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

titanic = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv")
df=titanic
print(df['fare'].sum())