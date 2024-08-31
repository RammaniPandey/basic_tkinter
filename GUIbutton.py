from tkinter import * # import Everything
root=Tk()
root.title('MY BOX GUI')
#root.iconbitmap('car1.ico.ico')
root.geometry("500x300")

def my_click():
    my_label = Label(root, text = "Aaya Samjh ho Pandit ji",fg='#900ECA')
    my_label.pack()


mybutton = Button(root, text = "Yha click kari pandit ji !",command= my_click,fg ='#150205',bg ='#CA7A0E',padx=30,pady=30)
mybutton.pack()


root.mainloop()


