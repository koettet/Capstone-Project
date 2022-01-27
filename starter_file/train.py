from sklearn.linear_model import LogisticRegression
import argparse
import os
import numpy as np
from sklearn.metrics import mean_squared_error, roc_auc_score
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

import pandas as pd
from azureml.core.run import Run
from azureml.core.dataset import Dataset
from azureml.core.workspace import Workspace

def main():  

    run = Run.get_context()

    # Add arguments to script
    parser = argparse.ArgumentParser()

    parser.add_argument('--data_url', type=str, default="https://raw.githubusercontent.com/koettet/Capstone-Project/master/starter_file/heart.csv", help='URL of the dataset to be used')
    parser.add_argument('--C', type=float, default=1.0, help="Inverse of regularization strength. Smaller values cause stronger regularization")
    parser.add_argument('--max_iter', type=int, default=100, help="Maximum number of iterations to converge")

    args = parser.parse_args()

    run.log("Regularization Strength:", np.float(args.C))
    run.log("Max iterations:", np.int(args.max_iter))

    # get data
    dataset = Dataset.Tabular.from_delimited_files(args.data_url)

    # Clean data
    x_df = dataset.to_pandas_dataframe().dropna()    
    y_df = x_df.pop('target')

    # TODO: Split data into train and test sets.
    x_train, x_test, y_train, y_test = train_test_split(x_df, y_df, test_size=0.15, random_state=123)

    model = LogisticRegression(C=args.C, max_iter=args.max_iter).fit(x_train, y_train)

    AUC_weighted = roc_auc_score(y_test, model.predict_proba(x_test)[:, 1], average="weighted")
    # accuracy = model.score(x_test, y_test)
    run.log("AUC_weighted", np.float(AUC_weighted))

    os.makedirs('outputs', exist_ok=True)
    # files saved in the "outputs" folder are automatically uploaded into run history
    joblib.dump(model, 'outputs/model.joblib')

if __name__ == '__main__':
    main()
