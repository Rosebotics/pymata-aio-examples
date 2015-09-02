"""
Uses the tkinter/ttk graphics library that comes with Python to drive a RedBot.
"""

import tkinter
from tkinter import ttk
from pymata_aio.pymata3 import PyMata3
from examples.sparkfun_redbot.sparkfun_experiments.library.redbot import RedBotEncoder, RedBotMotors


# COM_PORT = None # Use automatic com port detection (the default)
COM_PORT = "COM10"  # Manually specify the com port (optional)


# RedBot motor pins from RedBot.h
L_CTRL_1 = 2
L_CTRL_2 = 4
PWM_L = 5

R_CTRL_1 = 7
R_CTRL_2 = 8
PWM_R = 6

SERVO_GRIPPER_PIN = 11
SERVO_GRIPPER_ARM_PIN = 3
GRIPPER_CLOSE = 80
GRIPPER_MID = 120
GRIPPER_OPEN = 170
GRIPPER_ARM_DOWN = 70
GRIPPER_ARM_MID = 120
GRIPPER_ARM_UP = 150

straight_speed = 150
turning_speed = 100
board = PyMata3(com_port=COM_PORT)
last_button = None
TURN_AMOUNT = 30
encoders = RedBotEncoder(board)
motors = RedBotMotors(board)
ENCODER_PIN_LEFT = 16
ENCODER_PIN_RIGHT = 10


def main():
    global speedo_display_straight, speedo_display_turn
    print("tkinter GUI drive")
    board.servo_config(SERVO_GRIPPER_PIN)
    board.servo_config(SERVO_GRIPPER_ARM_PIN)

    root = tkinter.Tk()
    root.title("RedBot simple drive")

    main_frame = ttk.Frame(root, padding=30, relief="raised")
    main_frame.grid()

    speedo_display_straight = ttk.Label(main_frame, text="Straight speed = " + str(straight_speed))
    speedo_display_straight.grid(column=7, row=1)

    speedo_display_turn = ttk.Label(main_frame, text="Turning speed = " + str(turning_speed))
    speedo_display_turn.grid(column=7, row=2)

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

    button = ttk.Button(main_frame, text="Speed + ")
    button.grid(column=4, row=1)
    button["command"] = speedIncrease

    button = ttk.Button(main_frame, text="Speed -")
    button.grid(column=4, row=2)
    button["command"] = speedDecrease

    button = ttk.Button(main_frame, text="Reset Speeds")
    button.grid(column=6, row=7)
    button["command"] = reset_speed

    root.bind("<Up>", driveForward)
    root.bind("<Left>", ccwSpin)
    root.bind("<space>", stop)
    root.bind("<Right>", cwSpin)
    root.bind("<Down>", driveReverse)
    root.bind("<w>", armUp)
    root.bind("<s>", armDown)
    root.bind("<d>", gripperOpen)
    root.bind("<a>", gripperClose)
    root.bind("<,>", speedDecrease)
    root.bind("<.>", speedIncrease)
    root.bind("<Shift-Left>", turn_left_degree)
    root.bind("<Shift-Right>", turn_right_degree)
    root.mainloop()


def armUp(event=None):
    print("Move servo arm to up position")
    # board.analog_write(SERVO_GRIPPER_ARM_PIN, GRIPPER_ARM_UP)
    for pos in range(GRIPPER_ARM_MID, GRIPPER_ARM_UP, +1):
        board.analog_write(SERVO_GRIPPER_ARM_PIN, pos)
        board.sleep(.015)
    global button


def armDown(event=None):
    print("Move servo arm to down position")
    for pos in range(GRIPPER_ARM_MID, GRIPPER_ARM_DOWN, -1):
        board.analog_write(SERVO_GRIPPER_ARM_PIN, pos)
        board.sleep(.015)


def gripperOpen(event=None):
    print("Open the gripper")
    for pos in range(GRIPPER_MID, GRIPPER_OPEN, +1):
        board.analog_write(SERVO_GRIPPER_PIN, pos)
        board.sleep(.015)


def gripperClose(event=None):
    print("Close the gripper")
    for pos in range(GRIPPER_MID, GRIPPER_CLOSE, -1):
        board.analog_write(SERVO_GRIPPER_PIN, pos)
        board.sleep(.015)


def driveForward(event=None):
    print("Go forward")
    motors.drive(straight_speed)
    last_button_pushed("up")


def ccwSpin(event=None):
    print("Spin counter clockwise")
    motors.left_rev(turning_speed)
    motors.right_fwd(turning_speed)
    last_button_pushed("left")


def stop(event=None):
    print("Stop")
    motors.brake()
    last_button_pushed("space")


def cwSpin(event=None):
    print("Clockwise spin")
    motors.left_fwd(turning_speed)
    motors.right_rev(turning_speed)
    last_button_pushed("right")


def driveReverse(event=None):
    print("Go Reverse")
    motors.drive(-straight_speed)
    last_button_pushed("down")


def speedIncrease(event=None):
    global straight_speed
    global turning_speed
    speed_adjust = 30
    straight_speed += speed_adjust
    straight_speed = min(straight_speed, 255)
    turning_speed += speed_adjust
    turning_speed = min(turning_speed, 255)
    resend_last_speed()
    print("Speed is now : {}, turning speed is : {} ".format(straight_speed, turning_speed))


def speedDecrease(event=None):
    global straight_speed
    global turning_speed
    speed_adjust = 20
    straight_speed -= speed_adjust
    straight_speed = max(straight_speed, 0)
    turning_speed -= speed_adjust
    turning_speed = max(turning_speed, 0)
    resend_last_speed()
    print("Speed is now : {}, turning speed is : {} ".format(straight_speed, turning_speed))


def last_button_pushed(last_button_pushed):
    global last_button
    last_button = last_button_pushed


def reset_speed():
    global straight_speed, turning_speed
    straight_speed = 150
    turning_speed = 100
    resend_last_speed()


def resend_last_speed():
    if last_button == "down":
        driveReverse()
    elif last_button == "up":
        driveForward()
    elif last_button == "left":
        ccwSpin()
    elif last_button == "right":
        cwSpin()

    global speedo_display_straight, speedo_display_turn
    speedo_display_straight.configure(text="Straight speed = " + str(straight_speed))  # Updates the values on the
    # tkinter GUI
    speedo_display_turn.configure(text="Turning speed = " + str(turning_speed))


def turn_left_degree(event=None):
    encoders.clear_enc()
    motors.left_rev(turning_speed)
    motors.right_fwd(turning_speed)
    left_count = 0
    right_count = 0
    while left_count <= TURN_AMOUNT or right_count <= TURN_AMOUNT:
        left_count = encoders.get_ticks(ENCODER_PIN_LEFT)
        right_count = encoders.get_ticks(ENCODER_PIN_RIGHT)
        board.sleep(0.05)

    motors.brake()
    pass


def turn_right_degree(event=None):
    encoders.clear_enc()
    motors.left_fwd(turning_speed)
    motors.right_rev(turning_speed)
    left_count = 0
    right_count = 0
    while left_count <= TURN_AMOUNT or right_count <= TURN_AMOUNT:
        left_count = encoders.get_ticks(ENCODER_PIN_LEFT)
        right_count = encoders.get_ticks(ENCODER_PIN_RIGHT)
        board.sleep(0.05)
    motors.brake()


main()
