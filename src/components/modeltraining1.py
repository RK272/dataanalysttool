import pandas as pd
from sklearn.linear_model import LinearRegression, Ridge,Lasso,ElasticNet
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import RobustScaler
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder,StandardScaler

from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.linear_model import LinearRegression, Ridge,Lasso,ElasticNet
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error, explained_variance_score, max_error, median_absolute_error, mean_squared_log_error
import numpy as np
from sklearn.svm import SVR

class modeltrainerclass:

    def trainmodel(self,df,coltype,target,drop_col,colmodel):
        print('rrrrrrrrrrr')
        df=df.dropna()
        print("rithin1")
        column_list = [col.strip() for col in drop_col.split(',')]
        print("Columns to process:", column_list)
        
        dropped_columns = [col for col in column_list if col in df.columns]
        print('eef',dropped_columns)
        if dropped_columns:

            df = df.drop(columns=dropped_columns, axis=1)
        
        print(df)
        print('fffffffff')
        num = [column for column in df.columns if df[column].dtype != "O"]
        cat = [column for column in df.columns if df[column].dtype == "O"]
        #df=df.drop(columns=drop_col,axis=1)
        print('assssssssssss')

        num_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy="constant", fill_value=0)),  # Handle missing values first
        ('robust_scaler', RobustScaler()),  # Apply RobustScaler
        ('standard_scaler', StandardScaler())  # Apply StandardScaler
         ])

# Define the ColumnTransformer
        transformers = [('num', num_pipeline, num)]
        if cat:  # Only add if there are categorical columns
            transformers.append(('cat', OrdinalEncoder(), cat))
        preprocessor = ColumnTransformer(transformers=transformers)

        
        X_transformed = preprocessor.fit_transform(df)
        if cat:
            transformed_columns = list(preprocessor.named_transformers_['cat'].get_feature_names_out(cat))
        else:
            transformed_columns = []

# Convert back to DataFrame
        X_transformed_df = pd.DataFrame(X_transformed, columns=num + transformed_columns)

        y=X_transformed_df[target]
        x=X_transformed_df.drop(columns=target)



       
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
        models={
            'LinearRegression':LinearRegression(),
            'Lasso':Lasso(),
            'Ridge':Ridge(),
            'Elasticnet':ElasticNet(),
            'xgb':GradientBoostingClassifier(),
            'des':DecisionTreeClassifier(),
            'svr':SVR()
        }
        if colmodel=='LinearRegression':
            xgb_clf=models['LinearRegression']
        elif colmodel=='xgb':
            xgb_clf=models['xgb']
        elif colmodel=='des':
            xgb_clf=models['des']
        elif colmodel=='Ridge':
            xgb_clf=models['Ridge']
        elif colmodel=='svr':
            xgb_clf=models['svr']
        else: 
            xgb_clf=models['Lasso']
        
        
        
        model=xgb_clf.fit(x_train, y_train)
        y_pred = model.predict(x_test)
        
        if coltype =='classification':


            conf_matrix = confusion_matrix(y_test, y_pred)
            num_classes = len(set(y_test))  # Or len(conf_matrix)
            class_labels = [f'Class {i}' for i in range(num_classes)]
            conf_matrix_df = pd.DataFrame(conf_matrix, index=[f'Actual {label}' for label in class_labels], columns=[f'Predicted {label}' for label in class_labels])
            class_report_dict = classification_report(y_test, y_pred, output_dict=True)
            class_report_df = pd.DataFrame(class_report_dict).transpose()
            print("ddddddddddddddd")
            print(class_report_df)
            print('eeeeeeee')
            print(conf_matrix_df)
            return conf_matrix_df ,class_report_df
        else:
            metrics = {
            f'Mean Absolute Error (MAE) for {colmodel}': mean_absolute_error(y_test, y_pred),
            f'Mean Squared Error for for {colmodel}': mean_squared_error(y_test, y_pred),
            f'Root Mean Squared Error (RMSE) for {colmodel}': np.sqrt(mean_squared_error(y_test, y_pred)),
            f'R-squared (R²) for {colmodel}': r2_score(y_test, y_pred),
            f'Adjusted R-squared (Adjusted R²) for {colmodel}': 1 - (1 - r2_score(y_test, y_pred)) * (len(y_test) - 1) / (len(y_test) - x_test.shape[1] - 1),
            f'Explained Variance Score for {colmodel}': explained_variance_score(y_test, y_pred),
            f'Max Error for {colmodel}': max_error(y_test, y_pred),
            f'Median Absolute Error for {colmodel}': median_absolute_error(y_test, y_pred)
            }

# Check if the target values contain any negative numbers before adding MSLE
            if np.all(y_test >= 0) and np.all(y_pred >= 0):
                metrics['Mean Squared Logarithmic Error (MSLE) for {colmodel}'] = mean_squared_log_error(y_test, y_pred)

# Convert metrics dictionary to DataFrame
            metrics_df = pd.DataFrame(metrics.items(), columns=['Metric', 'Value'])

            print("Regression Metrics as DataFrame:")
            print(metrics_df)

# Optional: Residual Analysis
            residuals = y_test - y_pred
            residuals_df = pd.DataFrame({'Predicted': y_pred, 'Actual': y_test, 'Residuals': residuals})

            print("\nResiduals DataFrame:")
            print(residuals_df)
            return metrics_df ,residuals_df

        



