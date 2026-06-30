import sqlite3

def get_connection():
    connection = sqlite3.connect("students.db")
    return connection

def create_table():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        roll_no INTEGER UNIQUE,
        dept TEXT,
        mark INTEGER
    )
    """)

    connection.commit()
    connection.close()

create_table()

def add_student(student):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO students(name, roll_no,dept, mark)
        VALUES(?,?,?,?)
        """,
        (
           student.name,
           student.roll_no,
           student.dept,
           student.mark
        )
    )

    connection.commit()
    connection.close()

from student import Student
def get_all_students():
    connection = get_connection
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    
    connection.close()
    students = []
    for row in rows:
        student = Student.from_row(row)
        students.append(student)
    return students
