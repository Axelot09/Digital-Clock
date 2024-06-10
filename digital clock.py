# Digital Clock

# Imports

from tkinter import * 
from tkinter.ttk import *
from time import strftime 
  
root = Tk() 
root.title('Digital Clock') 
  
# Defining a 'time' function

def time(): 
    string = strftime('%H:%M:%S %p') 
    lbl.config(text = string) 
    lbl.after(1000, time) 

# Creating a label
   
lbl = Label(root, font = ('calibri', 40, 'bold'), 
            background = 'skyblue', 
            foreground = 'white') 

lbl.pack(anchor = 'center') 
time() 
  
mainloop()        