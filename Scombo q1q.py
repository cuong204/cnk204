from tkinter import *
from tkinter.ttk import Combobox

### EVENT HANDLERS ###
def cbb_languages_selected(event):
    #clear old text
    txt_language.delete(0, END)
    #insert new text (selected value from combobox)
    txt_language.insert(0, cbb_languages.get())

### Create window & widget ####
Window = Tk()
Window.title("Demo combobox")
Window.geometry("300x200")

cbb_languages = Combobox(Window, width=20)
cbb_languages["value"] = ("Python", "Java", "C#", "C++", "JavaScript")
cbb_languages.grid(row=0, column=0)
cbb_languages.bind("<<ComboboxSelected>>", cbb_languages_selected)

txt_language = Entry(Window, width=20)
txt_language.grid(row=0, column=1)

### Start Program ###
Window.mainloop()