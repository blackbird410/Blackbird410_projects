from tkinter import *

def screen():
    global screen
    global im
    screen = Tk()
    screen.title("Welcome")
    screen.geometry("300x250")
    screen.resizable(0, 0)
    screen.config()

    #----------------------------------------
    ph = PhotoImage(file="Dev.gif")
    im = Label(screen, image=ph)
    im.pack(fill=BOTH, expand=TRUE)
#---------------[TEST Label bg=...]------------------------
    tl = Label(text="Hello world", compound="bottom")     #<-----The one on the screenshot
    tl.pack(in_=im, side="bottom")
#----------------------------------------------------------

    login = Button(screen, text="Login", width="17", height="1", relief=GROOVE, command='')
    login.pack(side="right", in_=im, padx=10)

    registrate = Button(screen, text="Registrate", width="17", height="1", relief=GROOVE , command='')
    registrate.pack(anchor="center",side="left", in_=im, padx=10)
    

    screen.mainloop()

screen()