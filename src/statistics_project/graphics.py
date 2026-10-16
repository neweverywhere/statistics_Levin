import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def make_histplot(data_frDF:pd.DataFrame,x_name:str,**kwargs):
    fig, axes = plt.subplots(figsize=(4, 4))
    sns.histplot(data=data_frDF,x=x_name,kde=True,ax=axes, bins=10)
    axes.set_title(f"Распределение {x_name}")
    axes.set_xlabel("")
    axes.set_ylabel("Количество")
    if kwargs is not None:
        for k,v in kwargs.items():
            axes.axvline(v, color="crimson", linestyle="--", linewidth=1,
                         label=f"quantile {v:.0f}")
    plt.tight_layout()
    plt.show()

def points_on_X(data_frDF:pd.DataFrame, first:str, second:str):
    #центририруем
    first_center = data_frDF[first] - data_frDF[first].mean()
    second_center = data_frDF[second] - data_frDF[second].mean()

    # Наложение на один график
    plt.figure()
    plt.plot(first_center, np.zeros_like(first_center), 'o', label=first)
    plt.plot(second_center, np.zeros_like(second_center), 's', color='red', label=second)
    plt.axhline(0, color='k', linewidth=0.5)
    plt.legend()
    plt.show()
def common_plt(data_frDF:pd.DataFrame, x_name:str):
    fig, axes = plt.subplots(figsize=(4, 4))
    sns.kdeplot(data=data_frDF,x=x_name,ax=plt.gca())
    axes.set_title(f"Распределение {x_name}")
    axes.set_xlabel("")
    axes.set_ylabel("Количество")

    plt.tight_layout()
    plt.show()