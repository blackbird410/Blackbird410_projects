import numpy as np
import pandas as pd
import os
from matplotlib import pyplot as plt

data = pd.read_csv("mnist_train.csv")

data = np.array(data)
m, n = data.shape
np.random.shuffle(data)  # shuffle before splitting into dev and training sets

data_dev = data[0:1000].T
Y_dev = data_dev[0]
X_dev = data_dev[1:n]
X_dev = X_dev / 255.

data_train = data[1000:m].T
Y_train = data_train[0]
X_train = data_train[1:n]
X_train = X_train / 255.
_, m_train = X_train.shape


def init_params():
    # Initialize random weights and biases
    W1 = np.random.rand(10, 784) - 0.5
    b1 = np.random.rand(10, 1) - 0.5
    W2 = np.random.rand(10, 10) - 0.5
    b2 = np.random.rand(10, 1) - 0.5
    return W1, b1, W2, b2


def ReLU(Z):
    # Rectified Linear unit activation function for the neutrons
    return np.maximum(Z, 0)


def softmax(Z):
    # Activation function for the second layer
    A = np.exp(Z) / sum(np.exp(Z))
    return A


def forward_prop(W1, b1, W2, b2, X):
    Z1 = W1.dot(X) + b1
    A1 = ReLU(Z1)
    Z2 = W2.dot(A1) + b2
    A2 = softmax(Z2)
    return Z1, A1, Z2, A2


def ReLU_deriv(Z):
    return Z > 0


def one_hot(Y):
    # Defining a 10x10 matrix full of ones
    one_hot_Y = np.zeros((Y.size, Y.max() + 1))
    one_hot_Y[np.arange(Y.size), Y] = 1
    one_hot_Y = one_hot_Y.T

    # We could have just used => return np.ones((Y.size, Y.size))
    return one_hot_Y


def backward_prop(Z1, A1, Z2, A2, W1, W2, X, Y):
    one_hot_Y = one_hot(Y)
    dZ2 = A2 - one_hot_Y
    dW2 = 1 / m * dZ2.dot(A1.T)
    db2 = 1 / m * np.sum(dZ2)
    dZ1 = W2.T.dot(dZ2) * ReLU_deriv(Z1)
    dW1 = 1 / m * dZ1.dot(X.T)
    db1 = 1 / m * np.sum(dZ1)
    return dW1, db1, dW2, db2


def update_params(W1, b1, W2, b2, dW1, db1, dW2, db2, alpha):
    W1 = W1 - alpha * dW1
    b1 = b1 - alpha * db1
    W2 = W2 - alpha * dW2
    b2 = b2 - alpha * db2
    return W1, b1, W2, b2


def get_predictions(A2):
    return np.argmax(A2, 0)


def get_accuracy(predictions, Y):
    print("Predictions      : " + str(predictions) + "\nExpected       :" + str(Y))
    return np.sum(predictions == Y) / Y.size


def gradient_descent(X, Y, alpha, iterations):
    # Optimization algorithm
    W1, b1, W2, b2 = init_params()
    rec_of_perf = []

    for i in range(iterations):
        Z1, A1, Z2, A2 = forward_prop(W1, b1, W2, b2, X)
        # Propagate the loss or deviation through the network
        dW1, db1, dW2, db2 = backward_prop(Z1, A1, Z2, A2, W1, W2, X, Y)
        # Adjusting the weights and biases
        W1, b1, W2, b2 = update_params(W1, b1, W2, b2, dW1, db1, dW2, db2, alpha)

        if i % 50 == 0:
            print("Iteration: ", i)
            predictions = get_predictions(A2)
            perf = get_accuracy(predictions, Y)
            print("Performance      : " + str(round(perf * 100, 3)) + " %")
            print(int(round(perf*100, 0)) * "|")
            print("\n")
            rec_of_perf.append(round(perf*100, 3))

    df = pd.DataFrame(rec_of_perf)
    if os.path.exists("Record_of_Performance.csv"):
        os.remove("Record_of_Performance.csv")
    df.to_csv("Record_of_Performance.csv")

    return W1, b1, W2, b2


def make_predictions(X, W1, b1, W2, b2):
    _, _, _, A2 = forward_prop(W1, b1, W2, b2, X)
    predictions = get_predictions(A2)
    return predictions


def test_prediction(index, W1, b1, W2, b2):
    current_image = X_train[:, index, None]
    prediction = make_predictions(X_train[:, index, None], W1, b1, W2, b2)
    label = Y_train[index]
    print("Prediction: ", prediction)
    print("Label: ", label)

    current_image = current_image.reshape((28, 28)) * 255
    plt.gray()
    plt.imshow(current_image, interpolation='nearest')
    plt.show()

    return prediction[0] == label


W1, b1, W2, b2 = gradient_descent(X_train, Y_train, 0.1, 5000)

l_W1 = []
l_b1 = []
l_W2 = []
l_b2 = []
if os.path.exists("Net_Params.csv"):
    os.remove("Net_Params.csv")

l_W1 = list(W1)
l_W2 = list(W2)
l_b1 = list(b1)
l_b2 = list(b2)

dct = {"W1": l_W1, "b1": l_b1, "W2": l_W2, "b2": l_b2}
df = pd.DataFrame(dct)
print(df)
if os.path.exists("Net_Params.csv"):
    os.remove("Net_Params.csv")
df.to_csv("Net_Params.csv")

success = 0
tampon = 0
for t in range(5):
    tampon = test_prediction(t, W1, b1, W2, b2)
    if tampon:
        success += 1

print("Your algorithm has " + str(success) + " predictions over " + " 5 right.")
p = pd.read_csv("Record_of_Performance.csv")
p = np.array(p['0'])
p_max = max(p)
print("The maximum perfomance is : " + str(p_max) + " %")
