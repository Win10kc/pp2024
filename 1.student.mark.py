
print("Student management system go: ")
print()

#create a list of dictionaries, where each dictionary contains student information
list_student = [
    {'id': 1, 'name': 'Linh', 'DoB': '12/02/2003'},
    {'id': 2, 'name': 'Lan', 'DoB': '14/12/2003'},
    {'id': 3, 'name': 'May', 'DoB': '18/08/2003'},
    {'id': 4, 'name': 'Chung', 'DoB': '14/03/2003'},
    {'id': 5, 'name': 'Nguyen', 'DoB': '30/10/2003'}
]

#create a dictionary to map course IDs to course names
course_dict = {
    1: 'Advanced Python',
    2: 'Data Structures and Algorithms',
    3: 'Machine Learning',
    4: 'Web Development',
    5: 'AI'
}

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
for student in list_student:
    student_id, student_name, student_DoB = student['id'], student['name'], student['DoB']
    print(f"{student_name} (Student ID: {student_id}, DoB: {student_DoB}):")

    for course_id, mark in enumerate(list_mark[student_id - 1]):
        course_name = course_dict.get(course_id + 1, f"Course {course_id + 1}")
        print(f"  {course_name}: {mark}")

    print()

print(f"The list has {len(list_student)} students.")
