from tkinter import * # import Everything
root=Tk()
root.title('MY BOX GUI')
#root.iconbitmap('car1.ico.ico')
root.geometry("500x300")
my_label1 = Label(root,text="Ram Ram")
my_label2 = Label(root,text="Kaise hai pandit ji !")

my_label1.grid(row=0,column=0)
my_label2.grid(row=2,column=2)
root.mainloop()





