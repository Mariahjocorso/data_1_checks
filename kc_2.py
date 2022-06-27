import matplotlib.pyplot as plt
import pandas as pd
import numpy as num
import seaborn as sns


df = pd.read_csv(
    'assets\Sample-Data-Plant-Growth.csv')
df.head()
print(df)

sns.scatterplot(x=df['Weight'],
                y=df['Group'])
plt.show()
