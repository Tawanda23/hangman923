import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression #we use this for statistical modelling
from sklearn.model_selection import cross_val_score

df = pd.read_csv('Advertising.csv')

#this prints out the scatterplot to show our findings
sns.scatterplot(data=df, x='TV', y='Sales')
plt.show() #this displays the plot


#this is to create a straight line 

X = df[['TV']].values #dataframe (big X as its another variable)
y = df[['Sales']].values #pd.series
reg = LinearRegression()
reg.fit(X,y)

y_pred = reg.predict(X) #this brings back our scatterplot
plt.figure()
plt.plot(X, y_pred)
plt.show()

#unkown coefficients (y = mx + c)
print(reg.coef_)
print(reg.intercept_)
print(reg.predict(np.array([[100]]))) # this predicts what the sales will be for 100 000


#use cross-validation to evaluate the model
scores = cross_val_score(reg, X.reshape(-1, 1), y, cv=5)

print("Cross-validation scores: {}".format(scores))

#assume the scores is teh array of cross-validation scores
mean_score = np.mean(scores) #with 1.000 being the best fit
sts_score = np.std(scores)

print("Mean cross-validation score: {:.2f}".format(mean_score))
print("standard deviation of cross-validation scores: {:.2f}")
