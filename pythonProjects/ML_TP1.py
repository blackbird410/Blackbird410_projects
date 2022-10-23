import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression


# 1- Dataset creation
x, y = make_regression(n_samples=100, n_features=1, noise=10)
Y = y.reshape(100, 1)

X = np.hstack((x, np.ones(x.shape)))
theta = np.random.randn(2, 1)  # theta matrix definition


# 2- Model
def model(X, theta):
    return X.dot(theta)  # Y = theta * X


# plt.scatter(x, y)
# plt.plot(x, model(X, theta), c='r')
# plt.show()

# 3- Cost function
def cost_f(x_train, y_train, theta):
    m = len(y_train)
    # use of mean squared error here
    return 1/(2*m) * np.sum((model(x_train, theta) - y_train) ** 2)


# 4- Gradient Descent function
def grad(x, y, theta):
    m = len(y)
    return 1 / m * x.T.dot(model(x, theta)- y)


def gradient_descent(x_train, y_train, theta, l_rate, n_i):
    cost_history = np.zeros(n_i)
    for i in range(0, n_i):
        # Updating the weights and biases
        theta = theta - (l_rate * grad(x_train, y_train, theta))
        cost_history[i] = cost_f(x_train, y_train, theta)
    return theta, cost_history


# 5- Model training
plt.scatter(x, y)
theta_f, cost_hist = gradient_descent(X, Y, theta, l_rate=0.01, n_i=1000)
predictions = model(X, theta_f)
plt.plot(x, predictions, c='r')
#plt.plot(range(1000), cost_hist)
# Verify the results
#plt.title("Courbe d'apprentissage de la machine")
plt.show()


def coef_det(y, pred):
    u = ((y - pred)**2).sum()
    v = ((y - y.mean())**2).sum()
    return 1 - u/v


print("\nPerformance : " + str(coef_det(Y, predictions) * 100) + " %")
