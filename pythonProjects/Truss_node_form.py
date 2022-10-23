import pandas as pd
import os
from Truss_classes import *
from tkinter import *

if os.path.exists('Node_list.csv'):
    pass
else:
    b_data = pd.DataFrame([], columns=['Node number', 'Position X', 'Position Y', 'Reaction X', 'Reaction Y'])
    b_data.to_csv('Node_list.csv')
    del b_data


n_data = Tk()
n_data.title('Node entry')
n_data.geometry("490x600")

l_node_num = []
l_x_pos = []
l_y_pos = []
l_x_reaction = []
l_y_reaction = []


def button_s():
    node = TrussNode(int(e_1.get()), float(e_2.get()), float(e_3.get()), bool(v_1.get()), bool(v_2.get()))

    l_node_num.append(node.node_num)
    l_x_pos.append(node.x_pos)
    l_y_pos.append(node.y_pos)
    l_x_reaction.append(node.x_reaction)
    l_y_reaction.append(node.y_reaction)

    e_1.delete(0, END)
    e_2.delete(0, END)
    e_3.delete(0, END)
    c_1.deselect()
    c_2.deselect()

    node_dict = {'Node number': l_node_num, 'Position X': l_x_pos, 'Position Y': l_y_pos,
                 'Reaction X': l_x_reaction, 'Reaction Y': l_y_reaction}
    b_df = pd.DataFrame(node_dict)
    l_data = pd.read_csv('Node_list.csv')

    if 'Unnamed: 0' in b_df.columns:
        b_df.drop('Unnamed: 0', inplace=True, axis=1)
    if 'Unnamed: 0' in l_data.columns:
        l_data.drop('Unnamed: 0', inplace=True, axis=1)

    b_df.to_csv('Node_list.csv')

    l_data = pd.concat([l_data, b_df])
    os.remove('Node_list.csv')
    l_data.to_csv('Node_list.csv')


frame_1 = LabelFrame(n_data, text='Data entry', padx=15, pady=20)

label_1 = Label(frame_1, text='Node number :')
label_2 = Label(frame_1, text='Position X :')
label_3 = Label(frame_1, text='Position Y :')

e_1 = Entry(frame_1, width=50, borderwidth=5, bg='light blue')
e_2 = Entry(frame_1, width=50, borderwidth=5, bg='light blue')
e_3 = Entry(frame_1, width=50, borderwidth=5, bg='light blue')

v_1 = IntVar()
v_2 = IntVar()

c_1 = Checkbutton(frame_1, text='Reaction on the X axis', variable=v_1)
c_2 = Checkbutton(frame_1, text='Reaction on the Y axis', variable=v_2)

button_save = Button(frame_1, text='Submit data', padx=10, pady=10, bg='green', command=button_s)
button_exit = Button(frame_1, text='Exit', padx=10, pady=10, bg='red', command=exit)

frame_1.grid(row=0, column=0, padx=10)

label_1.grid(row=1, column=0)
label_2.grid(row=2, column=0)
label_3.grid(row=3, column=0)

e_1.grid(row=1, column=1)
e_2.grid(row=2, column=1)
e_3.grid(row=3, column=1)

c_1.grid(row=4, column=0)
c_2.grid(row=4, column=1)

button_save.grid(row=5, column=0, columnspan=2, ipadx=170)
button_exit.grid(row=6, column=0, columnspan=2, ipadx=190)

print(pd.read_csv('Node_list.csv'))

n_data.mainloop()
