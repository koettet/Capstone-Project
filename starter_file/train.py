from sklearn.linear_model import LogisticRegression
import argparse
import os
import numpy as np
from sklearn.metrics import mean_squared_error
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
from azureml.core.run import Run
from azureml.data.dataset_factory import TabularDatasetFactory

ws = Workspace.from_config()

def clean_data(data):
    # Clean and one hot encode data
    x_df = data.to_pandas_dataframe().dropna()
    y_df = x_df.pop("target")
    
    return(x_df, y_df)

# https://github.com/koettet/Capstone-Project/blob/9bc802ff0216f3eb846a883f358593ce7b28c03d/starter_file/heart.csv
# ds = ws.datasets['heart-data']

path = "https://github.com/koettet/Capstone-Project/blob/9bc802ff0216f3eb846a883f358593ce7b28c03d/starter_file/heart.csv"
ds = TabularDatasetFactory.from_delimited_files(path)


x, y = clean_data(ds)

# TODO: Split data into train and test sets.

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=123)
run = Run.get_context()

def main():
    # Add arguments to script
    parser = argparse.ArgumentParser()

    parser.add_argument('--C', type=float, default=1.0, help="Inverse of regularization strength. Smaller values cause stronger regularization")
    parser.add_argument('--max_iter', type=int, default=100, help="Maximum number of iterations to converge")

    args = parser.parse_args()

    run.log("Regularization Strength:", np.float(args.C))
    run.log("Max iterations:", np.int(args.max_iter))

    model = LogisticRegression(C=args.C, max_iter=args.max_iter).fit(x_train, y_train)

    AUC_weighted = roc_auc_score(y_test, model.predict_proba(x_test)[:, 1], average="weighted")
    run.log("AUC_weighted", float(AUC_weighted))

if __name__ == '__main__':
    main()
