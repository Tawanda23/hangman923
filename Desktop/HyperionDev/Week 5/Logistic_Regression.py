import pandas as pd
from sklearn.linear_model import LogisticRegression


#extract predictor variables and target

df['Buy'] = df['Buy'].map({'No': 0, 'Yes': 1})

X = df.drop('Allowance', axis=1)
y = df['Buy']

clf = Log