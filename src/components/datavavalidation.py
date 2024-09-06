import pandas as pd
from pandas_profiling import ProfileReport
import os
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

class datavalidation:
        
        def intiatedatavalidation(self,columns):
                
            data_dir = 'droped'  
            print("rithin")
            data=pd.read_csv("D:\dataanalysisproj\dataanalysttool\data\data.csv")
            s=data.isnull().sum()
            print(s)
            #data = data.fillna(data.mean())
            data=data.dropna()
            print("qqqqq")
            data = data.drop_duplicates()
            print("wwwwwwwwww")
            column_list = [col.strip() for col in columns.split(',')]
            print("Columns to process:", column_list)
        
        # Drop specified columns from DataFrame
            
            dropped_columns = [col for col in column_list if col in data.columns]
            if dropped_columns:

                data = data.drop(columns=dropped_columns, axis=1)
            if not os.path.exists(data_dir):
                os.makedirs(data_dir)
        # Save the modified DataFrame
            data.to_csv("droped/data_dropped.csv", index=False)
           
            print("++++++++++++++++++++")
            return data
        

    
        def intiatedatavalidationn(self, columns, dataty):
                data_dir = 'dataa'
                print("rithin")

                # Read the CSV file
                data = pd.read_csv("D:/dataanalysisproj/dataanalysttool/dataa/data.csv")

                # Check for missing values and drop rows with missing values
                s = data.isnull().sum()
                print(s)
                data = data.dropna()
                print("qqqqq")

                # Drop duplicate rows
                data = data.drop_duplicates()
                print("wwwwwwwwww")
                dataq=data

                # Split columns and data types
                column_list = [col.strip() for col in columns.split(',')]
                data_types = [dtype.strip() for dtype in dataty.split(',')]

                print("Columns to process:", column_list)

                # Convert columns to specified data types
                for col, dtype in zip(column_list, data_types):
                        if col in data.columns:
                                try:

                                        if dtype == 'str':
                                                data[col] = data[col].astype(str)
                                        elif dtype == 'int':
                                                data[col] = pd.to_numeric(data[col], errors='coerce').astype('Int64')
                                        elif dtype == 'float':
                                                data[col] = pd.to_numeric(data[col], errors='coerce').astype(float)
                                        elif dtype == 'datetime':
                                                data[col] = pd.to_datetime(data[col], errors='coerce')
                                        else:
                                                print(f"Unsupported data type: {dtype}")
                                except Exception as e:
                                        print(f"Error converting column {col} to {dtype}: {e}")

                print('ri')

                # Ensure the directory exists
                if not os.path.exists(data_dir):
                        os.makedirs(data_dir)

                # Save the modified DataFrame
                output_path = os.path.join(data_dir, "data_modified.csv")
                data.to_csv(output_path, index=False)
                print(f"Data saved to {output_path}")
                df=data
                
                info_data = {
                        'Column': df.columns,
                        'Non-Null Count': df.notna().sum(),
                        'Dtype': df.dtypes
                        }


                info_df = pd.DataFrame(info_data)

# Reset index to match the format from df.info()
                info_df.reset_index(drop=True, inplace=True)

# Convert Non-Null Count to string format like in df.info()
                info_df['Non-Null Count'] = info_df['Non-Null Count'].astype(str) + ' non-null'

# Convert Dtype to string format
                info_df['Dtype'] = info_df['Dtype'].astype(str)


                print("++++++++++++++++++++")
                return info_df


        
        def describe(self):
                
            data_dir = 'describe'  
            print("rithin")
            data=pd.read_csv("D:\dataanalysisproj\dataanalysttool\describe\describe.csv")
            
            
            #data = data.fillna(data.mean())
            data=data.describe().T
            print("qqqqq")
            
            print("wwwwwwwwww")
            
            
        
        # Drop specified columns from DataFrame
            
            
            if not os.path.exists(data_dir):
                os.makedirs(data_dir)
        # Save the modified DataFrame
            data.to_csv("describe/describe.csv", index=False)
           
            print("++++++++++++++++++++")
            return data
        
        def info(self):
                
            data_dir = 'info'  
            print("rithin")
            df=pd.read_csv("D:\dataanalysisproj\dataanalysttool\info\info.csv")
            
            info_data = {
                        'Column': df.columns,
                        'Non-Null Count': df.notna().sum(),
                        'Dtype': df.dtypes
                        }


            info_df = pd.DataFrame(info_data)

