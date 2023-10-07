from tkinter import *
from tkinter.ttk import Combobox

student_name = ['john', 'mary', 'peter', 'jane']
student_id = ['gch123', 'gch456', 'gch789', 'gch234']
student_gpa = [8.0, 5.8, 7.0, 6]

def cbb_student_selected(event):
    selected_index = cbb_student.current()
    if selected_index == -1:
        return
    
    name = student_name[selected_index]
    txt_name.delete(0, END)
    txt_name.insert(0, name)
    id = student_id[selected_index]
    txt_id.delete(0, END)
    txt_id.insert(0, id)
    gpa = student_gpa[selected_index]
    txt_gpa.delete(0, END)
    txt_gpa.insert(0, gpa)

Window = Tk()
Window.title("Student mangement")
Window.geometry("500x200")

lbl_students = Label(Window, text="Students")
lbl_students.grid(row=0, column=0, sticky=W, padx=0)

cbb_student = Combobox(Window, width=20)
cbb_student["value"] = student_name
cbb_student.grid(row=1, column=0, sticky=W)
cbb_student.bind("<<ComboboxSelected>>", cbb_student_selected)

lbl_name = Label(Window, text="Name")
lbl_name.grid(row=1, column=1, sticky=W)

txt_name = Entry(Window, width=20)
txt_name.grid(row=1, column=2, sticky=W)

lbl_id = Label(Window, text="ID")
lbl_id.grid(row=2, column=1, sticky=W)

txt_id = Entry(Window,width=20)
txt_id.grid(row=2, column=2, sticky=W)

lbl_gpa = Label(Window, text="Gpa")
lbl_gpa.grid(row=3, column=1, sticky=W)

txt_gpa = Entry(Window, width=20)
txt_gpa.grid(row=3, column=2, sticky=W)

Window.mainloop()


