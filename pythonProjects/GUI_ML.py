from tkinter import *

root = Tk()
root.title('Machine Learning Practice')

def button_choice(choice):
    if choice == 1:
        plt.scatter(x, y)
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
        plt.plot(x, model(X, theta), c='r')
        plt.show()


frame_2 = LabelFrame(root, padx=20, pady=20)

button_1 = Button(frame_2, text='1- Entrainer le modele', padx=40, pady=20, fg='blue')
button_2 = Button(frame_2, text='2- Visualiser le cout de l\'algorithme'
                  , padx=40, pady=20, fg='blue')
button_3 = Button(frame_2, text='3-Afficher le nuage de points', padx=40, pady=20, fg='blue')
button_4 = Button(frame_2, text='0- ANNULER', padx=40, pady=20, bg='red')

frame_2.grid(row=1, column=0)

button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_4.grid(row=2, column=1)

root.mainloop()
