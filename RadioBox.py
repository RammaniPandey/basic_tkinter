from tkinter import *
root = Tk()

root.title("")
root.geometry("500x500") 

q = IntVar()
q.get()
q.set('2')

def clickme(value):
    my_label=Label(root, text = value).pack()

Radiobutton(root, text = "Option 1", variable= q, value = 1).pack(anchor='w')
Radiobutton(root, text = "Option 2", variable= q, value = 2).pack(anchor='w')
Radiobutton(root, text = "Option 3", variable= q, value = 3).pack(anchor='w')
Radiobutton(root, text = "Option 4", variable= q, value = 4).pack(anchor='w')


my_label = Label(root, text= q.get())
my_label.pack()

my_button = Button(root, text = "SUBMIT!",command= lambda:clickme(q.get())).pack()

root.mainloop()