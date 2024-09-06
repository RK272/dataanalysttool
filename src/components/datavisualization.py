import matplotlib.pyplot as plt
import os
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd




class datavisualizations:
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

                data = data.drop(columns=dropped_columns, errors='ignore')
            if not os.path.exists(data_dir):
                os.makedirs(data_dir)
        # Save the modified DataFrame
            data.to_csv("droped/data_dropped.csv", index=False)
           
            print("++++++++++++++++++++")
            return data
    def create_barplots(self, df):
            save_dir = 'plots'
            print("harhar")
    
    # Selecting numerical and categorical features
            num_features = [column for column in df.columns if df[column].dtype != "O"]
            df_num = df[num_features]
    
            cat_features = [column for column in df.columns if df[column].dtype == "O"]
            df_cat = df[cat_features]
            if df_num.empty or df_cat.empty:
                print("No plots created. Either no numerical or no categorical data found in the DataFrame.")
                return  # Exit the function if either DataFrame is empty
    
    # Correct directory path
            barplot_dir = os.path.join(save_dir, 'barplots')
    
    # Uncomment to ensure directory is created
            os.makedirs(barplot_dir, exist_ok=True)
    
            print("maha")
    
    # Loop through categorical and numerical columns
            for x_col in df_cat.columns:
                for y_col in df_num.columns:
            # Create a bar plot for each combination of x and y
                    plt.figure(figsize=(8, 6))
            
            # Correcting the bar plot logic to group by categorical
                    y_values = df.groupby(x_col)[y_col].sum()
                    plt.bar(y_values.index, y_values.values, color='g')
            
                    plt.title(f'Bar Plot for {x_col} vs {y_col}')
                    plt.xlabel(x_col)
                    plt.ylabel(f'Sum of {y_col}')
                    plt.xticks(rotation=90)
            
            # Save the plot with a meaningful filename
                    plt.savefig(os.path.join(barplot_dir, f'bar_plot_{x_col}_vs_{y_col}.png'))
                    plt.close()

            print(f"Bar plots saved in the directory: {barplot_dir}")
    def create_histplots(self, df):
        save_dir = 'plots'
        barplot_dir = os.path.join(save_dir, 'hplots')
        os.makedirs(barplot_dir, exist_ok=True)

# Select numeric columns
        num_features = [column for column in df.columns if df[column].dtype != "O"]
        df_numeric = df[num_features]

# Iterate through numeric columns to create histograms
        for column in num_features:
            plt.figure(figsize=(8, 6))
    
    # Plot histogram for each column
            plt.hist(df_numeric[column], bins=30, edgecolor='black')
    
            plt.title(f'Histogram Plot for {column}')
            plt.xlabel(column)
            plt.ylabel('Count')
            plt.xticks(rotation=90)
    
    # Save the plot with a meaningful filename
            plt.savefig(os.path.join(barplot_dir, f'histogram_{column}.png'))
            plt.close()

        print(f"Histograms saved in the directory: {barplot_dir}")

    def create_hist2plots(self, df):
        save_dir = 'plots'
        barplot_dir = os.path.join(save_dir, 'h2plots')
        os.makedirs(barplot_dir, exist_ok=True)

# Select numeric columns
        num_features = [column for column in df.columns if df[column].dtype != "O"]
        df_numeric = df[num_features]

# Iterate through numeric columns to create histograms
        for column in num_features:
            plt.figure(figsize=(8, 6))
    
    # Plot histogram for each column using seaborn histplot
            sns.histplot(df_numeric[column], bins=30, kde=True, edgecolor='black')
    
            plt.title(f'Histogram Plot for {column}')
            plt.xlabel(column)
            plt.ylabel('Count')
            plt.xticks(rotation=90)
    
    # Save the plot with a meaningful filename
            plt.savefig(os.path.join(barplot_dir, f'histogram_{column}.png'))
            plt.close()

        print(f"Histograms saved in the directory: {barplot_dir}")
    
    def create_boxplots(self, df):
        save_dir = 'plots'
        barplot_dir = os.path.join(save_dir, 'boxplots')
        os.makedirs(barplot_dir, exist_ok=True)


        num_features = [column for column in df.columns if df[column].dtype != "O"]
        df_numeric = df[num_features]

        for column in num_features:
            plt.figure(figsize=(8, 6))
    

            
            sns.boxplot(df_numeric[column])
    
            plt.title(f'box Plot for {column}')
            plt.xlabel(column)
            plt.ylabel('Count')
            plt.xticks(rotation=90)
    

            plt.savefig(os.path.join(barplot_dir, f'histogram_{column}.png'))
            plt.close()

        print(f"Histograms saved in the directory: {barplot_dir}")

    def create_heatplots(self, df):
        num_features = [column for column in df.columns if df[column].dtype != "O"]
        df = df[num_features]
        save_dir = 'plots'
        barplot_dir = os.path.join(save_dir, 'heatplots')
        os.makedirs(barplot_dir, exist_ok=True)
        try:
            corr = df.corr()
            plt.figure(figsize=(10, 8))
            sns.heatmap(corr, annot=True, cmap='coolwarm')
            plt.title('Correlation Heatmap')
            plt.savefig(os.path.join(barplot_dir, 'correlationmat.png'))
            plt.close()
            print(f"Correlation heatmap saved in the directory: {barplot_dir}")
        except Exception as e:
            print(f"An error occurred: {e}")
    def create_countplots(self, df):
        save_dir = 'plots'
        barplot_dir = os.path.join(save_dir, 'countplots')
        os.makedirs(barplot_dir, exist_ok=True)


        num_features = [column for column in df.columns if df[column].dtype == "O"]
        df_numeric = df[num_features]

        for column in num_features:
            plt.figure(figsize=(8, 6))
    

            
            sns.countplot(df_numeric[column])
    
            plt.title(f'count Plot for {column}')
            plt.ylabel(column)
            plt.xlabel('Count')
            plt.xticks(rotation=90)
    

            plt.savefig(os.path.join(barplot_dir, f'histogram_{column}.png'))
            plt.close()

        print(f"Histograms saved in the directory: {barplot_dir}")

    def create_piechart(self, df):
        save_dir = 'plots'
        barplot_dir = os.path.join(save_dir, 'pieplots')
        os.makedirs(barplot_dir, exist_ok=True)


        num_features = [column for column in df.columns if df[column].dtype == "O"]
        df_numeric = df[num_features]

        for column in num_features:
            plt.figure(figsize=(8, 6))
    

            
            df_numeric[column].value_counts().plot(kind="pie",autopct='%.2f')
    
            plt.title(f'pie chart for {column}')
            
    

            plt.savefig(os.path.join(barplot_dir, f'histogram_{column}.png'))
            plt.close()

        print(f"Histograms saved in the directory: {barplot_dir}")
    
    def create_scatterplots(self, df):
        save_dir = 'plots'
        print("harhar")

