class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.marks = []

    def add_mark(self, mark):
        self.marks.append(mark)

    def __str__(self):
        return f"{self.name} (Student ID: {self.student_id}, DoB: {self.dob})"


class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name

    def __str__(self):
        return self.name


# Create student objects
students = [
    Student(1, 'Linh', '12/02/2003'),
    Student(2, 'Lan', '14/12/2003'),
    Student(3, 'May', '18/08/2003'),
    Student(4, 'Chung', '14/03/2003'),
    Student(5, 'Nguyen', '30/10/2003')
]
list_mark = [
    [85, 40, 56, 70, 36],  # Linh's marks
    [75, 60, 80, 65, 45],  # Lan's marks
    [90, 70, 85, 78, 60],  # May's marks
    [80, 55, 70, 72, 50],  # Chung's marks
    [95, 80, 92, 88, 70]   # Nguyen's marks
]

# Create course objects
courses = [
    Course(1, 'Advanced Python'),
    Course(2, 'Data Structures and Algorithms'),
    Course(3, 'Machine Learning'),
    Course(4, 'Web Development'),
    Course(5, 'AI')
]

# Assign marks to students
for i, student in enumerate(students):
    student_marks = list_mark[i]
    for j, mark in enumerate(student_marks):
        students[i].add_mark(mark)

# Print student information
for student in students:
    print(student)
    for course, mark in zip(courses, student.marks):
        print(f"  {course}: {mark}")
    print()

print(f"The list contains a total of {len(students)} students.")

