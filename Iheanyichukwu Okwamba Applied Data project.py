import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('school drop out dataset..csv')
pd.set_option('display.max_column', None)

df.rename(columns={"Marital status": "Marriage status"}, inplace=True)
df.rename(columns={'Application mode': "Mode of Application"}, inplace=True)
df.rename(columns={'Course': 'Course of study'}, inplace=True)
df.rename(columns={'Nacionality': 'Nationality'}, inplace=True)
df.rename(
    columns={'Mothers qualification': 'Qualification of Mother'}, inplace=True)
df.rename(
    columns={'Fathers qualification': 'Qualification of Father'}, inplace=True)
df.rename(columns={'Tuition fees up to date': 'Payment of fees'}, inplace=True)
df.rename(columns={'Unemployment rate': 'Rate of Unemployment'}, inplace=True)
df.rename(columns={'Inflation rate': 'Rate of Inflation'}, inplace=True)
df.rename(columns={'GDP': 'Gross Development Profit'}, inplace=True)
df.rename(columns={'Target': 'Result'}, inplace=True)

pd.crosstab(index=df['Course of study'],
            columns=df['Result']).plot(kind='line')
plt.ylabel('Total')
plt.xlabel('course of study')
plt.title('Graduate and dropout data')
plt.show()


pd.crosstab(index=df['Marriage status'],
            columns=df['Application order']).plot(kind='bar')
plt.ylabel('Total')
plt.xlabel('Marriage status')
plt.title('Student dropout due to marriage')
plt.show()


pd.crosstab(df.Result, ['Age at enrollment']).plot(
    kind='pie', subplots=True, autopct='%1.1f%%')
plt.ylabel('Mode of Application')
plt.xlabel('age of enrollment')
plt.title('Student dropout due to age of enrollment')
plt.show()
