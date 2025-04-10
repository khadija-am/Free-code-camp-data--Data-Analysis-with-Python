import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')


# 2
df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2) > 25).astype(int)

# 3
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(
        df,
        id_vars=['cardio'],
        value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
        )


    # 6
    df_cat = df_cat.value_counts().reset_index(name='total')
    

    # 7
    fig = sns.catplot(
        x='variable', y='total', hue='value', col='cardio',
        data=df_cat, kind='bar'
    ).fig


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat =df.copy()

# Remove rows where diastolic pressure is higher than systolic
df_heat = df_heat[df_heat['ap_lo'] <= df_heat['ap_hi']]

# Remove rows where height is less than the 2.5th percentile or greater than the 97.5th percentile
df_heat = df_heat[(df_heat['height'] >= df_heat['height'].quantile(0.025)) & 
(df_heat['height'] <= df_heat['height'].quantile(0.975))]

# Remove rows where weight is less than the 2.5th percentile or greater than the 97.5th percentile
df_heat = df_heat[(df_heat['weight'] >= df_heat['weight'].quantile(0.025)) & 
(df_heat['weight'] <= df_heat['weight'].quantile(0.975))]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))


    # 14
    plt.figure(figsize=(10, 8))
    # 15
    sns.heatmap(corr, 
            annot=True,      
            cmap='coolwarm',  
            mask=mask,        
            cbar_kws={"shrink": .8}, 
            fmt='.2f')       


    # 16
    fig.savefig('heatmap.png')
    return fig
