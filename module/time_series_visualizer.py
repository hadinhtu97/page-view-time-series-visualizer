import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('./data/data.csv', index_col='date', parse_dates=True)
df = df[(df['value'] >= df['value'].quantile(0.025))
        & (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    plt.plot(df.index, df['value'], c='r')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.savefig('./img/line_plot.png')


def draw_bar_plot():
    pass


def draw_box_plot():
    pass
