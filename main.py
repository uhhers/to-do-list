from tkinter import *
from tkinter import ttk
from tkinter import Listbox

mainWindow = Tk()
mainWindow.geometry("450x450+10+10")
ttkWidget = ttk.Notebook(mainWindow)

viewElements = Frame(ttkWidget)
editElements = Frame(ttkWidget)

ttkWidget.add(viewElements, text="View Elements")
ttkWidget.add(editElements, text="Edit Elements")
ttkWidget.pack()

addElementInput = Text(viewElements, height=1, width=15)
addElementInput.pack()

listbox = Listbox(viewElements)
listbox.pack()




mainWindow.mainloop()
