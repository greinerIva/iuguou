from tkinter import *
from tkinter.filedialog import asksaveasfile
from keyboard import add_hotkey


def save_file():
    f = asksaveasfile(initialfile = 'Untiled.macinton0',
defaultextension=".macinton0",filetypes=[("All Files","*.*"),("Macinton 0","*.macinton0")])


comms = []
strscode = 1

def newtake(event):
    global strscode, stringsare, windo
    if strscode == 1:
        comms.append(code.get())
    newenter = Entry(windo, width=128)
    newenter.grid(column=1, row=stringsare+1)
    code.grid(column=1, row=stringsare)
    stringsare += 1
    strscode += 1
    newenter.bind('<Return>', newtake)
    return stringsare, strscode
    

stringsare = 1
windo = Tk()
windo.title('Macinton 0')
windo.geometry('2048x1024')

add_hotkey('ctrl + s', save_file, args =())


code = Entry(windo, width=128)
code.grid(column=1, row=stringsare)
code.bind("<Return>", newtake)
windo.mainloop()
