import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error


# Prepare the data for multiple linear regression
df = pd.read_csv('/content/sample_data/spotify-2023.csv', encoding = 'latin')
X = df[['danceability_%', 'valence_%', 'energy_%', 'acousticness_%','instrumentalness_%','liveness_%','speechiness_%']]
y = df['in_spotify_charts']


# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


# Fit a multiple linear regression model
mlr = LinearRegression()
mlr.fit(X_train, y_train)




# Evaluate the model on the test set
y_pred = mlr.predict(X_test)
r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
print('R-squared: {:.3f}'.format(r2))
print('Mean squared error: {:.3f}'.format(mse))
print('Root mean squared error: {:.3f}'.format(rmse))






new_data = pd.DataFrame({'danceability_%': [0], #plug in whatever values of song
                        'valence_%': [0],
                        'energy_%': [0],
                        'acousticness_%': [0],
                        'instrumentalness_%': [0],
                        'liveness_%': [0],
                        'speechiness_%': [0],
                        })


#print("New Data")
#print(new_data)


# Make the prediction using the trained model
predicted_presence = mlr.predict(new_data)


# Print the predicted weight
print("\nPredicted Spotify Chart Presence")
print(predicted_presence)