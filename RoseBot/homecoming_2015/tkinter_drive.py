"""
Uses the tkinter/ttk graphics library that comes with Python to drive a RedBot.
"""

import tkinter
from tkinter import ttk
from pymata_aio.pymata3 import PyMata3
from examples.sparkfun_redbot.sparkfun_experiments.library.redbot import RedBotEncoder, RedBotMotors

COM_PORT = None  # Use automatic com port detection (the default)
# COM_PORT = "COM10"  # Manually specify the com port (optional)


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
GRIPPER_OPEN = 160
GRIPPER_ARM_DOWN = 70
GRIPPER_ARM_MID = 120
GRIPPER_ARM_UP = 180

straight_speed = 150
turning_speed = 100
board = PyMata3(com_port=COM_PORT)
last_button = None
TURN_AMOUNT = 30
# encoders = RedBotEncoder(board)
motors = RedBotMotors(board)
ENCODER_PIN_LEFT = 16
ENCODER_PIN_RIGHT = 10
gripper_open = False
arm_up = False

pos = GRIPPER_ARM_MID


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
    button["command"] = drive_forward

    button = ttk.Button(main_frame, text="CCW Spin")
    button.grid(column=0, row=1)
    button["command"] = ccw_spin

    button = ttk.Button(main_frame, text="Stop")
    button.grid(column=1, row=1)
    button["command"] = stop

    button = ttk.Button(main_frame, text="CW Spin")
    button.grid(column=2, row=1)
    button["command"] = cw_spin

    button = ttk.Button(main_frame, text="Reverse")
    button.grid(column=1, row=2)
    button["command"] = drive_reverse

    button = ttk.Button(main_frame, text="Speed + ")
    button.grid(column=4, row=1)
    button["command"] = speed_increase

    button = ttk.Button(main_frame, text="Speed -")
    button.grid(column=4, row=2)
    button["command"] = speed_decrease

    button = ttk.Button(main_frame, text="Reset Speeds")
    button.grid(column=6, row=7)
    button["command"] = reset_speed

    exit_button = ttk.Button(main_frame, text="Shutdown")
    exit_button.grid(column=7, row=8)
    exit_button["command"] = shutdown

    root.bind("<w>", drive_forward)
    root.bind("<a>", ccw_spin)
    root.bind("<d>", cw_spin)
    root.bind("<s>", drive_reverse)
    root.bind("<KeyRelease-w>", stop)
    root.bind("<KeyRelease-a>", stop)
    root.bind("<KeyRelease-s>", stop)
    root.bind("<KeyRelease-d>", stop)
    root.bind("<space>", stop)
    root.bind("<Up>", arm_up)
    root.bind("<Down>", arm_down)
    root.bind("<Left>", gripper_toggle)
    root.bind("<Right>", gripper_toggle)
    root.bind("<,>", speed_decrease)
    root.bind("<.>", speed_increase)
    # root.bind("<Shift-Left>", turn_left_degree)
    # root.bind("<Shift-Right>", turn_right_degree)
    root.bind("</>", reset_speed)
    root.mainloop()


def arm_up(event=None):
    global pos
    pos += 20
    print("Move servo arm up, Current Angle = {}".format(pos))

    board.analog_write(SERVO_GRIPPER_ARM_PIN, pos)
    pos = min(GRIPPER_ARM_UP, pos)
    board.sleep(.001)


def arm_down(event=None):
    global pos
    pos -= 20
    pos = max(GRIPPER_ARM_DOWN, pos)
    print("Move servo arm down, Current Angle = {}".format(pos))
    board.analog_write(SERVO_GRIPPER_ARM_PIN, pos)
    board.sleep(.001)


def gripper_toggle(event=None):
    print("Open the gripper")
    global gripper_open
    if not gripper_open:
        for pos in range(GRIPPER_MID, GRIPPER_OPEN, +1):
            board.analog_write(SERVO_GRIPPER_PIN, pos)
            board.sleep(.015)
        gripper_open = True
    else:
        for pos in range(GRIPPER_MID, GRIPPER_CLOSE, -1):
            board.analog_write(SERVO_GRIPPER_PIN, pos)
            board.sleep(.015)
        gripper_open = False


def drive_forward(event=None):
    print("Go forward")
    motors.drive(straight_speed)
    last_button_pushed("up")


def ccw_spin(event=None):
    print("Spin counter clockwise")
    motors.left_rev(turning_speed)
    motors.right_fwd(turning_speed)
    last_button_pushed("left")


def stop(event=None):
    print("Stop")
    motors.brake()
    last_button_pushed("space")


def cw_spin(event=None):
    print("Clockwise spin")
    motors.left_fwd(turning_speed)
    motors.right_rev(turning_speed)
    last_button_pushed("right")


def drive_reverse(event=None):
    print("Go Reverse")
    motors.drive(-straight_speed)
    last_button_pushed("down")


def speed_increase(event=None):
    global straight_speed
    global turning_speed
    speed_adjust = 30
    straight_speed += speed_adjust
    straight_speed = min(straight_speed, 255)
    turning_speed += speed_adjust
    turning_speed = min(turning_speed, 255)
    resend_last_speed()
    print("Speed is now : {}, turning speed is : {} ".format(straight_speed, turning_speed))


def speed_decrease(event=None):
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
        drive_reverse()
    elif last_button == "up":
        drive_forward()
    elif last_button == "left":
        ccw_spin()
    elif last_button == "right":
        cw_spin()

    global speedo_display_straight, speedo_display_turn
    speedo_display_straight.configure(text="Straight speed = " + str(straight_speed))  # Updates the values on the
    # tkinter GUI
    speedo_display_turn.configure(text="Turning speed = " + str(turning_speed))


#TODO: Find out how to put in encoders without blowing everything else up

# def turn_left_degree(event=None):
#     encoders.clear_enc()
#     motors.left_rev(turning_speed)
#     motors.right_fwd(turning_speed)
#     left_count = 0
#     right_count = 0
#     while left_count <= TURN_AMOUNT or right_count <= TURN_AMOUNT:
#         left_count = encoders.get_ticks(ENCODER_PIN_LEFT)
#         right_count = encoders.get_ticks(ENCODER_PIN_RIGHT)
#         board.sleep(0.05)
#
#     motors.brake()
#     pass
#
#
# def turn_right_degree(event=None):
#     encoders.clear_enc()
#     motors.left_fwd(turning_speed)
#     motors.right_rev(turning_speed)
#     left_count = 0
#     right_count = 0
#     while left_count <= TURN_AMOUNT or right_count <= TURN_AMOUNT:
#         left_count = encoders.get_ticks(ENCODER_PIN_LEFT)
#         right_count = encoders.get_ticks(ENCODER_PIN_RIGHT)
#         board.sleep(0.05)
#     motors.brake()


def shutdown(event=None):
    board.sleep(0.1)
    # encoders.shutdown()
    board.sleep(0.5)
    board.shutdown()


main()
