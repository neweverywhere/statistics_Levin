import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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