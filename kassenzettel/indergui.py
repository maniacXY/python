from tkinter import *
from tkinter import ttk 

window = Tk()
window.title('My Window')
 
window.geometry('500x300')
 
var1 = StringVar()
l = Label(window, bg='green', fg='yellow',font=('Arial', 12), width=10, textvariable=var1)
l.pack()
 
def print_selection():
    value = lb.get(lb.curselection())   
    var1.set(value)  
 
b1 = Button(window, text='print selection', width=15, height=2, command=print_selection)
b1.pack()
 
var2 = StringVar()
var2.set((1,2,3,4))
lb = Listbox(window, listvariable=var2)

list_items = [11,22,33,44]
for item in list_items:
    lb.insert('end', item)
lb.insert(1, 'first')
lb.insert(2, 'second')
lb.delete(2)
lb.pack()
 
window.mainloop()