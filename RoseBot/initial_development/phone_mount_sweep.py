#!/usr/bin/python
"""
Sweep the phone mount servos through their range.
"""

from pymata_aio.pymata3 import PyMata3

board = PyMata3()
SERVO_TILT_PIN = 11
SERVO_PAN_PIN = 3

DEFAULT_PAN_POSITION = 125
DEFAULT_TILT_POSITION = 45

PAN_MIN = 45
PAN_MAX = 180
TILT_MIN = 0
TILT_MAX = 100
STEP_AMOUNT = 2
SLEEP_TIME_S = 0.025

def setup():
    board.servo_config(SERVO_TILT_PIN)
    board.servo_config(SERVO_PAN_PIN)
    board.analog_write(SERVO_PAN_PIN, DEFAULT_PAN_POSITION)
    board.analog_write(SERVO_TILT_PIN, DEFAULT_TILT_POSITION)
    board.sleep(1.0)


def loop():
    print("Pan")
    for pos in range(DEFAULT_PAN_POSITION, PAN_MAX, STEP_AMOUNT):
        board.analog_write(SERVO_PAN_PIN, pos)
        board.sleep(SLEEP_TIME_S)

    for pos in range(PAN_MAX, PAN_MIN, -STEP_AMOUNT):
        board.analog_write(SERVO_PAN_PIN, pos)
        board.sleep(SLEEP_TIME_S)

    for pos in range(PAN_MIN, DEFAULT_PAN_POSITION + 1, STEP_AMOUNT):
        board.analog_write(SERVO_PAN_PIN, pos)
        board.sleep(SLEEP_TIME_S)


    print("Tilt")
    for pos in range(DEFAULT_TILT_POSITION, TILT_MAX, STEP_AMOUNT):
        board.analog_write(SERVO_TILT_PIN, pos)
        board.sleep(SLEEP_TIME_S)

    for pos in range(TILT_MAX, TILT_MIN, -STEP_AMOUNT):
        board.analog_write(SERVO_TILT_PIN, pos)
        board.sleep(SLEEP_TIME_S)

    for pos in range(TILT_MIN, DEFAULT_TILT_POSITION, STEP_AMOUNT):
        board.analog_write(SERVO_TILT_PIN, pos)
        board.sleep(SLEEP_TIME_S)


if __name__ == "__main__":
    setup()
    while True:
        loop()
