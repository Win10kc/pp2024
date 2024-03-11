import numpy as np
import curses

print('Student managerment system go: ')
class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.marks = np.array(marks)
        self.gpa = np.mean(self.marks)

    def display_info(self, stdscr, y):
        courses = ['Advanced Python', 'Data Structures and Algorithms', 'Machine Learning', 'Web Development', 'AI']
        stdscr.addstr(y, 0, f"{self.id}. {self.name} ({self.dob})")
        y += 1
        for mark, course in zip(self.marks, courses):
            stdscr.addstr(y, 0, f"{course}: {mark}")
            y += 1
        stdscr.addstr(y, 0, f"->GPA: {self.gpa:.2f}\n")
        y += 2
        return y

#Create a list of Student objects
students = [
    Student(1, 'Linh', '12/02/2003', [85, 40, 56, 70, 36]),
    Student(2, 'Lan', '14/12/2003', [75, 60, 80, 65, 45]),
    Student(3, 'May', '18/08/2003', [90, 70, 85, 78, 60]),
    Student(4, 'Chung', '14/03/2003', [80, 55, 70, 72, 50]),
    Student(5, 'Nguyen', '30/10/2003', [95, 80, 92, 88, 70])
]

#Sort the students by GPA in descending order
students.sort(key=lambda x: x.gpa, reverse=True)

#Function to display the sorted student list
def display_students(stdscr):
    stdscr.clear()
    y = 0
    for student in students:
        y = student.display_info(stdscr, y)
    stdscr.addstr(f"\nThe list contains a total of {len(students)} students.")
    stdscr.refresh()
    stdscr.getch()

#Use curses to run the display function
curses.wrapper(display_students)
