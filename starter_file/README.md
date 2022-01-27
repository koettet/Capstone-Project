*NOTE:* This file is a template that you can use to create the README for your project. The *TODO* comments below will highlight the information you should be sure to include.

# Prediction of heart disease conditions

*TODO:* Write a short introduction to your project.
This project is about training two models using the AZURE automated machine learning process and a custom LogisticRegression model optimized with HyperDrive to predict heart disease conditions based on 13 variables. Furthermore the best of both models measured by weighted AUC will be deployed and the model endpoint will be used to get a prediction for two new observations.

## Project Set Up and Installation
*OPTIONAL:* If your project has any special installation steps, this is where you should put it. To turn this project into a professional portfolio project, you are encouraged to explain how to set up this project in AzureML.
In order to use the provided scripts the user has to save the by AZURE provided 'config.json' in one folder with both notebooks: 'autoaml.ipynb', 'hyperparameter_tuning.ipynb', the python script: 'train.py' and the dependencies file: 'conda_dependencies.yml'.
The data can be uploaded manually by the user and should be named 'heart-data' in AZURE in that case. Otherwise the script will take care of this.
A compute cluster is also created by the script and named 'compute-cluster'. If the user wants to create his own cluster, this cluster should be named 'compute-cluster' and have at least 6 nodes.

## Dataset

### Overview
*TODO*: Explain about the data you are using and where you got it from.
The project uses the dataset 'Heart Disease UCI' from Kaggle. This dataset originally contained 75 attributes of 303 observations. The data on Kaggle is a subset of 14 of the 75 variables. See below a list of the used variables:

1. age
2. sex
3. cp
4. trestbps
5. chol
6. fbs
7. restecg
8. thalach
9. exang
10. oldpeak
11. slope
12. ca
13. thal
14. target

### Task
*TODO*: Explain the task you are going to be solving with this dataset and the features you will be using for it.

### Access
*TODO*: Explain how you are accessing the data in your workspace.

## Automated ML
*TODO*: Give an overview of the `automl` settings and configuration you used for this experiment

### Results
*TODO*: What are the results you got with your automated ML model? What were the parameters of the model? How could you have improved it?

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Hyperparameter Tuning
*TODO*: What kind of model did you choose for this experiment and why? Give an overview of the types of parameters and their ranges used for the hyperparameter search


### Results
*TODO*: What are the results you got with your model? What were the parameters of the model? How could you have improved it?

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Model Deployment
*TODO*: Give an overview of the deployed model and instructions on how to query the endpoint with a sample input.

## Screen Recording
*TODO* Provide a link to a screen recording of the project in action. Remember that the screencast should demonstrate:
- A working model
- Demo of the deployed  model
- Demo of a sample request sent to the endpoint and its response

## Standout Suggestions
*TODO (Optional):* This is where you can provide information about any standout suggestions that you have attempted.
