"""
Uses the tkinter/ttk graphics library that comes with Python.
Rosegraphics is built on top of tkinter/ttk.
"""

import tkinter
from tkinter import ttk
import random

button_names = ["Left", "Forward", "Right", "CCW Spin", "Stop", "CW Spin", "Left Rev", "Reverse", "Right Rev"]

def main():
    root = tkinter.Tk()
    root.title("Simple remote drive")

    main_frame = ttk.Frame(root, padding=30, relief='raised')
    main_frame.grid()

    for k in range(3):
        for j in range(3):
            index = j * 3 + k
            button = ttk.Button(main_frame, text=button_names[index])
            button.grid(column=k, row=j)
            button['command'] = lambda button_index=index: callback(root, button_index)
    root.mainloop()


def callback(root, button_index):
    """
    Changes the title on the root window.


    :type root: tkinter.Tk
    :type name: str
    """
    print("Test")

    s = 'You clicked on button {}'
    root.title(s.format(button_index))
    if button_index == 0:
        print("Go left forward")

main()
