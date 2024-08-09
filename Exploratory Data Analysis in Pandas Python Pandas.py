# Exploratory Data Analysis in Pandas

# Identifying patterns within the data understanding the relationships between the features and looking at outliers that may
# exist within your data set during this process you are looking for patterns and all these things but you're also looking for
# mistakes and missing values that need to clean

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\Toffee\OneDrive\Documents\Data Analyst\Python Pandas Adventure\world_population.csv")
df

pd.set_option('display.float_format', lambda x: '%.2f' % x)
df.info()

df.describe()

df.isnull().sum()

df.nunique()

#Sorting on values

df.sort_values(by="World Population Percentage", ascending=False).head(10)

df.corr(numeric_only = True)

#Heatmap using Seaborn

sns.heatmap(df.corr(numeric_only = True), annot = True)

plt.rcParams['figure.figsize'] = (20,7)
plt.show()

df.groupby('Continent').mean(numeric_only=True).sort_values(by="2022 Population",ascending=False)

df[df['Continent'].str.contains('Oceania')]

print(plt.style.available)
plt.style.use('seaborn-v0_8-bright')
df2 = df.groupby('Continent')[['1970 Population',
       '1980 Population', '1990 Population', '2000 Population',
       '2010 Population', '2015 Population', '2020 Population',
       '2022 Population']].mean(numeric_only=True).sort_values(by="2022 Population",ascending=False)
df2 
#or shortcut
#df2 = df.groupby('Continent')[df.columns[5:13]].mean(numeric_only=True).sort_values(by="2022 Population",ascending=False)
#df2 

df.columns

df3 = df2.transpose()
df3

df3.plot(kind = 'line', title = 'World Population', xlabel = 'Population Year', ylabel = 'Growth Rate')

df.boxplot(figsize=(20,10))

df.select_dtypes(include='float')
