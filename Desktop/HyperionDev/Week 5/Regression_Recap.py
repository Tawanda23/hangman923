# Problem

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from sklearn.linear_model import LogisticRegression

df = pd.read_csv('diabetes.csv')

sns.scatterplot(data=df, x='Glucose', y='Outcome')
plt.show()

X = df[['Glucose']].values
y = df['Outcome'].values 

#Multiple Linear Reg

#Here we find the independent and dependant variables
X = df[['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']].values
y = df['Outcome'].values

#Fitting the logistic Regression
clf = LogisticRegression().fit(X, y)

print("Coefficients: ", clf.coef_)
print("Intercept:", clf.intercept_)

#Making a prediction
y_pred= clf.predict([0, 180, 70, 23, 94, 31, 0.351, 45])
print("Outcome:" , y_pred)