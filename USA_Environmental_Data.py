import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel('C:/Users/sammy/Dropbox/Philadelphia Academies Inc/Environmental Jobs Projections Feb 2018/USA_ENV.xlsx')

df_grouped = df.groupby('Degree_Required')[['Base', 'Proj', 'Change', 'Median_2016_Salary']].agg({'Base':'sum', 'Proj':'sum', 'Change':'sum', 'Median_2016_Salary':'median'})

df_grouped['Percent Change'] = ((df_grouped.Proj - df_grouped.Base) / df_grouped.Base) * 100

df_grouped = df_grouped.sort_values('Median_2016_Salary', ascending=False)

# I want to plot a bar chart of salaries by degree requirement
# x_labels = degrees
# y_label = Salaries

x_label = list(df_grouped.index.str[0:9])
# x_label_abbv = ['Doctoral', 'Bachelors', 'Associates', 'High School', 'Dropout']
values = list(df_grouped['Median_2016_Salary'])
ax = sns.barplot(x_label, values)
ax.set(ylabel='Salary')
plt.show()



