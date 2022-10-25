import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
BMI  = df['weight']/((df['height']/100)**2)
df['overweight'] = [1 if i>25 else 0 for i in BMI]

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.

chol = df.cholesterol
glu = df.gluc
for i in range(len(chol)):
    if chol.loc[i]==1 and glu.loc[i]==1:
        chol.loc[i]=0
        glu.loc[i]=0

    elif chol.loc[i]==1 and glu.loc[i]==0:
        chol.loc[i]=0

    elif chol.loc[i]==0 and glu.loc[i]==1:
        glu.loc[i]=0

    elif chol.loc[i]>1 and glu.loc[i]==1:
        chol.loc[i]=1
        glu.loc[i]=0

    elif chol.loc[i]>1 and glu.loc[i]==0:
        chol.loc[i]=1

    elif chol.loc[i]>1 and glu.loc[i]>1:
        chol.loc[i]=1
        glu.loc[i]=1

    elif chol.loc[i]==1 and glu.loc[i]>1:
        chol.loc[i]=0
        glu.loc[i]=1

    elif chol.loc[i]==0 and glu.loc[i]>1:
        glu.loc[i]=1

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_m = df[['cholesterol','gluc','smoke', 'alco', 'active', 'overweight','id']]
    df_cat = df_m.melt('id', var_name='variable',  value_name='value')

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_card = df[['cardio','id']]
    df_cat = pd.merge(df_cat, df_card, on='id')
    df_cat_sorted = df_cat.sort_values('variable')
    
    # Draw the catplot with 'sns.catplot()'
    
    g = sns.catplot(x="variable", hue='value', col="cardio", data=df_cat_sorted, kind='count')
    g.set_axis_labels("variable", "total")

    # Get the figure for the output
    fig = plt.figure(1)
    rect = fig.patch
    rect.set_facecolor("white")


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    
    # Clean the data
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))]
    
    # Calculate the correlation matrix
    corr = df_heat.corr()
    col = corr.columns

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize = (10,10))
    rect = fig.patch
    rect.set_facecolor("white")

    # Draw the heatmap with 'sns.heatmap()'
    a = sns.heatmap(corr, xticklabels=col, yticklabels=col, mask=mask, annot= True, vmin = -0.15, vmax= 0.3, linewidths=0.5, square=True, center=0, annot_kws={"size": 10}, fmt='.1f', ax=ax, cbar_kws={'ticks':[0.24,0.16,0.08,0.00,-0.08], "shrink": 0.4})

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
