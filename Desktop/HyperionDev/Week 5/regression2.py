import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression #we use this for statistical modelling
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

df = pd.read_csv('Advertising.csv')

X = df[['TV', 'Radio', 'Billboard']].values

y =  df['Sales'].values

#split data into training and testing data subsets

Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size=0.2, random_state=0)

reg = LinearRegression
model = reg.fit(Xtrain, ytrain)

print("Coefficients:", model.coef_)
print("intercep: ", model.intercept_)
print("Predicted Sales for £100 m00 investment: ", reg.predict(np.array([[100,0,0]])))

#Fit miltiple Linear Regression model to makepredictions
y_pred = reg.predict(Xtest)

#calculating r-squared
R_sq =r2_score(ytest, y_pred)
print("R-squared is ", R_sq)