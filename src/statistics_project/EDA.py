import pandas as pd
from IPython.core.display_functions import display
from IPython.core.display import display_html

from src.statistics_project import graphics

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

def EDA_one_param(data_frDF:pd.DataFrame, param:str):
    df = data_frDF[param].copy()
    print("\n"*2)
    print("===="*20)
    print(f"начинаем анализ по {param}".center(80,"="))
    print("===="*20+"\n")
    df.info()
    first_qua=round(df.quantile(0.25),2)
    second_qua=round(df.quantile(0.5),2)
    third_qua=round(df.quantile(0.75),2)
    fourth_qua=round(df.quantile(0.95),2)
    print("Количество:".ljust(25," "),              df.count())
    print("Среднее:".ljust(25," "),                 round(df.mean(),2))
    print("Минимум:".ljust(25," "),                 round(df.min(),2))
    print("Максимум:".ljust(25," "),                round(df.max(),2))
    print("Стандартное отклонение:".ljust(25," "),  round(df.std(),2))
    print("25-й перцентиль:".ljust(25," "),         first_qua )
    print("50-й перцентиль:".ljust(25," "),         second_qua)
    print("75-й перцентиль:".ljust(25," "),         third_qua )
    print("95-й перцентиль:".ljust(25," "),         fourth_qua)
    #тут попробуем оценить насколько перцентили в процентах от максимального разброса значений отстоят друг от друга
    print(f"25-й перцентиль и 50-й перцентили отстоят друг от друга на "
          + str(round((first_qua-second_qua)/(df.min()-df.max())*100,1)).rjust(4,"0") + "% от всей длины отрезка")
    print(f"50-й перцентиль и 75-й перцентили отстоят друг от друга на "
          + str(round((second_qua-third_qua)/(df.min()-df.max())*100,1)).rjust(4,"0") + "% от всей длины отрезка")
    print(f"75-й перцентиль и 95-й перцентили отстоят друг от друга на "
          + str(round((third_qua-fourth_qua)/(df.min()-df.max())*100,1)).rjust(4,"0") + "% от всей длины отрезка")
    graphics.make_histplot(data_frDF,param,first = first_qua,second = second_qua
                           , third = third_qua, fourth = fourth_qua)
'''
Bond length of B-O достаточно сильно сконцентрирован около среднего значения, перцентили 
друг к другу прижаты
P.S. кажется, так можно находить выбросы. мы смотрим на процентную длину диапазона
от начала до первого квантиля а потом также от 90 до конца. если между квантилями разброс небольшой, 
а между концами и крайними квантилями большой, то есть основания проверить выбросы. 
B-O будем нормализовывать 
'''

