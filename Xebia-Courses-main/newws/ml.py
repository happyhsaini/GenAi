import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

# Load Data
df = pd.read_csv("headbrain.csv")

X = df['Head Size(cm^3)'].values
y = df['Brain Weight(grams)'].values

# ---------------- NORMAL EQUATION ----------------

mean_x = np.mean(X)
mean_y = np.mean(y)

numer = 0
denom = 0
n = len(X)

for i in range(n):
    numer += (y[i] - mean_y) * (X[i] - mean_x)
    denom += (X[i] - mean_x) ** 2

slope = numer / denom
intercept = mean_y - slope * mean_x

print("Slope:", slope)
print("Intercept:", intercept)

predictions = []
for i in range(n):
    predictions.append(slope * X[i] + intercept)

plt.figure(figsize=(10,6))
plt.scatter(X, y)
plt.plot(X, predictions, 'r')
plt.show()

error = 0
for i in range(n):
    error += (predictions[i] - y[i]) ** 2

mse = error / n
rmse = np.sqrt(mse)

print("MSE:", mse)
print("RMSE:", rmse)

# ---------------- GRADIENT DESCENT ----------------

X = X.reshape(-1,1)
y = y.reshape(-1,1)

minmax = MinMaxScaler()
scale_x = minmax.fit_transform(X)
scale_y = minmax.fit_transform(y)

def gradientDescent(epochs, alpha):
    slope = 0
    inter = 0
    for i in range(epochs):
        y_pred = scale_x * slope + inter
        loss = y_pred - scale_y
        gradSlope = (2/n) * np.dot(loss.T, scale_x)
        gradInter = (2/n) * np.sum(loss)
        slope = slope - alpha * gradSlope
        inter = inter - alpha * gradInter
    return slope, inter

epochs = 7000
alpha = 0.01

slope, inter = gradientDescent(epochs, alpha)

print("New Slope:", slope)
print("New Intercept:", inter)

predictions = []
for i in range(n):
    predictions.append(slope[0][0] * scale_x[i] + inter)

plt.figure(figsize=(10,6))
plt.scatter(scale_x, scale_y)
plt.plot(scale_x, predictions, 'r')
plt.show()







# Your code performs Simple Linear Regression to predict Brain Weight using Head Size. First, it loads the dataset and extracts input (X) and output (y) values. Then it calculates the slope and intercept manually using statistical formulas (Normal Equation method). Using these values, it predicts brain weight with the equation y = mx + c and plots the regression line on the scatter graph. After that, it calculates MSE and RMSE to measure how accurate the predictions are. Finally, it applies Gradient Descent with normalization to iteratively learn slope and intercept again and plots the new fitted line.