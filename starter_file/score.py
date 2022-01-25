import json
import pickle
import numpy as np
import pandas as pd
import azureml.train.automl
from sklearn.externals import joblib
from sklearn.linear_model import Ridge
import os
# import onnxruntime

from inference_schema.schema_decorators import input_schema, output_schema
from inference_schema.parameter_types.standard_py_parameter_type import StandardPythonParameterType
from inference_schema.parameter_types.numpy_parameter_type import NumpyParameterType
from inference_schema.parameter_types.pandas_parameter_type import PandasParameterType

sample_input  = pd.DataFrame(
    {"age": pd.Series([0], dtype="int64"), 
     "sec": pd.Series([0], dtype="int64"), 
     "cp": pd.Series([0], dtype="int64"), 
     "trestbps": pd.Series([0], dtype="int64"), 
     "chol": pd.Series([0], dtype="int64"), 
     "fbs": pd.Series([0], dtype="int64"), 
     "restecg": pd.Series([0], dtype="int64"), 
     "thalach": pd.Series([0], dtype="int64"), 
     "exang": pd.Series([0], dtype="int64"), 
     "oldpeak": pd.Series([0.0], dtype="float64"), 
     "ca": pd.Series([0], dtype="int64"), 
     "thal": pd.Series([0], dtype="int64")}
)

sample_output = np.array([0])
outputs = StandardPythonParameterType({'Results':sample_output}) # 'Results' is case sensitive

def init():
#     global sess
#     sess = onnxruntime.InferenceSession(
#         os.path.join(os.getenv("AZUREML_MODEL_DIR"), "model.onnx")
#     )   
    global model
    # Replace filename if needed.
    model_path = os.path.join(os.getenv('AZUREML_MODEL_DIR'), 'outputs/model.pkl')
    # Deserialize the model file back into a sklearn model.
    model = joblib.load(model_path)    
    
    
    
@input_schema('data', sample_input) 
# 'Inputs' is case sensitive
@output_schema(outputs)

def run(input): 
    # the parameters here have to match those in decorator, both 'Inputs' and 
    # 'GlobalParameters' here are case sensitive
    try:
        # data will be convert to target format
        # assert isinstance(data, np.ndarray)
        data = pd.read_json(data)
        result = model.predict(data)
        return result.tolist()
    except Exception as e:
        error = str(e)
        return error
 
