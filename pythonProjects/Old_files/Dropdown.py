from tkinter import *

root = Tk()
root.title('Checkboxes TP')
root.geometry('400x400')


def ch():
    my_label = Label(root, text=choice.get()).pack()


options = ["Option 1", "Option 2", "Option 3", "Option 4"]
choice = StringVar()
choice.set("No choice")

drop = OptionMenu(root, choice, *options)
drop.pack()

my_button = Button(root, text="Choice", command=ch)
my_button.pack()

root.mainloop()
