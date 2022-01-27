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

1. `age` - age in years
2. `sex` - 0 = male; 1 = female 
3. `cp` - chest pain type (4 values)
4. `trestbps` - resting blood pressure
5. `chol` - serum cholestoral in mg/dl
6. `fbs` - fasting blood sugar > 120 mg/dl
7. `restecg` - resting electrocardiographic results (values 0,1,2)
8. `thalach` - maximum heart rate achieved
9. `exang` - exercise induced angina
10. `oldpeak` - ST depression induced by exercise relative to rest
11. `slope` - the slope of the peak exercise ST segment
12. `ca` - number of major vessels (0-3) colored by flourosopy
13. `thal` - 3 = normal; 6 = fixed defect; 7 = reversable defect
14. `target` - 0 = no heart disease present; 1 = heart disease present


Please check Kaggle and the UCI machine learning repository for further details:

https://www.kaggle.com/ronitf/heart-disease-uci

https://archive.ics.uci.edu/ml/datasets/Heart+Disease

Acknowledgements
Creators:

Hungarian Institute of Cardiology. Budapest: Andras Janosi, M.D.
University Hospital, Zurich, Switzerland: William Steinbrunn, M.D.
University Hospital, Basel, Switzerland: Matthias Pfisterer, M.D.
V.A. Medical Center, Long Beach and Cleveland Clinic Foundation: Robert Detrano, M.D., Ph.D.

Donor:
David W. Aha (aha '@' ics.uci.edu) (714) 856-8779


### Task
*TODO*: Explain the task you are going to be solving with this dataset and the features you will be using for it.

The goal is to solve a classification problem to predict the column 'target (0 or 1)' to predict the presence of a heart disease in a patient. 
To predict this all other 13 variables described above will be used as features.
The deployment of the model will be tested with a request using two new dummy observations created by me changing the data of two original observations.

### Access
*TODO*: Explain how you are accessing the data in your workspace.

The data will be downloaded from my git repository if it is not already present in the Azure datastore with the name 'heart-data'.

## Automated ML
*TODO*: Give an overview of the `automl` settings and configuration you used for this experiment

### My used AML configuration:
Task: classification
Early stopping is enabled to shorten the runs.
The column 'target' is set as label column.
The experiment will timeout after 20 minutes.
Five concurrent iterations are allowed. Therefore, the compute cluster should have at least 6 node.
Weighted AUC is used a primary metric to measure the models performance and determine the best run.


### Results
*TODO*: What are the results you got with your automated ML model? What were the parameters of the model? How could you have improved it?

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Hyperparameter Tuning
*TODO*: What kind of model did you choose for this experiment and why? Give an overview of the types of parameters and their ranges used for the hyperparameter search.

I used a logistic regression model for this task. From my experience, this model often performs well in classification tasks and is an established model in the community.
The hyperparameters used and their limitations were the following:

C - Inverse of regularization strength: 0.1 to 1 sampled by uniform distribution
This variable controls the regularization. Smaller values mean a stronger regularization.

max_iter- Maximum number of iterations to converge: 1000 or 10000 randomly picked
The conversion process will only allow this value as maximum number of iterations. This variable can be used to shorten or lengthen the runs.

### Results
*TODO*: What are the results you got with your model? What were the parameters of the model? How could you have improved it?

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Model Deployment
*TODO*: Give an overview of the deployed model and instructions on how to query the endpoint with a sample input.

Currently the data can be provided in the script directly via JSON. This is not very user friendly but good enough to quickly check if the endpoint is functioning as expected.
For a MVP I would create the possibility of reading files as user input like a CSV.

### Sample input:
*These two oberservation were creted by me by using two original observations and changing randomly the values.*

"data ="{
   "data":[
      {
         "age":51,
         "sex":0,
         "cp":1,
         "trestbps":125,
         "chol":301,
         "fbs":1,
         "restecg":1,
         "thalach":160,
         "exang":0,
         "oldpeak":0.3,
         "slope":2,
         "ca":0,
         "thal":2
      },
      {
         "age":57,
         "sex":1,
         "cp":0,
         "trestbps":98,
         "chol":226,
         "fbs":0,
         "restecg":1,
         "thalach":150,
         "exang":0,
         "oldpeak":2.5,
         "slope":2,
         "ca":1,
         "thal":3
      }
   ]
}


## Screen Recording
*TODO* Provide a link to a screen recording of the project in action. Remember that the screencast should demonstrate:
- A working model
- Demo of the deployed  model
- Demo of a sample request sent to the endpoint and its response

### LINK

## Standout Suggestions
*TODO (Optional):* This is where you can provide information about any standout suggestions that you have attempted.

1. Only 13 of the 75 features were used. By including further features we might be able to generate a better performace.
2. For AML only one run was done. By taken these result into account for a second run a better solution might be possible. One option could be to block certrain model types to find a better solution by using the compute power more efficiently. 
3. Only logistic regression was was considererd as custom model. Further HyperDrive runs with other model types could be considered.
4. Instead of weighted AUC other metrics could be used. However, I feel like the AUC is a good pick without knowing more details.
5. The dataset should be grown and upted by further observations. Also before using the model anywhere in the world and for all kind of people, I would check where and how the observations of the dataset were created. This might help to determine the validity of the model for new observations.
