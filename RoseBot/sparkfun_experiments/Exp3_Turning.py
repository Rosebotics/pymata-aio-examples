#!/usr/bin/python
"""
  Exp3_Turning -- RoseBot Experiment 3

  Explore turning with the RoseBot by controlling the Right and Left motors
  separately.

  Hardware setup:
  This code requires only the most basic setup: the motors must be
  connected, and the board must be receiving power from the battery pack.
  
  23 Sept 2013 N. Seidle/M. Hord
  04 Oct 2014 B. Huang
  08 Oct 2015 L. Mathews 
 """

from pymata_aio.pymata3 import PyMata3
import rosebot.rosebot as rb
# This line "includes" the RoseBot library into your sketch.
# Provides special objects, methods, and functions for the RoseBot.

board = PyMata3()

motors = rb.RoseBotMotors(board)
# Instantiate the motor control object. This only needs to be done once.


def setup():
    print("Driving forward")
    # drive forward -- instead of using motors.drive(); Here is another way.
    motors.right_motor(150)  # Turn on right motor clockwise medium power (motorPower = 150)
    motors.left_motor(150)  # Turn on left motor counter clockwise medium power (motorPower = 150)
    board.sleep(1.0)  # Waits for 1000 ms.
    motors.brake();

    print("Pivot-- turn to right")
    # pivot -- spinning both motors CCW causes the RoseBot to turn to the right
    motors.right_motor(-100)  # Turn on right motor clockwise medium power (motorPower = 150)
    motors.left_motor(-100)  # Turn on left motor counter clockwise medium power (motorPower = 150)
    board.sleep(0.500)
    motors.brake()
    board.sleep(0.500)

    print("Driving Straight to Finish")
    # drive forward -- instead of using motors.drive(); Here is another way.
    motors.right_motor(150)  # Turn on right motor clockwise medium power (motorPower = 150)
    motors.left_motor(-150)  # Turn on left motor counter clockwise medium power (motorPower = 150)
    motors.drive(255)
    board.sleep(1.0)
    motors.brake()  # brake() motors


def loop():
    # Figure 8 pattern -- Turn Right, Turn Left, Repeat
    print("Veering Right")
    motors.left_motor(-200)  # Left motor CCW at 200
    motors.right_motor(80)  # Right motor CW at 80
    board.sleep(2.0)
    print("Veering Left")
    motors.left_motor(-80)  # Left motor CCW at 80
    motors.right_motor(200)  # Right motor CW at 200
    board.sleep(2.0)
    pass


if __name__ == "__main__":
    setup()
    while True:
        loop()
