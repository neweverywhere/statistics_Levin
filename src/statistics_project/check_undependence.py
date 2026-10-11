import pandas as pd
def check(data_frDF:pd.DataFrame,first:str,second:str):
    #a = 0
    #meanEN_A = data_frDF[first].mean()
    #meanEN_B = data_frDF[second].mean()
    #summary_of_deviations = 0
    #EN_B_dev_sum = 0
    #EN_A_dev_sum = 0
    #for row in data_frDF[[first, second]].itertuples(index=False):
    #    summary_of_deviations += (row[0] - meanEN_A) * (row[1] - meanEN_B)
    #    EN_A_dev_sum += (row[0] - meanEN_A) ** 2
    #    EN_B_dev_sum += (row[1] - meanEN_B) ** 2
    #    a += 1
    #    if a > 150: #считаем по первым 150 записям
    #        break
    #Pirson_R = summary_of_deviations / ((EN_A_dev_sum * EN_B_dev_sum) ** 0.5)

    #тут мы видим, что мой цикл находится в одном порядке по результату с df[].corr
    #для простоты и скорости дальше будет использоваться df[].corr(df[])
    Pirson_R = data_frDF[first].corr(data_frDF[second])

    return round(Pirson_R ** 2,4)