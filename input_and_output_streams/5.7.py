import pandas
import matplotlib.pyplot as plt
import pathlib
from pathlib import Path

plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (15, 5)

fixed_df = pandas.read_csv('bikes.csv', encoding='latin1', parse_dates=['Date'], dayfirst=True,
                           index_col='Date')

fixed_df['Maisonneuve 1'][:10]

