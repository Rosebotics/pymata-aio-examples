"""
Uses the tkinter/ttk graphics library that comes with Python to drive a RedBot.
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


def main():
    print("tkinter GUI drive")
    board.set_pin_mode(L_CTRL_1, Constants.OUTPUT)
    board.set_pin_mode(L_CTRL_2, Constants.OUTPUT)
    board.set_pin_mode(PWM_L, Constants.PWM)
    board.set_pin_mode(R_CTRL_1, Constants.OUTPUT)
    board.set_pin_mode(R_CTRL_2, Constants.OUTPUT)
    board.set_pin_mode(PWM_R, Constants.PWM)

    root = tkinter.Tk()
    root.title("RedBot simple drive")

    main_frame = ttk.Frame(root, padding=30, relief="raised")
    main_frame.grid()

    button = ttk.Button(main_frame, text="Forward")
    button.grid(column=1, row=0)
    button["command"] = driveForward

    button = ttk.Button(main_frame, text="CCW Spin")
    button.grid(column=0, row=1)
    button["command"] = ccwSpin

    button = ttk.Button(main_frame, text="Stop")
    button.grid(column=1, row=1)
    button["command"] = stop

    button = ttk.Button(main_frame, text="CW Spin")
    button.grid(column=2, row=1)
    button["command"] = cwSpin

    button = ttk.Button(main_frame, text="Reverse")
    button.grid(column=1, row=2)
    button["command"] = driveReverse

    root.bind("<Up>", driveForward)
    root.bind("<Left>", cwSpin)
    root.bind("<space>", stop)
    root.bind("<Right>", ccwSpin)
    root.bind("<Down>", driveReverse)

    root.mainloop()


def driveForward(event=None):
    print("Go forward")
    board.digital_write(L_CTRL_1, 1)
    board.digital_write(L_CTRL_2, 0)
    board.analog_write(PWM_L, 255)
    board.digital_write(R_CTRL_1, 1)
    board.digital_write(R_CTRL_2, 0)
    board.analog_write(PWM_R, 255)


def ccwSpin(event=None):
    print("Spin counter clockwise")
    board.digital_write(L_CTRL_1, 0)
    board.digital_write(L_CTRL_2, 1)
    board.analog_write(PWM_L, 255)
    board.digital_write(R_CTRL_1, 1)
    board.digital_write(R_CTRL_2, 0)
    board.analog_write(PWM_R, 255)


def stop(event=None):
    print("Stop")
    board.digital_write(L_CTRL_1, 1)
    board.digital_write(L_CTRL_2, 1)
    board.analog_write(PWM_L, 0)
    board.digital_write(R_CTRL_1, 1)
    board.digital_write(R_CTRL_2, 1)
    board.analog_write(PWM_R, 0)


def cwSpin(event=None):
    print("Clockwise spin")
    board.digital_write(L_CTRL_1, 1)
    board.digital_write(L_CTRL_2, 0)
    board.analog_write(PWM_L, 255)
    board.digital_write(R_CTRL_1, 0)
    board.digital_write(R_CTRL_2, 1)
    board.analog_write(PWM_R, 255)


def driveReverse(event=None):
    print("Go forward")
    board.digital_write(L_CTRL_1, 0)
    board.digital_write(L_CTRL_2, 1)
    board.analog_write(PWM_L, 255)
    board.digital_write(R_CTRL_1, 0)
    board.digital_write(R_CTRL_2, 1)
    board.analog_write(PWM_R, 255)


main()
