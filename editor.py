from tkinter import *
from tkinter import filedialog,END
import tkinter.scrolledtext as ScrolledText
#Parent
root = Tk(className = " NotePy")

#Functions
def OpenFile():
    OpenFile = filedialog.askopenfile(parent=root,mode='rb', title="Select A Text File to open")
    if OpenFile!=None:
        fileContents = OpenFile.read()
        textArea.insert("1.0", fileContents)
        OpenFile.close()
def Save():
    file = filedialog.asksaveasfile(mode='w')
    if file != None:
        data = textArea.get('1.0', END+'-1c')
        file.write(data)
        file.close()
#Text Areas
textArea = ScrolledText.ScrolledText(root, width=100, height= 80)
menu = Menu(root)
root.config(menu = menu)
fileMenu = Menu(menu)
menu.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="New")
fileMenu.add_command(label="Open",command = OpenFile)
fileMenu.add_command(label="Export",command = Save)
fileMenu.add_separator()
fileMenu.add_command(label="Exit")

helpMenu = Menu(menu)
helpMenu.add_command(label="About")
helpMenu.add_command(label="Guide")

textArea.pack()



#(Optional) keep the window open
root.mainloop()