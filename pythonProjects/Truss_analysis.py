from Planar_Truss import *

home = Tk()
home.title('STRUCTURAL ANALYSIS PROGRAM by Neil T. RIGAUD')
home.geometry('520x520')
home.resizable(False, False)
try :
    home.iconbitmap("Valknut.ico")
except:
    pass

bg = PhotoImage(file="bg.png")

my_label = Label(home, image=bg)
my_label.place(x=0, y=0, relwidth=1, relheight=1)

b_1 = Button(home, text='2D_Truss', padx=80, pady=30, bg='light green', font=("Calibri light", 20, 'bold')
             , command=Truss_2D)
b_2 = Button(home, text='3D_Truss', padx=80, pady=30, bg='light green', font=("Calibri light", 20, 'bold')
             , command=Truss_2D)
b_3 = Button(home, text='2D_Frame', padx=75, pady=30, bg='light green', font=("Calibri light", 20, 'bold')
             , command=Truss_2D)
b_4 = Button(home, text='3D_Frame', padx=75, pady=30, bg='light green', font=("Calibri light", 20, 'bold')
             , command=Truss_2D)

b_1.pack(anchor="center")
b_2.pack(anchor="center")
b_3.pack(anchor="center")
b_4.pack(anchor="center")


home.mainloop()
