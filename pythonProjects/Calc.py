from tkinter import *

root = Tk()
root.title('Simple Calculator')


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_c_add():
    a = e.get()
    global f_num
    global opp
    opp = 'Addition'
    f_num = int(a)
    e.delete(0, END)


def button_c_minus():
    a = e.get()
    global f_num
    global opp
    opp = 'Subtraction'
    f_num = int(a)
    e.delete(0, END)


def button_c_multiply():
    a = e.get()
    global f_num
    global opp
    opp = 'Multiplication'
    f_num = int(a)
    e.delete(0, END)


def button_c_divide():
    a = e.get()
    global f_num
    global opp
    opp = 'Division'
    f_num = int(a)
    e.delete(0, END)


def button_c_clear():
    e.delete(0, END)


def button_c_equal():
    b = e.get()
    e.delete(0, END)

    if opp == 'Addition':
        e.insert(0, int(f_num) + int(b))
    if opp == 'Subtraction':
        e.insert(0, int(f_num) - int(b))
    if opp == 'Multiplication':
        e.insert(0, int(f_num) * int(b))
    if opp == 'Division':
        if int(b) != 0:
            e.insert(0, int(f_num) / int(b))


frame_1 = LabelFrame(root, text='Espace de Saisie', padx=2, pady=2)
frame_2 = LabelFrame(root, padx=20, pady=20)
e = Entry(frame_1, width=50, borderwidth=5)

button_1 = Button(frame_2, text='1', padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(frame_2, text='2', padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(frame_2, text='3', padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(frame_2, text='4', padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(frame_2, text='5', padx=40, pady=20, command=lambda: button_click(4))
button_6 = Button(frame_2, text='6', padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(frame_2, text='7', padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(frame_2, text='8', padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(frame_2, text='9', padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(frame_2, text='0', padx=40, pady=20, command=lambda: button_click(0))
button_add = Button(frame_2, text='+', padx=40, pady=20, bg='blue', fg='yellow', command=button_c_add)
button_minus = Button(frame_2, text='-', padx=40, pady=20, bg='blue', fg='yellow', command=button_c_minus)
button_multiply = Button(frame_2, text='*', padx=40, pady=20, bg='blue', fg='yellow', command=button_c_multiply)
button_divide = Button(frame_2, text='/', padx=40, pady=20, bg='blue', fg='yellow', command=button_c_divide)
button_clear = Button(frame_2, text='CA', padx=40, pady=20, bg='red', fg='white', command=button_c_clear)
button_equal = Button(frame_2, text='=', padx=40, pady=20, bg='green', fg='white', command=button_c_equal)

frame_1.grid(row=0, column=0)
frame_2.grid(row=1, column=0)
e.grid(row=0, column=0)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_add.grid(row=1, column=3)
button_minus.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)
button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1)
button_equal.grid(row=4, column=2)

root.mainloop()
