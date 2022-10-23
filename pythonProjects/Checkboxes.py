from tkinter import *

root = Tk()
root.title('Checkboxes TP')
root.geometry('400x400')

value = IntVar()


def checkbox_value():
    if value.get():
        my_label = Label(root, text='There is a restraint.').pack()
    else:
        my_label = Label(root, text='There is no restraint.').pack()


c_1 = Checkbutton(root, text='No restraint', variable=value)
c_1.pack()

b = Button(root, text='Verify restraint', command=checkbox_value)
b.pack()

root.mainloop()
