from student import Student
import json
def is_roll_exists(roll_no):
    for student in students:
        if student.roll_no == roll_no:
            return True

    return False

def validate_marks(mark):
    if mark >= 0 and mark <= 100:
        return True
    else:
        return False
    
def validate_name(name):
    if name.strip() == "":
        return False
    return True

valid_departments=["CSE","ECE","EEE","MECH","IT"]
def validate_department(dept):
    if dept.upper() in valid_departments:
        return True
    
    return False


def add_student():
    
    while True:
        name=input("Enter student name: ")
        if validate_name(name):
            break
        print("Invalid name. Try again")

    while True:
        try:
            roll_no=int(input("Enter roll number of the student: "))
            if roll_no>0 and not is_roll_exists(roll_no):
                break
            print("Invalid or duplicate roll number.")
        except ValueError:
            print("Roll number must be a number!")


    while True:
        dept=input("Enter department of student: ")
        if validate_department(dept):
            dept=dept.upper()
            break
        print("Invalid department. Try again")

    while True:
        try:
            mark=int(input("Enter mark of the student: "))
            if validate_marks(mark):
                break
            print("Invalid mark, should be between 0 and 100")
        except ValueError:
            print("Mark must be a number")
    
    student = Student(
        name,
        roll_no,
        dept,
        mark)
    students.append(student)
    save_students()
    print("Student added successfully!")

def view_student():
    if len(students)==0:
        print("No student found")
        return
    
    for student in students:
        student.display_details()


def search_student():
    try:
        roll_no = int(input("Enter roll number to search: "))
    except ValueError:
        print("Roll number must be a number")
    for student in students:
        if student.roll_no == roll_no:
            print("Student found !")
            student.display_details()
            return
    print("Student not found")
        

def delete_student():
    try:
        roll_no = int(input("Enter roll number of student: "))
    except ValueError:
        print("Roll number must be a number")
        return   
    for student in students:
        if student.roll_no==roll_no:
            students.remove(student)
            save_students()
            print("Student successfully removed")
            return
    print("student not found")
    return

def update_student():
    try:
        roll_no = int(input("Enter roll number: "))

    except ValueError:
        print("Roll number must be a number!")
        return
    
    for student in students:
        if student.roll_no == roll_no:
            print("Student found")
            print("\nwhat do you want to update?")
            print("1. Name")
            print("2. Department")
            print("3. Mark")

            choice = int(input("Enter your choice:"))

            if choice == 1:
                while True:
                    new_name=input("Enter new name: ")
                    if validate_name(new_name):
                        student.update(new_name)
                        break
                    print("Invalid name. Try again")
            
            elif choice == 2:
                while True:
                    new_dept=input("Enter new dept: ")
                    if validate_department(new_dept):
                        student.update_dept(new_dept.upper())
                        break
                    print("Invalid department")
            
            elif choice == 3:
                while True:
                    try:
                        new_mark=int(input("Enter new mark: "))
                        if validate_marks(new_mark):
                            student.update_mark(new_mark)   
                            break
                        print("Invalid mark. Enter between 0 and 100")
                    except ValueError:
                        print("Mark must be a number")

            save_students()
            print("Student updated successfully!")
            return
   
    print("Student not found")

def save_students():
    student_data = []
    for student in students:
        student_data.append(student.to_dict())
    
    with open("students.json","w") as file:
        json.dump(student_data,file,indent=4)

def load_students():
    try:
        with open("students.json","r") as file:
            data = json.load(file)

            students = []
            for student_data in data:
                student = Student.from_dict(student_data)
                students.append(student)
            return students
    except FileNotFoundError:
        return []
            

students=load_students()
    
while True:
    print("\n>>>>>>>STUDENT MANAGEMENT SYSTEM<<<<<<<<")
    print("1. Add student")
    print("2. View student")
    print("3. Search student")
    print("4. Delete student")
    print("5. Update")
    print("6. Exit")

    choice =input("Enter your choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        view_student()
    elif choice =="3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        update_student()
    elif choice =="6":
        break
    else:
        print("Invalid choice")