# Heart_Disease_Prediction
This project is a machine learning-based system designed to predict the likelihood of heart disease 
in an individual based on various medical parameters. 
It uses logistic regression to classify individuals as either having heart disease or not, based on the given input data.

**Table of Contents**
1.  Overview
2.  Features
3.  Technologies Used
4.  Dataset
5.  Model Evaluation
6.  Installation
7.  Usage
8.  Contributing
9.  License

**Overview**
Heart disease is a major health concern, and early detection can help mitigate risks. 
This project implements a logistic regression model to predict heart disease using features like cholesterol levels, resting blood pressure, and more.

**Features**
Preprocessing and visualization of the dataset to explore insights.
Splitting the data into training and testing sets.
Training a logistic regression model for prediction.
Evaluation of the model's accuracy on both training and test datasets.
A predictive system to determine heart disease likelihood for new data.

**Technologies Used**

==>  **Python**

==>  **Libraries:**
Pandas
NumPy
Matplotlib
Seaborn
Scikit-learn

**Dataset**

The dataset used for this project is heart_disease_data.csv, which contains the following features:

==> Age, sex, chest pain type, resting blood pressure, serum cholesterol, fasting blood sugar, 
resting ECG results, maximum heart rate, exercise-induced angina, and more.

==> Target variable
0 - No heart disease
1 - Heart disease


**Model Evaluation**
Accuracy on Training Data: ~[insert_accuracy]%
Accuracy on Test Data: ~[insert_accuracy]%
The training accuracy indicates how well the model fits the training data, 
while the test accuracy reflects the model's ability to generalize to unseen data. 
Achieving comparable scores ensures that the model is neither overfitting nor underfitting.

**Installation**
1.  Clone this repository:
   https://github.com/HiteshGupta03/Heart_Disease_Prediction.git

2.  Navigate to the project directory:
  cd heart-disease-prediction

3.  Install the required libraries:
   pip install -r requirements.txt


**Usage**
1.  Run the script to train and evaluate the model:
   python heart_disease_prediction.py

2.  Use the predictive system by providing custom input data in the script under the input_data variable.
 
 Example Input:
input_data = (62, 0, 2, 130, 263, 0, 1, 97, 0, 1.2, 1, 1, 3)



**Contributing**
Contributions are welcome! 
If you have any ideas or enhancements, please create a pull request or open an issue.


**License**
This project is licensed under the MIT License. See the LICENSE file for details.

























