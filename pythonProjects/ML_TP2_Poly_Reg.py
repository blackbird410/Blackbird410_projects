from tkinter import *
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression


# 1- Dataset creation
n_rows = int(input('Effectif d\'analyse :'))
x, y = make_regression(n_samples=n_rows, n_features=1, noise=10)
y = y + abs(y / 2)
Y = y.reshape(n_rows, 1)  # Reset matrix dimension to (100,1)

X = np.hstack((x, np.ones(x.shape)))  # X matrix definition
X = np.hstack((x ** 2, X))  # Add x^2 column to the matrix
theta = np.random.randn(3, 1)  # theta matrix definition


# 2- Model
def model(X, theta):
    return X.dot(theta)


# 3- Cost function
def cost_f(a, b, t):
    m = len(b)
    return 1 / (2 * m) * np.sum((model(a, t) - b) ** 2)


# 4- Gradient Descent function
def grad(x, y, theta):
    m = len(y)
    return 1 / m * x.T.dot(model(x, theta) - y)


def gradient_descent(a, b, t, l_rate, n_i):
    cost_history = np.zeros(n_i)
    for i in range(0, n_i):
        t = t - (l_rate * grad(a, b, t))
        cost_history[i] = cost_f(a, b, t)
    return t, cost_history


def coef_det(y, pred):
    u = ((y - pred) ** 2).sum()
    v = ((y - y.mean()) ** 2).sum()
    return 1 - u / v


# 5- Model training

# GUI definition
root = Tk()
root.title('Machine Learning Practice')


def popup(variance):
    v = round(float(variance * 100), 3)
    messagebox.showinfo('Performance de la regression', 'Ce modele de regression est performant à ' +
                        str(v) + ' % .')


def button_click(choice):
    if choice == 1:
        plt.scatter(x, y)
        plt.title('Modele de regression quadratique')
        theta_f, cost_hist = gradient_descent(X, Y, theta, l_rate=0.01, n_i=1000)
        predictions = model(X, theta_f)
        plt.scatter(x, predictions, c='r')
        plt.show()

    if choice == 2:
        theta_f, cost_hist = gradient_descent(X, Y, theta, l_rate=0.01, n_i=1000)
        predictions = model(X, theta_f)
        plt.plot(range(1000), cost_hist)
        plt.title("Courbe d'apprentissage de la machine")
        plt.show()

    if choice == 3:
        plt.scatter(x, y)
        plt.show()

    if choice == 4:
        theta_f, cost_hist = gradient_descent(X, Y, theta, l_rate=0.01, n_i=1000)
        predictions = model(X, theta_f)
        popup(coef_det(Y, predictions))


frame_2 = LabelFrame(root, padx=20, pady=20)

button_1 = Button(frame_2, text='1- Entrainer le modele', padx=40, pady=20, fg='blue', command=lambda: button_click(1))
button_2 = Button(frame_2, text='2- Visualiser le cout de l\'algorithme'
                  , padx=40, pady=20, fg='blue', command=lambda: button_click(2))
button_3 = Button(frame_2, text='3-Afficher le nuage de points', padx=40, pady=20, fg='blue',
                  command=lambda: button_click(3))
button_0 = Button(frame_2, text='0- ANNULER', padx=40, pady=20, bg='red', command=exit)
button_4 = Button(frame_2, text='4- C. de Performance', padx=40, pady=20, bg='cyan', command=lambda: button_click(4))

frame_2.grid(row=1, column=0)

button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_0.grid(row=2, column=1)
button_4.grid(row=2, column=0)

root.mainloop()
