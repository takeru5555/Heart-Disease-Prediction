import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# %matplotlib inline
sns.set_style("whitegrid")
plt.style.use("fivethirtyeight")

df = pd.read_csv("heart.csv")
# print(df.head())

pd.set_option("display.float", "{:.2f}".format)
df.describe()