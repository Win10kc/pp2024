
print("Student management system go: ")
print()
#create a list of tuples, where each tuple contains the id, name, and DoB of a student
list_student = [(1, 'Linh', '12/02/2003'), (2, 'Lan', '14/12/2003'), (3, 'May', '18/08/2003'), (4, 'Chung', '14/03/2003'), (5, 'Nguyen', '30/10/2003')]

list_course = [(101, 'Advanced python'), (202, 'Data Structures and Algorithms'), (303, 'Machine Learning'), (404, 'Web Development'), (505, 'AI')]

# List marks
list_mark =[
    [85, 40, 56, 70, 36],  # Linh's marks
    [75, 60, 80, 65, 45],  # Lan's marks
    [90, 70, 85, 78, 60],  # May's marks
    [80, 55, 70, 72, 50],  # Chung's marks
    [95, 80, 92, 88, 70]   # Nguyen's marks
]


#list of ((list information of students, list courses), list mark)
list_student_course_mark = list(zip(list_student, list_course, list_mark))

# Print out
for student_course_mark in list_student_course_mark:
    student, course, marks = student_course_mark
    student_id, student_name, student_DoB = student
    course_id, course_name = course

    print(f"Student ID: {student_id}, Student Name: {student_name}, Student DoB: {student_DoB}")
    print(f"Course ID: {course_id}, Course Name: {course_name}")
    print(f"Marks: {marks}")
    print()

print(f"The list has {len(list_student)} students.")
