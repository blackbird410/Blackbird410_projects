import pandas as pd
import os
from tkinter import *

if os.path.exists('Dataset.csv'):
    pass
# Verify the existence of the dataset file
else:
    dfr = pd.DataFrame([])
    dfr.columns = ['Name', 'First name', 'Age', 'School']
    dfr.to_csv('Dataset.csv')

root = Tk()
root.title('Formulaire de saisie de donnees')

# Assigning each columns to a list
l_names = []
l_f_names = []
l_ages = []
l_schools = []


def button_s():
    """This function saves the data entered in the form and update the list."""

    l_names.append(e_1.get())
    l_f_names.append(e_2.get())
    l_ages.append(e_3.get())
    l_schools.append(e_4.get())

    e_1.delete(0, END)
    e_2.delete(0, END)
    e_3.delete(0, END)
    e_4.delete(0, END)

    my_dict = {'Nom': l_names, 'Prenom': l_f_names, 'Age': l_ages, 'Ecole': l_schools}
    df = pd.DataFrame(my_dict)
    l_data = pd.read_csv('Dataset.csv')

    if 'Unnamed: 0' in l_data.columns:
        l_data.drop('Unnamed: 0', inplace=True, axis=1)

    l_data = pd.concat([l_data, df])
    os.remove('Dataset.csv')
    l_data.to_csv('Dataset.csv')


frame_1 = LabelFrame(root, text='Espace de saisie', padx=50, pady=50, bg='light gray')

label_1 = Label(frame_1, text='Nom :', bg='light gray')
label_2 = Label(frame_1, text='Prenom :', bg='light gray')
label_3 = Label(frame_1, text='Age :', bg='light gray')
label_4 = Label(frame_1, text='Ecole :', bg='light gray')

e_1 = Entry(frame_1, width=50, borderwidth=5, bg='light blue')
e_2 = Entry(frame_1, width=50, borderwidth=5, bg='light blue')
e_3 = Entry(frame_1, width=50, borderwidth=5, bg='light blue')
e_4 = Entry(frame_1, width=50, borderwidth=5, bg='light blue')

button_save = Button(frame_1, text='Enregistrer', padx=20, pady=10, bg='light green', command=button_s)
button_exit = Button(frame_1, text='Annuler', padx=20, pady=10, bg='red', command=exit)

frame_1.grid(row=0, column=0)

label_1.grid(row=1, column=0)
label_2.grid(row=2, column=0)
label_3.grid(row=3, column=0)
label_4.grid(row=4, column=0)

e_1.grid(row=1, column=1)
e_2.grid(row=2, column=1)
e_3.grid(row=3, column=1)
e_4.grid(row=4, column=1)

button_save.grid(row=5, column=0, columnspan=2)
button_exit.grid(row=6, column=0, columnspan=2)

l_data1 = pd.read_csv('Dataset.csv')
print(l_data1)

root.mainloop()
