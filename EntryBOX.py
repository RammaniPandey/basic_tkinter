from tkinter import * # import Everything

root=Tk()
root.title('MY BOX GUI')
#root.iconbitmap('car1.ico.ico')
root.geometry("800x800")

e = Entry(root, width = 30, fg = 'Red')
e.grid(row=0,column=1)

ee = Entry(root, width = 30, fg= 'Red')
ee.grid(row=0,column=2)

def clickme():
    mylabel = Label(root, text= ' Your First Name ' + e.get())
    mylabel.grid(row=3,column=1)
    e.delete(0,END)
     

def click2():
     mylabel = Label(root, text= ' Your Last Name ' + ee.get())
     mylabel.grid(row=3,column=2)
     ee.delete(0,END)

mybutton = Button(root, text = " Name likhiye pandit ji!", fg ='Green',bg ='white',padx=10,pady=10,command = clickme)
mybutton.grid(row=2,column=1)


mybutton = Button(root, text = "Jaati likhiye pandit ji!", fg ='Green',bg ='white',padx=10,pady=10,command = click2)
mybutton.grid(row=2,column=2)

root.mainloop()





