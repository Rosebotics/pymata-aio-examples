"""
  Exp7_2_DriveDistance -- RoseBot Experiment 7.2

  In an earlier experiment, we used a combination of speed and time to
  drive a certain distance. Using the encoders, we can me much more accurate.
  In this example, we will show you how to setup your robot to drive a certain
  distance regardless of the motorPower.

  This sketch was written by SparkFun Electronics, with lots of help from
  the Arduino community. This code is completely free for any use.

  8 Oct 2013 M. Hord
  Revised, 31 Oct 2014 B. Huang
  Adapted for pymata-aio 9 Oct 2015 L. Mathews
"""

from pymata_aio.pymata3 import PyMata3
from pymata_aio.constants import Constants
import rosebot.rosebot as rb
import sys

ENCODER_PIN_LEFT = 16
ENCODER_PIN_RIGHT = 10


def setup():
    board.set_pin_mode(rb.PIN_BUTTON, Constants.INPUT)
    board.digital_write(rb.PIN_BUTTON, 1)  # writing pin high sets the pull-up resistor


def loop():
    # wait for a button press to start driving.
    if board.digital_read(rb.PIN_BUTTON) == 0:
        motors.drive_distance(12, 150)  # drive 12 inches at motor_power = 150

# TODO: Ask Dr. Fisher if this is needed/wanted anymore, or just use equivalent library function?
# def driveDistance(distance, motor_power):
#     left_count = 0
#     right_count = 0
#     num_rev = distance / WHEEL_CIRC
#
#     # debug
#     print("drive_distance() {} inches at {} power for {:.2f} revolutions".format(distance, motor_power, num_rev))
#
#     encoders.clear_enc()  # clear the encoder count
#     motors.drive(motor_power)
#
#     while right_count < num_rev * COUNT_PER_REV:
#         left_count = encoders.get_ticks(ENCODER_PIN_LEFT)
#         right_count = encoders.get_ticks(ENCODER_PIN_RIGHT)
#         print("{}       {}       stop once over {:.0f} ticks".format(left_count, right_count, num_rev * COUNT_PER_REV))
#         board.sleep(0.1)
#
#     motors.brake()


# --------------------------------------------------------------------------------------------------
#  Initializes the robot, instantiating the required board, motor and sensor objects
# --------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    board = PyMata3(ip_address='r03.wlan.rose-hulman.edu')  # change the 'rXX' value
    board.keep_alive(2)
    motors = rb.RoseBotMotors(board)
    IR_sensor_center = rb.RoseBotAnalogInput(board, rb.PIN_A6)
    encoders = rb.RoseBotEncoder(board)

    try:
        setup()
        while 1:
            loop()
    # control-C can cause exceptions - the following suppresses them
    except:
        board.shutdown()
        sys.exit(0)
