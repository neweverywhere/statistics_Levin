import pandas as pd


def min_max_std(df:pd.DataFrame, param:str): #стоковая стандартизация, приводящая к виду 0->1
    diff_minmax = df[param].max() - df[param].min()
    minimal = df[param].min()
    df[param+"_min-max_std"] = df[param].apply(lambda x: (x-minimal)/(diff_minmax-minimal))
    print(param+" min-max standartised")
    print(f"new column = {param}+_min-max_std")

def mean_std(df:pd.DataFrame, param:str): # -> {-1 0 1} я так понял, что это нормировка по умолчанию в М.стат
    mean = df[param].mean()
    df[param+"_mean-std"] = df[param].apply(lambda x: (x-mean/(df[param].std())))
    print(param+" mean standartised")
    print(f"new column = {param}+_mean-std")

