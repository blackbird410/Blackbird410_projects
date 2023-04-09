import pandas as pd
import os
from Truss_classes import *
from tkinter import *

if os.path.exists('Load_list.csv'):
    pass
else:
    b_data = pd.DataFrame([], columns=['Node applied', 'Load on X', 'Load on Y'])
    b_data.to_csv('Load_list.csv')
    del b_data


load_data = Tk()
load_data.title('Load entry')
load_data.geometry("475x600")

l_node_app = []
l_x_load = []
l_y_load = []


def button_s():
    load = TrussLoad(int(e_1.get()), float(e_2.get()), float(e_3.get()))

    l_node_app.append(load.node_app)
    l_x_load.append(load.x_load)
    l_y_load.append(load.y_load)

    e_1.delete(0, END)
    e_2.delete(0, END)
    e_3.delete(0, END)

    load_dict = {'Node applied': l_node_app, 'Load on X': l_x_load, 'Load on Y': l_y_load}
    b_df = pd.DataFrame(load_dict)
    l_data = pd.read_csv('Load_list.csv')

    if 'Unnamed: 0' in b_df.columns:
        b_df.drop('Unnamed: 0', inplace=True, axis=1)
    if 'Unnamed: 0' in l_data.columns:
        l_data.drop('Unnamed: 0', inplace=True, axis=1)

    b_df.to_csv('Load_list.csv')

    l_data = pd.concat([l_data, b_df])
    os.remove('Load_list.csv')
    l_data.to_csv('Load_list.csv')


frame_1 = LabelFrame(load_data, text='Data entry', padx=15, pady=20)

label_1 = Label(frame_1, text='Node applied:')
label_2 = Label(frame_1, text='Load on X axis (kip):')
label_3 = Label(frame_1, text='Load on Y axis (kip):')

e_1 = Entry(frame_1, width=50, borderwidth=5, bg='light blue')
e_2 = Entry(frame_1, width=50, borderwidth=5, bg='light blue')
e_3 = Entry(frame_1, width=50, borderwidth=5, bg='light blue')

button_save = Button(frame_1, text='Submit data', padx=10, pady=10, bg='green', command=button_s)
button_exit = Button(frame_1, text='Exit', padx=10, pady=10, bg='red', command=exit)

frame_1.grid(row=0, column=0, padx=10)

label_1.grid(row=1, column=0)
label_2.grid(row=2, column=0)
label_3.grid(row=3, column=0)

e_1.grid(row=1, column=1)
e_2.grid(row=2, column=1)
e_3.grid(row=3, column=1)

button_save.grid(row=4, column=0, columnspan=2, ipadx=100)
button_exit.grid(row=5, column=0, columnspan=2, ipadx=123)

print(pd.read_csv('Load_list.csv'))

load_data.mainloop()
