# output.py: module for curses output

def display_output(stdscr, message, y):
    stdscr.addstr(y, 0, message)
    stdscr.refresh()

