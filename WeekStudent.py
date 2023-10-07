name=[]
gpa=[]

def print_menu():
    print("1. Add a student")
    print("2. Edit a student's GPA")
    print("3. Delete a student")
    print("4. Search name")
    print("5. Search GPA")
    print("6. Print all")
    print("7. QUit")





def student_management(names, gpas):
    while running:
        print_menu()
        choice = int(input("enter your choice: "))
        if choice ==1:
            add_student(names,gpas)
        elif choice == 2:
            edit_gpa(names, gpas)
        elif choice == 3:
            delete_student(names, gpas)
        elif choice == 4:
            search_name(names, gpas)
        elif choice == 5:
            search_gpa(names, gpas)
        elif choice == 6:
            print_all(names, gpas)
        elif choice == 7:
            running = False
        else:
            print("Invalid choice. Please try again")

def Add_student(names, gpas):
    name = input("enter the student's name: ")
    gpa =float(input("enter the student's GPA: "))
    names.append(name)
    gpas.append(gpa)
    print(f'Sutdent {name} added successfully.')

def edit_gpa(names, gpas):
    name = input('Enter student name to edit: ')
    if found_index == -1:
        print(f'Student {name} not found.')
        return
    new_gpa = float(input('Enter new GPA: '))
    gpas[found_index] = new_gpa

def delete_student(names, gpas):
    name = input('enter the student name to delete: ')
    
    found_index = find_student(name, name)
    if found_index != -1:
        names.pop(found_index)
        gpas.pop(found_index)

    print(f'student {name} delete successfully.')

def seach_name(names, gpas):
    name = input('Enter student name to search: ')
    found_index = find_student(names, name) # find index of student with name

    if found_index != -1:
        print('Student found:')
        print(f'Name: {names[found_index]}')
        print(f'GPA: {gpas[found_index]}')

def find_student(names, name):
    for i in range(len(names)):
        if names[i] == name:
            return i

    print(f'Student {name} not found.')
    return -1

def search_gpa(names, gpas):
    gpa = float(input('Enter student GPA to search for: '))

    for i in range(len(gpas)):
        if gpas[i] >= gpa:
            print(f'Name: {names[i]}, GPA: {gpas[i]}')

def print_all(names, gpas):
    for i in range(len(names)):
        print(f'Name: {names[i]}, GPA: {gpas[i]}')
    
    