# Correct the directory path construction
        barplot_dir = os.path.join(save_dir, 'scplots')

# Uncomment this line to ensure the directory is created
        os.makedirs(barplot_dir, exist_ok=True)

# Filter numeric columns
        num_feature = [column for column in df.columns if df[column].dtype != "O"]
        df = df[num_feature]
        print("maha")

# Loop through combinations of columns
        for i, x_col in enumerate(df.columns):
            for y_col in df.columns[i + 1:]:
        # Create a scatter plot for each combination of x and y
                plt.figure(figsize=(8, 6))
        
        # Pass the column data correctly using keyword arguments
                sns.scatterplot(x=df[x_col], y=df[y_col])
        
                plt.title(f'Scatter Plot for {x_col} vs {y_col}')
                plt.xlabel(x_col)
                plt.ylabel(y_col)
                plt.xticks(rotation=90)
        
        # Save the plot with a meaningful filename
                plt.savefig(os.path.join(barplot_dir, f'scatter_plot_{x_col}_vs_{y_col}.png'))
                plt.close()

        print(f"Scatter plots saved in the directory: {barplot_dir}")


    

    def create_scatter2plots(self, df):
        save_dir = 'plots'
        print("harhar")

# Correct the directory path construction
        barplot_dir = os.path.join(save_dir, 'sc2plots')

# Uncomment this line to ensure the directory is created
        os.makedirs(barplot_dir, exist_ok=True)

# Filter numeric columns
        num_feature = [column for column in df.columns if df[column].dtype != "O"]
        df = df[num_feature]
        print("maha")

# Loop through combinations of columns
        for i, x_col in enumerate(df.columns):
            for y_col in df.columns[i + 1:]:
        # Create a scatter plot for each combination of x and y
                plt.figure(figsize=(8, 6))
        
        # Pass the column data correctly using keyword arguments
                sns.scatterplot(x=df[x_col], y=df[y_col])
        
                plt.title(f'Scatter Plot for {x_col} vs {y_col}')
                plt.xlabel(x_col)
                plt.ylabel(y_col)
                plt.xticks(rotation=90)
        
        # Save the plot with a meaningful filename
                plt.savefig(os.path.join(barplot_dir, f'scatter_plot_{x_col}_vs_{y_col}.png'))
                plt.close()

        print(f"Scatter plots saved in the directory: {barplot_dir}")


        
    def create_boxplots2(self, df):
        save_dir = 'plots'
        print("harhar")

# Selecting numerical and categorical features
        num_features = [column for column in df.columns if df[column].dtype != "O"]
        df_num = df[num_features]

        cat_features = [column for column in df.columns if df[column].dtype == "O"]
        df_cat = df[cat_features]

# Check if either DataFrame is empty and exit function if true
        if df_num.empty or df_cat.empty:
            print("No plots created. Either no numerical or no categorical data found in the DataFrame.")
            return

# Correct directory path for saving box plots
        boxplot_dir = os.path.join(save_dir, 'boxplots2')
        os.makedirs(boxplot_dir, exist_ok=True)

        print("maha")

# Loop through categorical and numerical columns
        for x_col in df_cat.columns:
            for y_col in df_num.columns:
        # Create a box plot for each combination of x and y
                plt.figure(figsize=(8, 6))

        # Using seaborn's boxplot with categorical x and numerical y
                sns.boxplot(x=df[x_col], y=df[y_col])

                plt.title(f'Box Plot for {x_col} vs {y_col}')
                plt.xlabel(x_col)
                plt.ylabel(y_col)
                plt.xticks(rotation=90)

        # Save the plot with a meaningful filename
                plt.savefig(os.path.join(boxplot_dir, f'box_plot_{x_col}_vs_{y_col}.png'))
                plt.close()

        print(f"Box plots saved in the directory: {boxplot_dir}")
