from math import *
y = int(input("Saisir x0 : "))

def f(x):
    i = 0
    xn = ((2*x + 27) / (3 * (3 * pow(x, 2) - 1))) + (2 * x) / 3
    while abs(x - xn) > 0:
        print("i : ", i, "\t| Xn : ", xn, "\t| x-(f(x)/f'(x)) : ", x)
        i += 1
        x = xn
        xn = ((2*x + 27) / (3 * (3 * pow(x, 2) - 1))) + (2 * x) / 3
    print(xn)
    return xn


print("Valeur : ", f(y))
