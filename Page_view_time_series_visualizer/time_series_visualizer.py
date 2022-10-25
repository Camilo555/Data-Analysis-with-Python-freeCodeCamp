import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df =  pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Clean data
l = int(round((2.5*len(df.index))/100,))
df_top = df['value'].nlargest(n=l)
df_bot = df['value'].nsmallest(n=l)

df = df[(~df.value.isin(df_top)) & (~df.value.isin(df_bot))]



def draw_line_plot():
    # Draw line plot
    fig = plt.figure(figsize=(15, 8), dpi=100)
    ax = fig.add_subplot(111)

    df.plot(color='red', title = 'Daily freeCodeCamp Forum Page Views 5/2016-12/2019', ax=ax,legend=False)
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
  
    rect = fig.patch
    rect.set_facecolor("white")

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_2 = df.copy()
    df_2['day'] = df_2.index.day
    df_2['month'] = df_2.index.month
    df_2['Months'] = df_2.index.month_name()
    df_2['year'] = df_2.index.year
    df_2.reset_index()
    df_2.sort_values('month')

    df_g = df_2.groupby(['year','Months'])['value'].mean().unstack()
    new_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    df_g = df_g.reindex(new_order, axis=1)
    df_g.index.name = 'Years'
  
    # Draw bar plot
    fig = plt.figure(figsize=(10, 10), dpi=100)
    ax = fig.add_subplot(111)

    df_g.plot.bar(ax=ax)
    ax.set_ylabel('Average Page Views')
    rect = fig.patch
    rect.set_facecolor("white")

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box['month'] = df_box.index.month
    df_box.reset_index(inplace=True)
    df_box['Year'] = [d.year for d in df_box.date]
    df_box['Month'] = [d.strftime('%b') for d in df_box.date]

    df_box.rename(columns = {'value':'Page Views'}, inplace = True)
    df_box = df_box.sort_values('month')
  
    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20,10))

    sns.boxplot(x="Year", y= "Page Views", data=df_box, ax=ax1)
    ax1.set_title('Year-wise Box Plot (Trend)')

    sns.boxplot(x="Month", y= "Page Views", data=df_box, ax=ax2)
    ax2.set_title('Month-wise Box Plot (Seasonality)')
    plt.setp((ax1,ax2),yticks=[0,20000,40000,60000,80000,100000,120000,140000,160000,180000,200000])
    rect = fig.patch
    rect.set_facecolor("white")

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
