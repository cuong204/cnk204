from tkinter import*
from tkinter. ttk import Combobox

window = Tk()
window.title('demo listbox')
window.geometry('300x200')

lbl_book = Label(window, text='book')
lbl_book.grid(row=0, column=0, sticky=W)

cbb_book = Combobox(window, width=20)
# cbb_book['value'] = book_name
cbb_book.grid(row=1, column=0, rowspan= 2, columnspan= 3)
# cbb_book.bind("<<ComboboxSelected>>", )

list_book = list(window, wi)

lbl_name = Label(window, text='name')
lbl_name.grid(row=1, column=2, sticky=W)

txt_name = Entry(window, width= 20)
txt_name.grid(row=1, column=3, columnspan= 2)

              

window.mainloop()