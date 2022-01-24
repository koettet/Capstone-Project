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
    y_df = x_df.pop("y")
    
    return(x_df, y_df)

ds = ws.datasets['heart-data']

x, y = clean_data(ds)

# TODO: Split data into train and test sets.

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=123)

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

    AUC = model.score(x_test, y_test)
    run.log("AUC_weighted", np.float(AUC))

if __name__ == '__main__':
    main()
