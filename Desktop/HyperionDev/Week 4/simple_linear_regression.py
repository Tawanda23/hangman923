import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score

df = pd.read_csv("insurance.csv")

sns.scatterplot(data=df, x='age', y='charges')

plt.show()
