import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression

df = pd.read_csv('Advertising.csv')

#scatterplot  to  see patterns 
sns.scatterplot(data=df, x='Radio', y='Sales')
plt.show()

#creating three independent variables
X = df[['TV', 'Radio', 'Billboard']].values  #creating dataframe object with 3 columns

#create a  dependent variable
y = df['Sales'].values


reg = LinearRegression
model = reg.fit(X, y)

#regression coefficients and intercept
print("Coefficients: ", model.coef_)
print("Intercept: ", model.intercept_)