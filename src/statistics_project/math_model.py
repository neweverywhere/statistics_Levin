import pandas as pd
from sklearn.mixture import GaussianMixture

from . import graphics


def check_multinormal_model(df:pd.DataFrame,*, param:str,components:int = 1, autoBIC:bool = False,description:str = "",bins:int = 20):

    if autoBIC:
        result = bic_in_multinormal_model(df,param)
        components = list(result.keys())[list(result.values()).index(min(result.values()))]
        # просто взяли индекс минимального значения и применили к ключам
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
    round_list = lambda x: list(map(lambda y: round(float(y),2),x))
    lines_list = round_list(gm.means_.flatten())
    print(f"Средние компонент: {lines_list}")
    print(f"Дисперсии: {round_list(gm.covariances_.flatten())}")
    print(f"Веса: {round_list(gm.weights_)}")
    lines = {f"{i}":lines_list[i] for i in range(len(lines_list))}

    graphics.make_histplot(df, param, bins=bins, description=description,**lines)


def bic_in_multinormal_model(df:pd.DataFrame, param:str,*,description:str = "",search_range:int = 10, giveDiff:bool = False):
    print("===="*20)
    if description != "": print(description.center(80, "="))
    print("===="*20+"\n")
    x = df[param].values.reshape(-1, 1)
    # Чтобы понять, сколько компонент нужно, сравним BIC:
    result = {}
    for k in range(1,search_range):
        gm = GaussianMixture(n_components=k, random_state=42).fit(x)
        result[k]=gm.bic(x)
        if giveDiff:
            if k>1:
                print(f"components={k}: BIC = {gm.bic(x):.2f}     {chr(8710)}BIC = {result[k-1]-result[k]:.2f}")
                continue
        print(f"components={k}: BIC = {gm.bic(x):.2f}")
    return result