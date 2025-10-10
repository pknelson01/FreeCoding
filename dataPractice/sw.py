import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

y = pd.read_csv("sw.csv", index_col=0)
y.to_excel("sw.xlsx", index=True)

x = pd.read_csv("ratings.csv", index_col=0)
x["Year"] = x["Year"].astype(str) 
x.to_excel("watchedList.xlsx", index=True)

print("Updated.")