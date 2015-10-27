#!/usr/bin/python
"""
  Exp5_Bumpers -- RoseBot Experiment 5

  Now let's experiment with the whisker bumpers. These super-simple switches
  let you detect a collision before it really happens- the whisker will
  bump something before your robot crashes into it.

  This sketch was written by SparkFun Electronics, with lots of help from
  the Arduino community.
  This code is completely free for any use.
  Visit https://learn.sparkfun.com/tutorials/RoseBot-inventors-kit-guide
  for SIK information.

  8 Oct 2013 M. Hord
  Revised 30 Oct 2014 B. Huang
  Adapted for pymata-aio 8 Oct 2015 L. Mathews
"""
import rosebot.rosebot as rb

board = rb.RoseBotConnection(ip_address="r03.wlan.rose-hulman.edu")
# Instantiate the motor control object. This only needs to be done once.
motors = rb.RoseBotMotors(board)
left_bumper = rb.RoseBotDigitalInput(board, rb.PIN_3)  # initializes bumper object on pin 3
right_bumper = rb.RoseBotDigitalInput(board, rb.PIN_11)  # initializes bumper object on pin 11


def setup():
    # nothing here
    pass

def loop():
    motors.drive(255)

    left_bumper_state = left_bumper.read()
    # board.sleep(0.1)  # When using XBee a small sleep is necessary
    right_bumper_state = right_bumper.read()
    # board.sleep(0.1)  # When using XBee a small sleep is necessary
    if left_bumper_state == 0:  # left bumper is bumped
        reverse()
        turn_right()

    if right_bumper_state == 0:  # left bumper is bumped
        reverse()
        turn_left()


def reverse():
    """backs up at full power"""
    motors.drive(-255)
    board.sleep(0.5)
    motors.brake()
    board.sleep(0.1)


def turn_right():
    """turns RoseBot to the Right"""
    motors.drive_left(-150)  # spin CCW
    motors.drive_right(-150)  # spin CCW
    board.sleep(0.5)
    motors.brake();
    board.sleep(0.1)  # short delay to let robot fully stop


def turn_left():
    """turns RoseBot to the Left"""
    motors.drive_left(150)  # spin CCW
    motors.drive_right(150)  # spin CCW
    board.sleep(0.5)
    motors.brake();
    board.sleep(0.1)  # short delay to let robot fully stop


if __name__ == "__main__":
    setup()
    while True:
        loop()





