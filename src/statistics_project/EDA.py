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

def EDA_one_param(data_frDF:pd.DataFrame, param:str,*,
                  shut_print:bool = False,shut_graphics:bool = False, description:str= "", round_num:int = 2, output_round_num:int = 2):
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
    summary["mean"] =         round(df.mean(),          round_num)
    summary["min_value"] =    round(df.min(),           round_num)
    summary["max_value"] =    round(df.max(),           round_num)
    summary["std"] =          round(df.std(),           round_num)
    summary["25% quantile"] = round(df.quantile(0.25),  round_num)
    summary["50% quantile"] = round(df.quantile(0.5),   round_num)
    summary["75% quantile"] = round(df.quantile(0.75),  round_num)
    summary["95% quantile"] = round(df.quantile(0.95),  round_num)
    if shut_print:
        pass
    else:
        print("Количество:".ljust(25," "),              str(round(summary["amount"]        ,output_round_num  )))
        print("Среднее:".ljust(25," "),                 str(round(summary["mean"]          ,output_round_num  )))
        print("Минимум:".ljust(25," "),                 str(round(summary["min_value"]     ,output_round_num  )))
        print("Максимум:".ljust(25," "),                str(round(summary["max_value"]     ,output_round_num  )))
        print("Стандартное отклонение:".ljust(25," "),  str(round(summary["std"]           ,output_round_num  )))
        print("25-й перцентиль:".ljust(25," "),         str(round(summary["25% quantile"]  ,output_round_num  )))
        print("50-й перцентиль:".ljust(25," "),         str(round(summary["50% quantile"]  ,output_round_num  )))
        print("75-й перцентиль:".ljust(25," "),         str(round(summary["75% quantile"]  ,output_round_num  )))
        print("95-й перцентиль:".ljust(25," "),         str(round(summary["95% quantile"]  ,output_round_num  )))
        #тут попробуем оценить насколько перцентили в процентах от максимального разброса значений отстоят друг от друга
        print(f"25-й перцентиль и 50-й перцентили отстоят друг от друга на "
              + str(round((summary["25% quantile"]-summary["50% quantile"])/(df.min()-df.max())*100,1)).rjust(4,"0") + "% от всей длины отрезка")
        print(f"50-й перцентиль и 75-й перцентили отстоят друг от друга на "
              + str(round((summary["50% quantile"]-summary["75% quantile"])/(df.min()-df.max())*100,1)).rjust(4,"0") + "% от всей длины отрезка")
        print(f"75-й перцентиль и 95-й перцентили отстоят друг от друга на "
              + str(round((summary["75% quantile"]-summary["95% quantile"])/(df.min()-df.max())*100,1)).rjust(4,"0") + "% от всей длины отрезка")
    if shut_graphics:
        pass
    else:
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
            diff = compared[k] - original[k]
            try:
                pct = f"{(diff / original[k]) * 100:.2f}%"
            except ZeroDivisionError:
                pct = "/0(!!)"
            print(f"Разница {k}:".ljust(25, " ") +
                  f"{diff:.2f}({pct}    )".ljust(20, " ")+
                  f"(исходное/новое):({original[k]}/{compared[k]})")



    else:
        print("\n"*3+"попытка сравнить частные EDA для двух разных аргументов!".upper()+"\n"*3)
