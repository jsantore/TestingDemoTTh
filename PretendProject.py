import  sqlite3
from typing import Tuple
import student
'''
this file contains a bunch of functions to be tested. Many of them have very naive implementations and should be 
 fixed. But our set of good tests will show us that.'''

grade_map = {"A":4.0,
             "A-":3.7,
             "B+":3.3,
             "B":3.0,
             "B-":2.7,
             "C+":2.3,
             "C":2.0,
             "C-":1.7,
             "D+":1.3,
             "D":1.0,
             "D-":0.7,
             "F":0}

def open_db(filename:str)->Tuple[sqlite3.Connection, sqlite3.Cursor]:
    #connect to exiting database or create new one
    db_connection = sqlite3.connect(filename)
    #get ready to read/write data
    cursor = db_connection.cursor()
    return db_connection, cursor


def close_db(connection:sqlite3.Connection):
    #make sure any changes get saved
    connection.commit()
    connection.close()


# def update_gpa(student_rec:student.Student, grade:str, course_credits:int)->student.Student:
#     #first some basic error checking
#     if grade.upper() not in grade_map:
#         raise ValueError("grade must be a letter grade from A to F")
#     #oh no!!! this might be a problem
#     new_gpa = student_rec.gpa+grade_map[grade.upper()]/student_rec.credits+course_credits
#     student_rec.gpa = new_gpa
#     return student_rec


def update_gpa(student_rec:student.Student, grade:str, course_credits:int)->student.Student:
    #first some basic error checking
    if grade.upper() not in grade_map:
        raise ValueError("grade must be a letter grade from A to F")
    #oh no!!! this might be a problem
    new_gpa = (student_rec.gpa*student_rec.credits+grade_map[grade.upper()]*course_credits)/(student_rec.credits+course_credits)
    student_rec.gpa = new_gpa
    return student_rec


def add_student(cursor:sqlite3.Cursor, student_rec:student.Student):
    cursor.execute(f'''INSERT INTO STUDENTS (first_name, last_name, gpa, credits)
                   VALUES ("{student_rec.first_name}", "{student_rec.last_name}", {student_rec.gpa}, {student_rec.credits})''')

def find_student(cursor:sqlite3.Cursor, banner_id:int)->student.Student:
    '''A Naive implementation of a find method, works in the happy path'''
    select_cursor = cursor.execute(f'''SELECT * FROM STUDENTS WHERE banner_id={banner_id}''')
    results = select_cursor.fetchall()
    #we only expect one item back here
    student_data = results[0]
    found_student = student.Student(student_data[1], student_data[2], student_data[3], student_data[4], student_data[0])
    return found_student





def main():
    conn, cursor = open_db("demo_db.sqlite")
    close_db(conn)



if __name__ == '__main__':
    main()