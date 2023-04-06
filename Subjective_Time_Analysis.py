import pandas as pd
from scipy import stats

df = pd.read_excel('SubjectiveData.xlsx')
pd_summary = df[["Normal Cursor", "Bubble Cursor"]].describe()
print(pd_summary)

result = stats.wilcoxon(df["Normal Cursor"], df["Bubble Cursor"])
print(result)