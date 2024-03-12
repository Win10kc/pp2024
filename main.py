# main.py: main script for coordination

import curses
from input import get_input
from output import display_output
from domains.student import Student

def display_students(stdscr):
    stdscr.clear()
    y = 0
    students = [
        Student(1, 'Linh', '12/02/2003', [85, 40, 56, 70, 36]),
        Student(2, 'Lan', '14/12/2003', [75, 60, 80, 65, 45]),
        Student(3, 'May', '18/08/2003', [90, 70, 85, 78, 60]),
        Student(4, 'Chung', '14/03/2003', [80, 55, 70, 72, 50]),
        Student(5, 'Nguyen', '30/10/2003', [95, 80, 92, 88, 70])
    ]
    students.sort(key=lambda x: x.gpa, reverse=True)
    for student in students:
        y = student.display_info(stdscr, y)
    display_output(stdscr, f"\nThe list contains a total of {len(students)} students.", y)
    stdscr.getch()

# Use curses to run the display function
curses.wrapper(display_students)
