import os
import sys
from math import sqrt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

filename = "Final_Vectorised_Dataset.csv"

df = pd.read_csv(filename)

def func(x):
    values = x[1:-1].strip().split(' ')
    return sum([float(val) * float(val) for val in values if val.strip() != ''])

df['vector_mss'] = df['Title_Vector'].apply(lambda x : func(x))

df.head()

(df['Lines of Code'].min(), df['Lines of Code'].max())
(df['vector_mss'].min(), df['vector_mss'].max())
(df['Cyclomatic Complexity'].min(), df['Cyclomatic Complexity'].max())

df['loc_sr'] = df['Lines of Code'].apply(lambda x : sqrt(x))
(df['loc_sr'].min(), df['loc_sr'].max())

df['cc_sr'] = df['Cyclomatic Complexity'].apply(lambda x : sqrt(x))
(df['cc_sr'].min(), df['cc_sr'].max())

#plotting both graphs side by side
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(15, 5))
ax1.scatter(x=df['vector_mss'], y=df['loc_sr'], marker='.')
ax1.set_title('Title vector vs Lines of code')
ax2.scatter(x=df['vector_mss'], y=df['cc_sr'], marker='.')
ax2.set_title('Title vector vs Cyclomatic complexity')  
plt.tight_layout()
plt.show()

required_columns = ['loc_sr', 'Cyclomatic Complexity', 'vector_mss']
req_df = df[required_columns]

req_df.corr()
