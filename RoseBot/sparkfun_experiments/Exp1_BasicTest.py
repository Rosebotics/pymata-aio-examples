#!/usr/bin/python
"""
  Exp1_BasicTest -- RoseBot Experiment 1

  Time to make sure the electronics work! To test everything out, we're
  going to blink the LED on the board.
  
   23 Sept 2013 N. Seidle/M. Hord
   04 Oct 2014 B. Huang
   09 Oct 2015 L.Mathews 
"""

from pymata_aio.pymata3 import PyMata3
from pymata_aio.constants import Constants
import rosebot.rosebot as rb
import sys


def setup():
    """setup() function runs once at the very beginning."""
    board.set_pin_mode(rb.PIN_BUTTON, Constants.OUTPUT)
    # The RedBot has an LED connected to pin 13.
    # Pins are all generic, so we have to first configure it
    # as an OUTPUT using this command.


def loop():
    """loop() function repeats over and over... forever!"""
    print("Blink sequence")
    board.digital_write(rb.PIN_BUTTON, 1)  # Turns LED ON -- HIGH puts 5V on pin 13.
    board.sleep(0.5)  # "pauses" the program for 500 milliseconds
    board.digital_write(rb.PIN_BUTTON, 0)  # Turns LED OFF -- LOW puts 0V on pin 13.
    board.sleep(0.5)  # "pauses" the program for 500 milliseconds
    # The total delay period is 1000 ms, or 1 second.


# --------------------------------------------------------------------------------------------------
#  Initializes the robot, instantiating the required board, motor and sensor objects
# --------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    board = PyMata3(ip_address='r03.wlan.rose-hulman.edu')  # change the 'rXX' value
    board.keep_alive(2)
    motors = rb.RoseBotMotors(board)
    try:
        setup()
        while 1:
            loop()
    # control-C can cause exceptions - the following suppresses them
    except:
        board.shutdown()
        sys.exit(0)
