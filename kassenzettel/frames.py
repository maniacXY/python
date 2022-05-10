from tkinter import *
import glob


root = Tk()
root.title('Model Definition')
root.geometry('{}x{}'.format(600, 600))

# create all of the main containers
center = Frame(root, bg='gray2', width=590, height=590, padx=3, pady=3)

# layout all of the main containers
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

center.grid(row=1, sticky="nsew")

# create the center widgets
center.grid_rowconfigure(0, weight=1)
center.grid_columnconfigure(1, weight=1)

ctr_left = Frame(center, bg='blue', width=295, height=590, padx=50, pady=50)
ctr_right = Frame(center, bg='green', width=295, height=590, padx=70, pady=50)

ctr_left.grid(row=0, column=0, sticky="ns")
ctr_right.grid(row=0, column=2, sticky="ns")

# create right sub widgets
ctr_right.grid_rowconfigure(1, weight=1)
ctr_right.grid_columnconfigure(0, weight=1)

right_top = Frame(ctr_right, bg='yellow', width=295, height=194)
right_center = Frame(ctr_right, bg='red', width=295, height=194)
right_bottom = Frame(ctr_right, bg='purple', width=295, height=194)

right_top.grid(row=0, column=0, sticky="ew")
right_center.grid(row=1, column=0, sticky="ew")
right_bottom.grid(row=2, column=0, sticky="ew")

#


root.mainloop()

 