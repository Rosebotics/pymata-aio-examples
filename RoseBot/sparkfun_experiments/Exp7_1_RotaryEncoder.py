"""
  Exp7_1_RotaryEncoder -- RoseBot Experiment 7

  Knowing where your robot is can be very important. The RoseBot supports
  the use of an encoder to track the number of revolutions each wheel has
  made, so you can tell not only how far each wheel has traveled but how
  fast the wheels are turning.

  This sketch was written by SparkFun Electronics, with lots of help from
  the Arduino community. This code is completely free for any use.

  8 Oct 2013 M. Hord
  Revised, 31 Oct 2014 B. Huang+
  Adapted for pymata-aio 9 Oct 2015 L. Mathews
 """

from pymata_aio.pymata3 import PyMata3
from pymata_aio.constants import Constants
import rosebot.rosebot as rb
import sys



"""The commented code below is used only if you wish to connect serially instead of via WiFly"""
# COM_PORT = None  # Use automatic com port detection (the default)
# # COM_PORT = "COM5" # Manually specify the com port (optional)
# board = PyMata3(com_port=COM_PORT)


COUNTS_PER_REV = 192  # 4 pairs of N-S x 48:1 gearbox = 192 ticks per wheel rev


def setup():
    board.set_pin_mode(rb.PIN_BUTTON, Constants.INPUT)
    board.digital_write(rb.PIN_BUTTON, 1)  # writing pin high sets the pull-up resistor
    print("Left     Right")
    print("==============")


def loop():
    board.sleep(0.1)  # Add a delay
    # wait for a button press to start driving.
    if board.digital_read(rb.PIN_BUTTON) == 0:
        encoders.clear_enc()  # Reset the counters
        motors.drive(150)  # Start driving forward

    left_count = encoders.get_ticks(rb.PIN_A2)
    right_count = encoders.get_ticks(rb.PIN_10)

    print("{}       {}".format(left_count, right_count))  # stores the encoder count to a variable


    #  if either left or right motor are more than 5 revolutions, stop
    if left_count >= 5 * COUNTS_PER_REV or right_count >= 5 * COUNTS_PER_REV:
        motors.brake()



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
