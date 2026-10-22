import pandas as pd
from IPython.display import display, display_html

from . import graphics

hw01version = "0.1"


#Exploratory Data Analysis - основные данные по всему датафрейму
def do_EDA(df:pd.DataFrame):
    print("shape = (str,clm) "+str(df.shape))
    print("===="*20)
    print(df.dtypes)
    print("===="*20)
    display_html(df.head(5))
    print("===="*20)
    df.info()

def EDA_one_param(data_frDF:pd.DataFrame, param:str,*, description:str= ""):
    df = data_frDF[param].copy()
    print("\n"*2)
    print("===="*20)
    print(f" начинаем анализ по {param} ".center(80,"="))
    if description != "": print(description.center(80, "="))
    print("===="*20+"\n")
    df.info()
    summary = {}
    summary["name"] =         param
    summary["amount"] =       df.count()
    summary["mean"] =         round(df.mean(),2)
    summary["min_value"] =    round(df.min(),2)
    summary["max_value"] =    round(df.max(),2)
    summary["std"] =          round(df.std(),2)
    summary["25% quantile"] = round(df.quantile(0.25),2)
    summary["50% quantile"] = round(df.quantile(0.5),2)
    summary["75% quantile"] = round(df.quantile(0.75),2)
    summary["95% quantile"] = round(df.quantile(0.95),2)
    print("Количество:".ljust(25," "),              summary["amount"]        )
    print("Среднее:".ljust(25," "),                 summary["mean"]          )
    print("Минимум:".ljust(25," "),                 summary["min_value"]     )
    print("Максимум:".ljust(25," "),                summary["max_value"]     )
    print("Стандартное отклонение:".ljust(25," "),  summary["std"]           )
    print("25-й перцентиль:".ljust(25," "),         summary["25% quantile"]  )
    print("50-й перцентиль:".ljust(25," "),         summary["50% quantile"]  )
    print("75-й перцентиль:".ljust(25," "),         summary["75% quantile"]  )
    print("95-й перцентиль:".ljust(25," "),         summary["95% quantile"]  )
    #тут попробуем оценить насколько перцентили в процентах от максимального разброса значений отстоят друг от друга
    print(f"25-й перцентиль и 50-й перцентили отстоят друг от друга на "
          + str(round((summary["25% quantile"]-summary["50% quantile"])/(df.min()-df.max())*100,1)).rjust(4,"0") + "% от всей длины отрезка")
    print(f"50-й перцентиль и 75-й перцентили отстоят друг от друга на "
          + str(round((summary["50% quantile"]-summary["75% quantile"])/(df.min()-df.max())*100,1)).rjust(4,"0") + "% от всей длины отрезка")
    print(f"75-й перцентиль и 95-й перцентили отстоят друг от друга на "
          + str(round((summary["75% quantile"]-summary["95% quantile"])/(df.min()-df.max())*100,1)).rjust(4,"0") + "% от всей длины отрезка")
    graphics.make_histplot(data_frDF,param,first = summary["25% quantile"],second = summary["50% quantile"]
                           , third = summary["75% quantile"], fourth = summary["95% quantile"],description = description)
    #graphics.common_plt(data_frDF,param)
    return summary
'''
Bond length of B-O достаточно сильно сконцентрирован около среднего значения, перцентили 
друг к другу прижаты
P.S. кажется, так можно находить выбросы. мы смотрим на процентную длину диапазона
от начала до первого квантиля а потом также от 90 до конца. если между квантилями разброс небольшой, 
а между концами и крайними квантилями большой, то есть основания проверить выбросы. 
B-O будем нормализовывать 
'''


def compare_EDAs(*, original:dict, compared:dict):
    if (original.get("name")==compared.get("name")):
        print("\n"+"====" * 20)
        print(f" сравнение EDA для '{original["name"]}' ".center(80, "="))
        print("====" * 20 + "\n")
        for k in original.keys():
            if k == "name":
                continue
            diff = original[k] - compared[k]
            print(f"Разница {k}:".ljust(25, " ") +
                  f"{diff:.2f}({(diff /original[k] )*100:.2f}%)".ljust(20, " ")+
                  f"(исходное/новое):({original[k]}/{compared[k]})")


    else:
        print("\n"*3+"попытка сравнить частные EDA для двух разных аргументов!".upper()+"\n"*3)
