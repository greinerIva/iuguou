from tkinter import *
from tkinter.filedialog import asksaveasfile


def save_file():
   f = asksaveasfile(initialfile = 'Untiled.macinton0',
defaultextension=".macinton0",filetypes=[("All Files","*.*"),("Macinton 0","*.macinton0")])

windo = Tk()
windo.title('Macinton 0')
windo.geometry('2048x1024')
btn= Button(windo, text= "Save", command= lambda:save_file())
btn.grid(column=1, row=1)

isok = True
stringsare = 3
code = Entry(windo, width=12)
code.grid(column=1, row=stringsare)
windo.mainloop()