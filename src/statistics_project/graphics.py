import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats


def make_histplot(data_frDF:pd.DataFrame, x_name:str, *, description:str= "",bins:int = 10,figsize:tuple=(4,4), **kwargs):
    fig, axes = plt.subplots(figsize=figsize)
    sns.histplot(data=data_frDF,x=x_name,kde=True,ax=axes, bins=bins)
    axes.set_title(f"Распределение {x_name}")
    axes.set_xlabel(description)
    axes.set_ylabel("количество")
    if kwargs:
        for k,v in kwargs.items():
            axes.axvline(v, color="crimson", linestyle="--", linewidth=1,
                         label=f"quantile {v:.0f}")
    plt.tight_layout()
    plt.show()
def points_on_surface(data_frDF:pd.DataFrame, x_name:str,y_name:str,
                      *,transperency:float=0.2,figsize:tuple=(4,4), hue:str="",description:str= ""):
    plt.figure(figsize=figsize)
    sns.scatterplot(data=data_frDF, x=x_name, y=y_name,
                    hue=hue, palette='viridis', alpha=transperency)
    plt.title(description)
    plt.xlabel(x_name)
    plt.ylabel(y_name)
    plt.show()
def points_on_X(data_frDF:pd.DataFrame, first:str, second:str):
    #центририруем
    first_center = data_frDF[first] - data_frDF[first].mean()
    second_center = data_frDF[second] - data_frDF[second].mean()

    #аложение на один график
    plt.figure()
    plt.plot(first_center, np.zeros_like(first_center), 'o', label=first)
    plt.plot(second_center, np.zeros_like(second_center), 's', color='red', label=second)
    plt.axhline(0, color='k', linewidth=0.5)
    plt.legend()
    plt.show()
def common_plt(data_frDF:pd.DataFrame, x_name:str, *,figsize:tuple=(4,4), description:str= ""):
    fig, axes = plt.subplots(figsize=figsize)
    sns.kdeplot(data=data_frDF,x=x_name,ax=plt.gca())
    axes.set_title(f"Распределение {x_name}")
    axes.set_xlabel(description)
    axes.set_ylabel(x_name)

    plt.tight_layout()
    plt.show()

def lognorm_graph(df_local:pd.DataFrame, param:str,*,figsizz:tuple=(10,6), bins:int = 100,X_rng:tuple = (0,50), description:str = "",Floc:float = -0.15):
    x = df_local[param].dropna().values
    shape, loc, scale = stats.lognorm.fit(x, floc=Floc)

    # График
    fig, ax = plt.subplots(figsize=figsizz)
    ax.hist(x, bins=bins, density=True, alpha=0.6, edgecolor='black', label='Данные')

    # Теоретическая кривая
    xs = np.linspace(0, x.max(), 500)
    ax.plot(xs, stats.lognorm.pdf(xs, shape, loc, scale), 'r-', linewidth=2, label='Логнормальное')

    ax.set_xlim(X_rng)
    ax.set_xlabel(param+' (г на 100 г)')
    ax.set_ylabel('Плотность')
    (ax.set_title(description)) if description != ""  else ax.set_title(f'Гистограмма {param} + логнормальная плотность')
    ax.legend()
    plt.show()