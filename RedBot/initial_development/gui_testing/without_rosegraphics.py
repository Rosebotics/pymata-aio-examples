"""
Uses the tkinter/ttk graphics library that comes with Python.
Rosegraphics is built on top of tkinter/ttk.
"""

import tkinter
from tkinter import ttk
import random


def main():
    """ Calls the   TEST   functions in this module. """
    root = tkinter.Tk()
    root.title('Hello!')

    main_frame = ttk.Frame(root, padding=30, relief='raised')
    main_frame.grid()

    for k in range(3):
        for j in range(3):
            name = 'Thing ' + str(j * 3 + k)
            button = ttk.Button(main_frame, text=name)
            button.grid(column=k, row=j)
            button['command'] = lambda my_name=name: callback(root,
                                                              my_name)
    root.mainloop()


def callback(root, name):
    """
    Changes the title on the root window.

    :type root: tkinter.Tk
    :type name: str
    """
    s = 'Button ({}) likes {}'
    root.title(s.format(name, random.randrange(1000)))

main()
