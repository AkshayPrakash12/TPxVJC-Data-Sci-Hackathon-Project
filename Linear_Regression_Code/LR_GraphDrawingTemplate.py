import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv('../Datasets/spotify-2023.csv', encoding='latin')

value_here = 0 #to make ref not return error
# Fit a simple linear regression model to predict weight from height
X = df[f'{value_here}'].values.reshape(-1, 1)
y = df[f'{value_here}'].values.reshape(-1, 1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
lr = LinearRegression()
lr.fit(X_train, y_train)

# Visualize the data and the regression line
plt.scatter(X, y)
plt.plot(X, lr.predict(X), color='red')
plt.xlabel('[Y value]')
plt.ylabel('[Y value]')
plt.title('Simple Linear Regression: [X value] vs. [Y value]')
plt.show()

# Interpret the coefficients of the model
print('Intercept:', lr.intercept_)
print('Coefficient:', lr.coef_)