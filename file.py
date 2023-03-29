from tkinter import *
from tkinter import ttk

window= Tk()

def mouse_click(event):
    print("clicked")
    
label = Label( window, text="Click here")
label.pack()
label.bind( "<Triple-Button-1>", mouse_click )
window.mainloop()