# Reset index to match the format from df.info()
            info_df.reset_index(drop=True, inplace=True)

# Convert Non-Null Count to string format like in df.info()
            info_df['Non-Null Count'] = info_df['Non-Null Count'].astype(str) + ' non-null'

# Convert Dtype to string format
            info_df['Dtype'] = info_df['Dtype'].astype(str)

            #data = data.fillna(data.mean())
            
            print("qqqqq")
            
            print("wwwwwwwwww")
            
            
        
        # Drop specified columns from DataFrame
            
            
            if not os.path.exists(data_dir):
                os.makedirs(data_dir)
        # Save the modified DataFrame
            info_df.to_csv("info/info.csv", index=False)
           
            print("++++++++++++++++++++")
            return info_df
        def checkuniquevalues(self, columns: str) -> dict:

                data_dir = 'droped'  
                print("rithin")
                data = pd.read_csv("D:\\dataanalysisproj\\dataanalysttool\\data1\\data.csv")  # Use raw string or double backslashes for Windows paths
                s = data.isnull().sum()
                print(s)
                
                # Drop any rows with NaN values
                data = data.dropna()
                print("Data after dropping NaN values:")
                print(data)
                
                # Drop duplicate rows
                data = data.drop_duplicates()
                print("Data after dropping duplicates:")
                print(data)
                
                column_list = [col.strip() for col in columns.split(',')]
                print("Columns to process:", column_list)
                
                unique_values = {}
                for col in column_list:
                        if col in data.columns:
                                unique_values[col] = data[col].unique().tolist()  # Get unique values for each specified column
                
                print("Unique values in each column:", unique_values)
                return unique_values
        def filter(self, columns: str,columns1,orand1,dataty1) -> dict:

                data_dir = 'filter'  
                print("rithin")
                data = pd.read_csv("D:\\dataanalysisproj\\dataanalysttool\\filter\\data.csv")  # Use raw string or double backslashes for Windows paths
                s = data.isnull().sum()
                print(s)
                
                # Drop any rows with NaN values
                data = data.dropna()
                print("Data after dropping NaN values:")
                print(data)
                
                # Drop duplicate rows
                data = data.drop_duplicates()
                print("Data after dropping duplicates:")
                print(data)
                
                column_list = [col.strip() for col in columns.split(',')]
                print("Columns to process:", column_list)
                column_list1 = [col1.strip() for col1 in columns1.split(',')]
                print("Columns to process:", column_list1)
                if column_list and column_list1:
                     for col in column_list:
                          for col1 in column_list1:
                               if col in data.columns:
                                    
                                    print(col1)
                                    
                                    if dataty1=='INT':
                                        col1=int(col1)
                                        if orand1=='GE':
                                             d=np.where(data[col] >= col1)[0]
                                        elif orand1=='LE':
                                             d=np.where(data[col] <= col1)[0] 
                                        elif orand1=='NE':
                                             d=np.where(data[col] != col1)[0]
                                        else:
                                             d=np.where(data[col] == col1)[0] 
                                 
                                    else:
                                        if orand1=='GE':
                                             d=np.where(data[col] >= col1)[0]
                                        elif orand1=='LE':
                                             d=np.where(data[col] <= col1)[0] 
                                        elif orand1=='NE':
                                             d=np.where(data[col] != col1)[0]
                                        else:
                                             d=np.where(data[col] == col1)[0] 
                                                  
                                        
                                        
                                    data=data.iloc[d]

                 # Get unique values for each specified column
                
                
                return data
        def filter2(self, columns1a: str,columns1b,columns2a: str,columns2b,orand: str,dataty: str) -> dict:

                data_dir = 'filter2'  
                print("rithin")
                data = pd.read_csv("D:\\dataanalysisproj\\dataanalysttool\\filter2\\data.csv")  # Use raw string or double backslashes for Windows paths
                s = data.isnull().sum()
                print(s)
                
                # Drop any rows with NaN values
                data = data.dropna()
                print("Data after dropping NaN values:")
                print(data)
                
                # Drop duplicate rows
                data = data.drop_duplicates()
                print("Data after dropping duplicates:")
                print(data)
                
                column_list1a = [col1a.strip() for col1a in columns1a.split(',')]
                print("Columns to process:", column_list1a)
                column_list1b = [col1b.strip() for col1b in columns1b.split(',')]
                print("Columns to process:", column_list1b)
                column_list2a = [col2a.strip() for col2a in columns2a.split(',')]
                print("Columns to process:", column_list2a)
                column_list2b = [col2b.strip() for col2b in columns2b.split(',')]
                print("Columns to process:", column_list2b)
                if column_list1a and column_list1b and column_list2a and column_list2b :
                     for col1a in column_list1a:
                          for col1b in column_list1b:
                               for col2a in column_list2a:
                                    for col2b in column_list2b: 
                                        if col1a and col2a in data.columns:
                                                if dataty=='BINT':
                                                     
                                                     col1b=int(col1b)
                                                     col2b=int(col2b)
                                                     if orand=="AND":

                                                     
                                                        d=np.where((data[col1a] == col1b) & (data[col2a] == col2b))[0]
                                                     else:


                                                        d=np.where((data[col1a] == col1b) | (data[col2a] == col2b))[0]
                                                     
                                                elif dataty=='1INT':
                                                     
                                                     col1b=int(col1b)
                                                     if orand=="AND":

                                                     
                                                        d=np.where((data[col1a] == col1b) & (data[col2a] == col2b))[0]
                                                     else:


                                                        d=np.where((data[col1a] == col1b) | (data[col2a] == col2b))[0]

                                                elif dataty=='2INT':
                                                     
                                                     col2b=int(col2b)
                                                     if orand=="AND":

                                                     
                                                        d=np.where((data[col1a] == col1b) & (data[col2a] == col2b))[0]
                                                     else:


                                                        d=np.where((data[col1a] == col1b) | (data[col2a] == col2b))[0]
                                                else:
                                                     if orand=="AND":

                                                     
                                                        d=np.where((data[col1a] == col1b) & (data[col2a] == col2b))[0]
                                                     else:


                                                        d=np.where((data[col1a] == col1b) | (data[col2a] == col2b))[0]
                                                     
                                                
                                                data=data.iloc[d]

                 # Get unique values for each specified column
                
                
                return data
        
      
        
      

        def filter1(self, columns: str, columns1: str) -> pd.DataFrame:

                data_dir = 'filter'
                print("Starting filter process...")
                
                # Load data from CSV
                csv_path = r"D:\dataanalysisproj\dataanalysttool\filter\data.csv"  # Use raw string for Windows path
                data = pd.read_csv(csv_path)
                
                # Log data info
                print(f"Initial data shape: {data.shape}")
                print("Missing values in each column:")
                print(data.isnull().sum())
                
                # Drop rows with NaN values
                data = data.dropna()
                print("Data after dropping NaN values:")
                print(data.head())
                
                # Drop duplicate rows
                data = data.drop_duplicates()
                print("Data after dropping duplicates:")
                print(data.head())
                
                # Process columns
                column_list = [col.strip() for col in columns.split(',')]
                print("Columns to process:", column_list)
                
                column_list1 = [col1.strip() for col1 in columns1.split(',')]
                print("Filter values:", column_list1)
                
                if column_list and column_list1:
                        # Apply filter conditions
                        for col in column_list:
                                if col in data.columns:
                                        for col1 in column_list1:
                                # Filter data based on the condition
                                                filtered_indices = np.where(data[col] == col1)[0]
                                                if filtered_indices.size > 0:

                                                        data = data.iloc[filtered_indices]
                                                else:
                                                        print(f"No match found for column '{col}' with value '{col1}'")
                
                # Return the filtered data
                print("Filtered data shape:", data.shape)
                return data

        