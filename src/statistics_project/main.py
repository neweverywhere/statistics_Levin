import dataset_injection
import graphics
from IPython.core.display import display_html
import check_undependence
df = dataset_injection.fileLoad('pyrovskytes.xlsx')
df.info()
#display_html(df[['EN(A)','EN(B)']].head(5))
print(check_undependence.check(df,'Bond length of A-O','r(AVI)'))
'''
можем поперебирать разные данные и увидеть, что длины связей ионов не зависят от приведенных в датасете велчин.
отметим, что в процессе образования молекул имеет значение градиент температур формирования связи,
локальные разности концентраций и межмолекулярные взаимодействия приводят к тому, что
длины связей становятся стохастической величиной, что также усиливается за счет
систематических погрешностей измерений длин
'''
graphics.make_histplot(df[df['Bond length of B-O']>0.1],'Bond length of B-O')
