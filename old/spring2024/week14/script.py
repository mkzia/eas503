
import pandas as pd
import numpy as np
import os

df = pd.read_csv('housing.csv')



df["income_cat"] = pd.cut(df["median_income"],
                               bins=[0., 1.5, 3.0, 4.5, 6., np.inf],
                               labels=[1, 2, 3, 4, 5])

df["income_cat"].value_counts().sort_index().plot.bar(rot=0, grid=True)

from sklearn.model_selection import train_test_split
train, test = train_test_split(df, test_size=0.3, stratify=df['income_cat'], random_state=42)
train.drop('income_cat', axis=1, inplace=True)
test.drop('income_cat',  axis=1, inplace=True)

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.base import BaseEstimator, TransformerMixin

class Preprocessor(BaseEstimator, TransformerMixin): 
    # Train our custom preprocessors 
    numerical_columns = [
        'longitude', 
        'latitude', 
        # 'housing_median_age', 
        # 'total_rooms',
        # 'total_bedrooms', 
        # 'population', 
        # 'households', 
        'median_income', 
    ]
    categorical_columns = [
        'ocean_proximity'
    ]
    
    def fit(self, X, y=None): 

        # Create and fit simple imputer
        self.imputer = SimpleImputer(strategy='median')
        self.imputer.fit(X[self.numerical_columns])
        
        # Create and fit Standard Scaler 
        self.scaler = StandardScaler()
        self.scaler.fit(X[self.numerical_columns]) 
        
        # Create and fit one hot encoder
        self.onehot = OneHotEncoder(handle_unknown='ignore')
        self.onehot.fit(X[self.categorical_columns])
        
        return self 

    def transform(self, X): 
        
        # Apply simple imputer 
        imputed_cols = self.imputer.transform(X[self.numerical_columns])
        onehot_cols = self.onehot.transform(X[self.categorical_columns])
        
        # Copy the df 
        transformed_df = X.copy()
         
        # Apply transformed columns
        transformed_df[self.numerical_columns] = imputed_cols
        transformed_df[self.numerical_columns] = self.scaler.transform(transformed_df[self.numerical_columns])        
        
        # Drop existing categorical columns and replace with one hot equivalent
        transformed_df = transformed_df.drop(self.categorical_columns, axis=1) 
        transformed_df[self.onehot.get_feature_names_out()] = onehot_cols.toarray().astype(int)
        
        return transformed_df
    

from sklearn.pipeline import make_pipeline
from sklearn.ensemble import RandomForestRegressor
rfr = make_pipeline(Preprocessor(), RandomForestRegressor())
y_train = train['median_house_value']
X_train = train.drop([
        'median_house_value', 
        # 'longitude',
        # 'latitude',
        'housing_median_age',
        'population',
        'total_rooms',
        'total_bedrooms',
        'households',
    ], axis=1)
rfr.fit(X_train, y_train)

params = rfr.get_params()

from sklearn.metrics import root_mean_squared_error, mean_absolute_error, r2_score

y_test = test['median_house_value']
X_test = test.drop([
        'median_house_value', 
        # 'longitude',
        # 'latitude',
        'housing_median_age',
        'population',
        'total_rooms',
        'total_bedrooms',
        'households',
    ], axis=1)

y_test_hat=rfr.predict(X_test)
rm2e = root_mean_squared_error(y_test, y_test_hat)
mae = mean_absolute_error(y_test, y_test_hat)
print(mae)
print(r2_score(y_test, y_test_hat))

# import mlflow
# from mlflow.models import infer_signature

# MLFLOW_TRACKING_URI="http://127.0.0.1:8080"
# # Set our tracking server uri for logging
# mlflow.set_tracking_uri(uri=MLFLOW_TRACKING_URI)

# # Create a new MLflow Experiment
# mlflow.set_experiment("predict_median_house_pricing")

# # Start an MLflow run
# with mlflow.start_run():
#     # Log the hyperparameters
#     mlflow.log_params(params)

#     # Log metrics
#     mlflow.log_metric("root_mean_squared_error", rm2e)
#     mlflow.log_metric("mean_absolute_error", mae)

#     # Set a tag that we can use to remind ourselves what this run was for
#     mlflow.set_tag("Training Info", "RandomForestRegressor model for housing data, n_estimators=50")

#     # Infer the model signature
#     signature = infer_signature(X_train, rfr.predict(X_train))

#     # Log the model
#     model_info = mlflow.sklearn.log_model(
#         sk_model=rfr,
#         artifact_path="housing_model",
#         signature=signature,
#         input_example=X_train,
#         registered_model_name="rfr_n_estimators_50",
#     )