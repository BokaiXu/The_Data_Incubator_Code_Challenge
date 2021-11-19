import pandas as pd
import numpy as np

df=pd.read_csv('dataset/content_based.csv')
df=df.drop(['Unnamed: 0'],axis=1)

df2=pd.read_csv('dataset/steam_app.csv')
df2=df2.rename(columns={'Unnamed: 0':'Steam_appid'})

def find_similar_games(app_id):
    """
    """
    lst_name=[]
    if app_id not in df2['Steam_appid'].tolist():
        return False
    else:
        name=df2.loc[df2['Steam_appid']==app_id,'name'].values[0]
        rec_id_lst=df.loc[df['app_id']==app_id].values[0][1:]
        lst_name.append(name)
        for ids in rec_id_lst:
            lst_name.append(df2.loc[df2['Steam_appid']==ids,'name'].values[0].strip())
        return lst_name
