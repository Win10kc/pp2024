
print("Student management system go: ")
print()

#create a list of tuples, where each tuple contains the id, name, and DoB of a student
list_student = [(1, 'Linh', '12/02/2003'), (2, 'Lan', '14/12/2003'), (3, 'May', '18/08/2003'), (4, 'Chung', '14/03/2003'), (5, 'Nguyen', '30/10/2003')]

list_course = [(101, 'Advanced python'), (202, 'Data Structures and Algorithms'), (303, 'Machine Learning'), (404, 'Web Development'), (505, 'AI')]

#list of (list information of students, list courses)
list_student_course = list(zip(list_student, list_course))

# List marks
list_mark = [(85,), (75,), (90,), (80,), (95,)]

#list of ((list information of students, list courses), list mark)
list_student_course_mark = list(zip(list_student_course, list_mark))

# Print out
for student_course, mark in list_student_course_mark:
    # unpack the nested tuple (list information of students, list courses) into 2 individual
    student, course = student_course 

    # unpack the student tuple
    student_id, student_name, student_DoB = student 

    # unpack the course tuple
    course_id, course_name = course

    # get the first element of the mark tuple
    mark = mark[0] 

    print(f"Student ID: {student_id}, Student Name: {student_name}, Student DoB: {student_DoB}")
    print(f"Course ID: {course_id}, Course Name: {course_name}")
    print(f"Mark: {mark}")
    print()

print("The list has 5 students ")
