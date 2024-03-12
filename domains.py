# domains/student.py: Class definition for Student
import numpy as np

class Student:
    def __init__(self, id, name, dob, marks):
        self.id = id
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

