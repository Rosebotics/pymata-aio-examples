#!/usr/bin/python
"""
  This example is a test for the Homecoming 2015 servo arms.
 """

from pymata_aio.pymata3 import PyMata3
# This line "includes" the RedBot library into your sketch.
# Provides special objects, methods, and functions for the RedBot.

board = PyMata3()
# Instantiate the motor control object. This only needs to be done once.
SERVO_GRIPPER_PIN = 3
SERVO_GRIPPER_ARM_PIN = 11
GRIPPER_MIN_VALUE= 60
GRIPPER_ARM_MIN_VALUE = 60
GRIPPER_ARM_MAX_VALUE = 170
GRIPPER_MAX_VALUE = 170

def setup():

    board.servo_config(SERVO_GRIPPER_PIN)
    board.servo_config(SERVO_GRIPPER_ARM_PIN)


def loop():
    print("Servo Up")
    for pos in range(60,170, +1):
        board.analog_write(SERVO_GRIPPER_PIN,pos)
        board.analog_write(SERVO_GRIPPER_ARM_PIN,pos)
        board.sleep(.05)

    print("Gripper Open")
    for pos in range(170,60, -1):
        board.analog_write(SERVO_GRIPPER_PIN,pos)
        board.sleep(.015)

    print("Servo Down")
    for pos in range(170,60, -1):
        board.analog_write(SERVO_GRIPPER_ARM_PIN,pos)
        board.sleep(.05)


    print("Close Gripper")
    for pos in range(60,170, +1):
        (SERVO_GRIPPER_PIN,pos)
        board.analog_write(SERVO_GRIPPER_PIN,pos)
        board.sleep(.015)


if __name__ == "__main__":
    setup()
    while True:
        loop()
