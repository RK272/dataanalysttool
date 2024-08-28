import pandas as pd


class datavalidation:
        
        def intiatedatavalidation(self):
                

                data=pd.read_csv("data/data.csv")
                print(data.head(5))
