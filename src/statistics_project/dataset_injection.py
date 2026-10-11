import pandas as pd
def fileLoad(name:str='pyrovskytes.xlsx'):
    df = pd.read_excel(name, sheet_name=0)
    df = df.dropna()
    return df


