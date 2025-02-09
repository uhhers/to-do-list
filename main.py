from tkinter import *
from tkinter import Listbox, messagebox, ttk
import os
import time
import sys

if getattr(sys, 'frozen', False):
    script_path = os.path.dirname(sys.executable)  # When running as .exe
else:
    script_path = os.path.dirname(os.path.abspath(__file__))  # When running as .py
save_path = os.path.join(script_path, "save.txt")

if not os.path.exists(save_path):
    with open(save_path, "w") as file:
        pass
else:
    pass

mainWindow = Tk()
mainWindow.geometry("450x450+10+10")

def makeActivity():
    with open(save_path, "r") as file:
        stringinput = file.read()
    stringlist = stringinput.split("/")
    stringlist.pop()
    textinbox = addElementInput.get("1.0", END).strip("\n")
        
    if textinbox in stringlist:
        messagebox.showwarning("Element creating", "Elements must not have the same name...")
    elif textinbox == "":
        messagebox.showwarning("Element creating", "You can't create an element with an empty name!")
    else:
        stringlist.append(textinbox)
        stringlist.append("0")    

    with open(save_path, "w") as file:
        for text in stringlist:
            file.write(text + "/")
        file.close()

    addElementViewerListbox.delete(0, END)
    index = 1
    for i in stringlist:
        if i == "0":
            continue
        addElementViewerListbox.insert(index, i)
        index 

def updateList():
    with open(save_path, "r") as file:
        stringinput = file.read()
    stringlist = stringinput.split("/")
    stringlist.pop()
    
    editListbox.delete(0, END)
    index = 1
    for i in stringlist:
        if i == "0":
            continue
        editListbox.insert(index, i)
        index += 1

def getElementInfo():
    with open(save_path, "r") as file:
        stringinput = file.read()
    stringlist = stringinput.split("/")
    stringlist.pop()

    selectedElement = editListbox.curselection()
    if selectedElement:
        selectedElementIndex = selectedElement[0]
        selectedElementTxt = editListbox.get(selectedElementIndex)
        elementNum = stringlist[stringlist.index(selectedElementTxt) + 1] == 1

        messagebox.showinfo("Element Info", f"{selectedElementTxt} [ {"Done" if elementNum else "Undone"} ]")

ttkWidget = ttk.Notebook(mainWindow)
ttkWidget.pack()

mainEditElements = Frame(ttkWidget)
edit1Elements = Frame(mainEditElements)
edit1Elements.pack(side=LEFT)
edit2Elements = Frame(mainEditElements)
edit2Elements.pack(side=RIGHT, expand = TRUE, fill = BOTH)

mainViewElements = Frame(ttkWidget)
view1Elements = Frame(mainViewElements)
view1Elements.pack(side=LEFT)
view2Elements = Frame(mainViewElements)
view2Elements.pack(side=RIGHT, expand = TRUE, fill = BOTH)

ttkWidget.add(mainViewElements, text="View Elements")
ttkWidget.add(mainEditElements, text="Edit Elements")
ttkWidget.pack()

addElementViewerListbox = Listbox(view1Elements, height = 20)
addElementInput = Text(view2Elements, height = 1, width = 20)
addElementButton = Button(view2Elements, command = makeActivity, text = "Add Element", relief=GROOVE, borderwidth = 5 )
editListbox = Listbox(edit1Elements, height = 20)
updateEditButton = Button(edit2Elements, command = updateList, text="Update List", relief=GROOVE, borderwidth = 5 )
infoEditButton = Button(edit2Elements, command = getElementInfo, text = "Element Info", relief = GROOVE, borderwidth = 5 )
toggleEditButton = Button(edit2Elements, text = "Toggle Element", relief = GROOVE, borderwidth = 5)   

addElementViewerListbox.pack()
addElementButton.pack(fill = X)
addElementInput.pack(fill = X)
editListbox.pack()
updateEditButton.pack(fill = X)
infoEditButton.pack(fill = X)



mainWindow.mainloop()
