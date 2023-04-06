import pandas as pd
from statsmodels.stats.anova import AnovaRM
import pingouin as pg
import researchpy
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)  # display all columns

df = pd.read_excel('ExperimentData.xlsx')

pd_summary = researchpy.summary_cont(df.groupby(['CursorType'])['Error']).round(2).reset_index()
print(pd_summary)

res = AnovaRM(data=df, depvar='Error', subject='Participant', within=['CursorType', 'TargetWidth', 'TargetDistance', 'DistractorNumber'], aggregate_func='mean')
print(res.fit())

res = AnovaRM(data=df, depvar='Error', subject='Participant', within=['CursorType', 'TargetWidth', 'TargetDistance', 'DistractorNumber'], aggregate_func='mean')
print(res.fit())

sns.set()
ax = sns.pointplot(data=df, x='CursorType', y='Error', hue='TargetWidth', dodge=True,
                   capsize=.1, errwidth=1, palette='colorblind')
plt.show()

sns.set()
ax = sns.pointplot(data=df, x='CursorType', y='Error', hue='TargetDistance', dodge=True,
                   capsize=.1, errwidth=1, palette='colorblind')
plt.show()