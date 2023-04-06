import pandas as pd
from statsmodels.stats.anova import AnovaRM
import pingouin as pg
import researchpy

pd.set_option('display.max_columns', None)
df = pd.read_excel('ExperimentData.xlsx')
pd_summary = researchpy.summary_cont(df.groupby(['CursorType', 'Block'])['Time']).round(2).reset_index()
print(pd_summary)

print("\n")
print("----------NORMAL CURSOR----------")
print("\n")

df_rt = df[df['CursorType'] == 'NormalCursor']  # get the dataframe of Normal Cursor

res_rt = AnovaRM(data=df_rt, depvar='Time', subject='Participant', within=['Block'], aggregate_func='mean')
print(res_rt.fit())

post_hocs_rt = pg.pairwise_tests(dv='Time', within='Block', subject='Participant', padjust='bonf', data=df_rt)
print(post_hocs_rt)

print("\n")
print("----------BUBBLE CURSOR----------")
print("\n")
df_rt = df[df['CursorType'] == 'BubbleCursor']  # get the dataframe of Bubble Cursor

res_rt = AnovaRM(data=df_rt, depvar='Time', subject='Participant', within=['Block'], aggregate_func='mean')
print(res_rt.fit())

post_hocs_rt = pg.pairwise_tests(dv='Time', within='Block', subject='Participant', padjust='bonf', data=df_rt)
print(post_hocs_rt)