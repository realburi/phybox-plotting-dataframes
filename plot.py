import pandas as pd
import matplotlib.pyplot as plt


#df = pd.DataFrame.from_csv('phybox.csv', parse_dates=False)
df = pd.read_csv('/Users/otgonjargal/Desktop/phybox.csv')


df = df.cumsum()

#print(df)
df.plot()
plt.show()
