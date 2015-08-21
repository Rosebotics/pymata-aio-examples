"""
Uses the tkinter/ttk graphics library that comes with Python.
Rosegraphics is built on top of tkinter/ttk.
"""

import tkinter
from tkinter import ttk
from pymata_aio.pymata3 import PyMata3
from pymata_aio.constants import Constants

# RedBot motor pins from RedBot.h
L_CTRL_1 = 2
L_CTRL_2 = 4
PWM_L = 5

R_CTRL_1 = 7
R_CTRL_2 = 8
PWM_R = 6

board = PyMata3()
button_names = ["Left", "Forward", "Right", "CCW Spin", "Stop", "CW Spin", "Left Rev", "Reverse", "Right Rev"]




def main():
    board.set_pin_mode(L_CTRL_1, Constants.OUTPUT)
    board.set_pin_mode(L_CTRL_2, Constants.OUTPUT)
    board.set_pin_mode(PWM_L, Constants.PWM)
    board.set_pin_mode(R_CTRL_1, Constants.OUTPUT)
    board.set_pin_mode(R_CTRL_2, Constants.OUTPUT)
    board.set_pin_mode(PWM_R, Constants.PWM)

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

    s = 'You clicked on button {}'
    root.title(s.format(button_index))
    if button_index == 0:
        print("Go left forward")
    elif button_index == 1:
        print("Go forward")
        board.digital_write(L_CTRL_1, 1)
        board.digital_write(L_CTRL_2, 0)
        board.analog_write(PWM_L, 245)
        board.digital_write(R_CTRL_1, 1)
        board.digital_write(R_CTRL_2, 0)
        board.analog_write(PWM_R, 245)
    elif button_index == 2:
        print("Go right forward")
    elif button_index == 3:
        print("CCW Pivot")
    elif button_index == 4:
        print("Stop")
        board.digital_write(L_CTRL_1, 1)
        board.digital_write(L_CTRL_2, 0)
        board.analog_write(PWM_L, 0)
        board.digital_write(R_CTRL_1, 1)
        board.digital_write(R_CTRL_2, 0)
        board.analog_write(PWM_R, 0)
    elif button_index == 5:
        print("CW Pivot")
    elif button_index == 6:
        print("Go left reverse")
    elif button_index == 7:
        print("Reverse")
    elif button_index == 8:
        print("Go right reverse")


main()
