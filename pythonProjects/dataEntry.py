import os
import pandas as pd
import tkinter as tk

from tkinter import *
from tkinter import ttk
from GradientFrame import GradientFrame
from person import Person

if os.path.exists('List.csv'):
    pass
else:
    dataBase = pd.DataFrame([], columns=['No', 'Last Name', 'First Name', 'Age', 'Gender', 'Occupation', 'Address'])
    dataBase.to_csv('List.csv')
    del dataBase

root = Tk()
root.title('Personal info')
root.geometry('470x600')
root['bg'] = '#4dfaf7'
root.resizable(False, False)

gf = GradientFrame(root, colors = ("#34ebe8", "white"), width = 470, height = 600)
gf.config(direction = gf.top2bottom)
gf.pack(fill=BOTH, expand=TRUE)

frame_1 = GradientFrame(gf, 
                        colors=("#34ebe8", "white"),
                        width=445,
                        height=580)
frame_1.config(direction = frame_1.left2right)
frame_1.place(x=10, y=10)

action_frame = Frame(gf, border=0).place(x=25, y=70)


#-------------------FUNCTIONS-------------------

def save():
    g = "Male" if gender.get() == 1 else "Female"

    p = Person(e_1.get(), e_2.get(), int(e_3.get()), g, e_5.get(), e_6.get())

    e_1.delete(0, END)
    e_2.delete(0, END)
    e_3.delete(0, END)
    e_5.delete(0, END)
    e_6.delete(0, END)

    prev_data = pd.read_csv('List.csv')
    n = prev_data.shape[0]

    df = pd.DataFrame({'No': [n + 1], 
                        'Last Name': [p.lastName], 
                        'First Name': [p.firstName], 
                        'Age': [p.age], 
                        'Gender': [p.gender], 
                        'Occupation': [p.occupation], 
                        'Address': [p.address]})

    if 'Unnamed: 0' in prev_data.columns:
        prev_data.drop('Unnamed: 0', inplace=True, axis=1)
    if 'Unnamed: 0' in df.columns:
        df.drop('Unnamed: 0', inplace=True, axis=1)

    print(df)

    prev_data = pd.concat([prev_data, df], ignore_index=True)
    os.remove('List.csv')
    prev_data.to_csv('List.csv')

#-----------------------------------------------

gpx = 40 

# Elements definitions
l_1 = Label(frame_1, text="Last Name :", font="Helvetica 14", bg="#34ebe8").place(x=gpx, y=20)
l_2 = Label(frame_1, text="First Name :", font="Helvetica 14", bg="#34ebe8").place(x=gpx, y=70)
l_3 = Label(frame_1, text="Age :", font="Helvetica 14", bg="#34ebe8").place(x=gpx, y=120)
l_4 = Label(frame_1, text="Gender :", font="Helvetica 14", bg="#34ebe8").place(x=gpx, y=170)
l_5 = Label(frame_1, text="Occupation :", font="Helvetica 14", bg="#34ebe8").place(x=gpx, y=220)
l_6 = Label(frame_1, text="Address :", font="Helvetica 14", bg="#34ebe8").place(x=gpx, y=270)

e_1 = Entry(frame_1, width=40, borderwidth=5, bg='light blue')
e_1.place(x=110 + gpx, y=20)
e_2 = Entry(frame_1, width=40, borderwidth=5, bg='light blue')
e_2.place(x=110 + gpx, y=70)
e_3 = Entry(frame_1, width=40, borderwidth=5, bg='light blue')
e_3.place(x=110 + gpx, y=120)

gender = IntVar()

rb_1 = Radiobutton(frame_1,
               text="Male",
               font="Helvetica 15",
               bg="#34ebe8",
               padx = 20, 
               variable=gender, 
               value=1
               ).place(x=110 + gpx, y=170)
rb_2 = Radiobutton(frame_1, 
               text="Female",
               font="Helvetica 15",
               bg="#34ebe8",
               padx= 20, 
               variable=gender, 
               value=2
               ).place(x=230 + gpx, y=170)

e_5 = Entry(frame_1, width=40, borderwidth=5, bg='light blue')
e_5.place(x=110 + gpx, y=220)
e_6 = Entry(frame_1, width=40, borderwidth=5, bg='light blue')
e_6.place(x=110 + gpx, y=270)

b_1 = Button(action_frame,
            text='SAVE', 
            height=1, 
            font="Helvetica 12", 
            command=save).place(x=130 + gpx, y=320)
b_2 = Button(action_frame, 
            text='RESET', 
            height=1,  
            font="Helvetica 12", 
            command='').place(x=240 + gpx, y=320)


# -----------------TreeView Def-------------------

# ------------------------------------------------

root.mainloop()