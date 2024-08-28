import pandas as pd
from pandas_profiling import ProfileReport


class datavalidation:
        
        def intiatedatavalidation(self):
                
                
            print("rithin")
            data=pd.read_csv("D:\dataanalysisproj\dataanalysttool\data\data.csv")
            s=data.isnull().sum()
            print(s)
            data = data.fillna(method='ffill')
           
            print("++++++++++++++++++++")

                

