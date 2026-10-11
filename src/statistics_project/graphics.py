import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def make_histplot(data_frDF:pd.DataFrame,x_name:str):
    fig, axes = plt.subplots(figsize=(4, 4))
    sns.histplot(
        data=data_frDF,
        x=x_name,
        kde=True,
        ax=axes
        , bins=10
        # изменяет число столбцов, а следовательно, и точность. при интегральных количествах(100+, наприммер) теряет смысл
    )
    axes.set_title(f"Распределение {x_name}")
    axes.set_xlabel("")
    axes.set_ylabel("Количество")

    plt.tight_layout()
    plt.show()