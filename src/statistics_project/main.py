import dataset_injection
from . import math_model, graphics, check_undependence, EDA

df = dataset_injection.fileLoad('pyrovskytes.xlsx')
df = df[df['Bond length of B-O'] > 0.1]
df = df[df['Bond length of A-O'] > 0.1]
#df.info()
#print(df["B Valence"].unique())
#print(df["B Valence"].describe())
#print(df["EN(B)"].unique())
#print(df["EN(B)"].describe())
#print(df["Electronegativity difference with radius"].unique())
#for i in range(7):
#    #graphics.common_plt(df[df["B Valence"] == i-1], 'Bond length of B-O',desctiption="B valence = "+str(i-1))
#    EDA.EDA_one_param(df[df["B Valence"] == i-1], 'Bond length of B-O',description=(" Bval = "+str(i-1)))
#    pass

# display_html(df[['EN(A)','EN(B)']].head(5))
'''
можем поперебирать разные данные и увидеть, что длины связей ионов не зависят от приведенных в датасете велчин.
отметим, что в процессе образования молекул имеет значение градиент температур формирования связи,
локальные разности концентраций и межмолекулярные взаимодействия приводят к тому, что
длины связей становятся стохастической величиной, что также усиливается за счет
систематических погрешностей измерений длин - устарело!!!

сначала общая EDA,проверка независимости, потом по нашей переменной EDA, графики, 
сделать частную выборку, взять по ней частную EDA и сравнить с исходной, нормировка и стандартизация

'''
EDA.do_EDA(df)


#graphics.points_on_X(df,'Bond length of A-O','Bond length of B-O')
#print(check_undependence.checkP(df, 'Bond length of A-O', 'r(AVI)'))
#set = ('r(AVI)','Bond length of A-O',"EN(B)","EN(A)", "ionic radius of A")
#for i in set:
#    print(f"check dependence of {i} and bond length of B-O")
#    print(check_undependence.checkMI(df, i, 'Bond length of B-O'))
#print(check_undependence.checkMI(df, 'r(AVI)', 'Bond length of B-O'))
#TODO: рассмотреть попарной сверки со всеми параметтрами? -очень долго считается, В КОНЦЕ
#TODO: добавить вторую проверку независимости, т.к. может не увидеть y=x^2


#BO_EDA = EDA.EDA_one_param(df,'Bond length of B-O')
#graphics.common_plt(df, 'Bond length of B-O')
#graphics.make_histplot(df[df['Bond length of B-O']>0.1],'Bond length of B-O')
#graphics.make_histplot(df[df['Bond length of B-O']>0.1],'Bond length of A-O')


#df_SELECTED = sample_set.make_selection(df,325)
#BO_EDA_N = EDA.EDA_one_param(df_SELECTED,'Bond length of B-O')
#EDA.compare_EDAs(original=BO_EDA,compared=BO_EDA_N)
'''
по сиду 112312 удивительно точно подбирает
'''
#standartise.mean_std(df_SELECTED,'Bond length of B-O')
#EDA.EDA_one_param(df_SELECTED,'Bond length of B-O'+"_mean-std")

'''
небольшое предварительное описание мат базы: все длины связей имеют строго положительную величину,
значения сильно сгруппированы вокруг среднего, однако диаграмма имеет двухпиковый вид при 10 бинах
похожа на график с перегибом, из того, что смог подобрать, это 10*ln(x)/(x^2) или (10/x)*e^(-1/x)

'''
#math_model.bic_in_multinormal_model(df[df["B Valence"] == 4], 'Bond length of B-O',description="B Valence = 4")

#for i in range(-1,6):  #переберём валентности
#    #math_model.bic_in_multinormal_model(df[df["B Valence"] == i], 'Bond length of B-O',description=f"B Valence = {str(i)}")
#    graphics.make_histplot(df[df["B Valence"] == i],'Bond length of B-O',bins = 20,description=f"Bval = {i}")
#    pass
'''
для каждой валентности B-O:
bic_res_BO={-1=5,0=2,1=6,2=6,3=5,4=3,5=4}
или списком: [5,2,6,6,5,3,4]
'''
#bic_res_BO={-1:5,
#            0:2,
#            1:6,
#            2:6,
#            3:5,
#            4:3,
#            5:4}
#for val,comp in bic_res_BO.items():
#    math_model.check_multinormal_model(df[df["B Valence"] == val],param='Bond length of B-O',components=comp,
#                                       autoBIC=False,description=f"Bval = {val}")
'''
смог отметить на графике, что видит компьютер!
видим каждую компоненту, на которую он реагирует при большом числе бинов

'''



