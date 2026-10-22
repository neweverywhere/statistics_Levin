import pandas as pd
from sklearn.mixture import GaussianMixture

from . import graphics


def check_multinormal_model(df:pd.DataFrame,*, param:str,components:int = 1, autoBIC:bool = False,description:str = ""):

    if autoBIC:
        result = bic_in_multinormal_model(df,param)
        components = list(result.keys())[list(result.values()).index(min(result.values()))]
        '''
        работает дай бог в половине случаев для 
        bic_in_multinormal_model(df[df["B Valence"] == 4], 'Bond length of B-O'
        выдает монотонное убывание. лучше самому посмотреть и выбрать. если монотонно убывает, то берем
        наибольшую разность  в убывании, лень было прикручивать
        '''
        #TODO: прикрутить нормальный autoBIC
    print("\n"*3)
    print("====" * 20)
    print(f" начинаем мультимодальный анализ для числа компонент = {components} ".center(80, "="))
    if description != "": print(description.center(80, "="))
    print("====" * 20 + "\n")


    x = df[param].values.reshape(-1, 1)
    gm = GaussianMixture(n_components=components, random_state=42).fit(x)
    lines_list = gm.means_.flatten()
    print(f"Средние компонент: {lines_list}")
    print(f"Дисперсии: {gm.covariances_.flatten()}")
    print(f"Веса: {gm.weights_}")
    lines = {f"{i}":lines_list[i] for i in range(len(lines_list))}

    graphics.make_histplot(df, param, bins=20, description=description,**lines)


def bic_in_multinormal_model(df:pd.DataFrame, param:str,*,description:str = ""):
    print("===="*20)
    if description != "": print(description.center(80, "="))
    print("===="*20+"\n")
    x = df[param].values.reshape(-1, 1)
    # Чтобы понять, сколько компонент нужно, сравнивай BIC:
    result = {}
    for k in range(1,10):
        gm = GaussianMixture(n_components=k, random_state=42).fit(x)
        result[k]=gm.bic(x)
        print(f"components={k}: BIC = {gm.bic(x):.2f}")
    return result