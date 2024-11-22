# -*- coding: utf-8 -*-
"""Heart_Disease_Prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1HiRD9-Xzw8ngc5_AJ99JcymX4iT3PoS8

# Importing The Dependencies
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import warnings
warnings.filterwarnings('ignore')

"""# Data Collection and Uploading"""

# Loading the csv data to Pandas DataFrame
heart_data = pd.read_csv('heart_disease_data.csv')

# Print the first five rows of the DataSet
heart_data.head()

# Print the last five rows of the Datase
heart_data.tail()

# number of rows and columns in the Dataset
heart_data.shape

# Getting some info about the Dataset
heart_data.info()

# Cheching for missing valus
heart_data.isnull().sum()

# statistical measures about the data
heart_data.describe()

# Checing the distribution of Target Variables
heart_data['target'].value_counts()

"""1---> Defective Heart

0---> Healthy Heart

Splitting the Features and Target
"""

x = heart_data.drop(columns='target', axis=1)
y = heart_data['target']

print(x)

print(y)

# Splitting the Data Into Train and Test Data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, stratify=y, random_state=2)

print(x.shape, x_train.shape, x_test.shape)

print(y.shape, y_train.shape, y_test.shape)

"""**Model Training**

**Logistic Regression**
"""

model = LogisticRegression()

# Traing LogisticRegression model with Training data
model.fit(x_train, y_train)

"""**Model Evaluation**

**Accuracy Score**
"""

x_train_prediction = model.predict(x_train)
training_data_accuracy = accuracy_score(x_train_prediction, y_train)

print('Accuracy on Training data :', training_data_accuracy)

x_test_prediction = model.predict(x_test)
test_data_accuracy = accuracy_score(x_test_prediction, y_test)

print('Accuracy on Test data :', test_data_accuracy)

"""**Building a Predictive system**"""

input_data = (62,0,2,130,263,0,1,97,0,1.2,1,1,3)


# Change the input data to a numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the numpy array as we aare predicting for only on instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = model.predict(input_data_reshaped)
print(prediction)

if(prediction[0] == 0):
  print('The person does not have a Heart Disease')
else:
  print('The person has Heart Disease')