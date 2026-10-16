import numpy as np
import dataset_injection
from sklearn.feature_selection import mutual_info_regression
import graphics
import EDA
from IPython.core.display import display_html
import check_undependence
from src.statistics_project import sample_set

df = dataset_injection.fileLoad('pyrovskytes.xlsx')
df = df[df['Bond length of B-O'] > 0.1]
df = df[df['Bond length of A-O'] > 0.1]
# df.info()
# display_html(df[['EN(A)','EN(B)']].head(5))
'''
можем поперебирать разные данные и увидеть, что длины связей ионов не зависят от приведенных в датасете велчин.
отметим, что в процессе образования молекул имеет значение градиент температур формирования связи,
локальные разности концентраций и межмолекулярные взаимодействия приводят к тому, что
длины связей становятся стохастической величиной, что также усиливается за счет
систематических погрешностей измерений длин - устарело!!!

сначала общая EDA,проверка независимости, потом по нашей переменной EDA, графики,  
нормировка и стандартизация, сделать частную выборку, взять по ней частную EDA и сравнить с исходной

'''
#EDA.do_EDA(df)


#graphics.points_on_X(df,'Bond length of A-O','Bond length of B-O')
#print(check_undependence.checkP(df, 'Bond length of A-O', 'r(AVI)'))
#print(check_undependence.checkMI(df, 'Bond length of A-O', 'Bond length of B-O'))
#TODO: рассмотреть попарной сверки со всеми параметтрами? -очень долго считается, В КОНЦЕ
#TODO: добавить вторую проверку независимости, т.к. может не увидеть y=x^2


EDA.EDA_one_param(df,'Bond length of B-O')

#graphics.common_plt(df, 'Bond length of B-O')
#graphics.make_histplot(df[df['Bond length of B-O']>0.1],'Bond length of B-O')
#graphics.make_histplot(df[df['Bond length of B-O']>0.1],'Bond length of A-O')


df_SELECTED = sample_set.make_selection(df,325)
EDA.EDA_one_param(df_SELECTED,'Bond length of B-O')
'''
т.к. значения очень близки к среднему, даже маленькая выборка по умолчанию(сейчас 150 стоит) очень близка 
к исходному. имеет смысл сделать оценку отклонений (где?)
'''
#TODO: сделать оценку отклонений выборку от ЕДА. добавить возвращаемые значения ЕДА?





