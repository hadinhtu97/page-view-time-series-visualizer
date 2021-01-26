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
    df_bar = df.copy()
    df_bar['Years'] = df_bar.index.year
    df_bar['Months'] = df_bar.index.month
    df_bar = df_bar.rename(columns={
        'value': 'Average Page Views'
    })
    df_bar = df_bar.groupby(['Years', 'Months']).mean()
    df_bar = df_bar.reset_index()

    fig = sns.catplot(kind='bar', data=df_bar, x='Years',
                      y='Average Page Views', hue='Months', legend_out=False)

    legend = fig.axes.flat[0].get_legend()
    month_labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
                    'September', 'October', 'November', 'December']
    for t, l in zip(legend.texts, month_labels):
        t.set_text(l)

    fig.savefig('./img/bar_plot.png')


def draw_box_plot():
    pass
