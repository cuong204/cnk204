from tkinter import *
from tkinter import messagebox

#Event handlers
def btn_choose_clicked():
    selected_index = list_colors.curselection()
    if len(selected_index) == 0:
        messagebox.showerror('Index Error', 'Please choose a color')
        return
    selected_color = list_colors.get(selected_index)
    window.configure(bg=selected_color)
    
window = Tk()
window.title("Demo listbox")
window.geometry("300x200")

list_colors = Listbox(window, width=20, height=5, selectmode=SINGLE)
list_colors.insert(1, "Red")
list_colors.insert(2, "Green")
list_colors.insert(3, "Blue")
list_colors.insert(4, "Yellow")

list_colors.grid(row=1, column=0)

btn_choose = Button(window, text="Choose", command=btn_choose_clicked)
btn_choose.grid(row=6, column=0)
window.mainloop()
