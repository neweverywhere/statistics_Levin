import numpy as np
import pandas as pd
def check_R(data_frDF:pd.DataFrame, first:str, second:str):
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

def checkMI(data_frDF:pd.DataFrame, first:str, second: str):
    # '''
    # Берём два столбца из датасета и превращаем в numpy-массивы т кдаёт быстрый доступ и удобные операции.
    x = data_frDF[first].to_numpy()
    y = data_frDF[second].to_numpy()

    # Число бинов: ~sqrt(N). max(5, ...) — страховка, если данных мало.
    bins = max(5, int(np.sqrt(len(x))))
    bins = max(5, int(len(x)**0.4))

    # --- Наблюдаемая MI ---

    # histogram2d: считает, сколько точек попало в каждую ячейку сетки bins×bins.
    # hist_xy[i,j] = число точек с x в бине i и y в бине j.
    hist_xy, _, _ = np.histogram2d(x, y, bins=bins)

    # Нормируем: получаем совместные частоты p(x,y). Сумма всех = 1.
    p_xy = hist_xy / hist_xy.sum()

    # Маргинальные частоты. keepdims=True сохраняет форму (bins,1) и (1,bins),
    # чтобы при умножении получилась матрица (bins,bins) — broadcasting.
    p_x = p_xy.sum(axis=1, keepdims=True)  # распределение X
    p_y = p_xy.sum(axis=0, keepdims=True)  # распределение Y

    # Ожидаемое совместное распределение при независимости: p(x)·p(y)
    p_indep = p_x * p_y

    # MI = Σ p(x,y) · log( p(x,y) / (p(x)·p(y)) ).
    # mask = p_xy > 0 — там, где частота 0, log(0) неопределён, эти ячейки пропускаем.
    mask = p_xy > 0
    mi = np.sum(p_xy[mask] * np.log(p_xy[mask] / p_indep[mask]))

    print(f"MI = {mi:.5f} nats")

    # --- Перестановочный тест ---

    # Генератор случайных чисел с фиксированным seed для воспроизводимости.
    rng = np.random.default_rng(0)

    # Массив, куда сложим MI для 1000 перемешанных версий y.
    mi_null = np.empty(1000)

    # Цикл: 1000 раз перемешиваем y и считаем MI заново.
    for i in range(1000):
        # rng.permutation(y) — случайная перестановка значений y.
        # Пары (x_i, y_i) теряют связь, но распределения x и y сохраняются.
        y_sh = rng.permutation(y)

        # Тот же расчёт MI, но на перемешанных данных.
        h, _, _ = np.histogram2d(x, y_sh, bins=bins)
        p_xy_s = h / h.sum()
        px_s = p_xy_s.sum(axis=1, keepdims=True)
        py_s = p_xy_s.sum(axis=0, keepdims=True)
        p_ind = px_s * py_s
        m = p_xy_s > 0
        mi_null[i] = np.sum(p_xy_s[m] * np.log(p_xy_s[m] / p_ind[m]))

    # p-value: доля перемешанных MI, которые оказались ≥ наблюдаемой.
    # Если связь реальна, наблюдаемая MI будет заметно больше "шумовых".
    p_value = (mi_null >= mi).mean()
    print(f"p-value = {p_value:.4f}")

    # --- Нормированная MI (для интерпретации "много/мало") ---

    # Энтропия H(X) = -Σ p(x)·log p(x). Верхняя граница MI.
    h_x = -np.sum(p_x[p_x > 0] * np.log(p_x[p_x > 0]))
    h_y = -np.sum(p_y[p_y > 0] * np.log(p_y[p_y > 0]))

    # NMI ∈ [0,1]: 0 — независимы, 1 — полностью связаны.
    nmi = mi / min(h_x, h_y)
    print(f"NMI = {nmi:.3f}")
    # '''