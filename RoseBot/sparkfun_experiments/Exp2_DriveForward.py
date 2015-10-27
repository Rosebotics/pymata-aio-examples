#!/usr/bin/python
"""
  Exp2_DriveForward -- RoseBot Experiment 2

  Drive forward and stop.

  Hardware setup:
  The Power switch must be on, the motors must be connected, and the board must be receiving power
  from the battery. The motor switch must also be switched to RUN.
  
  23 Sept 2013 N. Seidle/M. Hord
  04 Oct 2014 B. Huang
  08 Oct 2015 L. Mathews
"""

from pymata_aio.pymata3 import PyMata3
import rosebot.rosebot as rb
import sys
import signal
# This line "includes" the RoseBot library into your sketch.
# Provides special objects, methods, and functions for the RoseBot.

def signal_handler(sig, frame):
    print('\nYou pressed Ctrl+C')
    if board is not None:
       board.send_reset()
       board.shutdown()

    sys.exit(0)

board = PyMata3(ip_address='r02.wlan.rose-hulman.edu')

motors = rb.RoseBotMotors(board)
# Instantiate the motor control object. This only needs to be done once.


def setup():
    signal.signal(signal.SIGINT, signal_handler)
    print("Left and right motors at full speed forward")
    motors.drive(255)  # Turn on Left and right motors at full speed forward.
    board.sleep(2.0)  # Waits for 2 seconds
    print("Stop both motors")
    motors.stop()  # Stops both motors
    board.shutdown()


def loop():
    # Nothing here. We'll get to this in the next experiment.
    pass


if __name__ == "__main__":
    setup()

