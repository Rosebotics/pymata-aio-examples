"""
  Exp8_1_AccelerometerRead -- RedBot Experiment 8.1

  Measuring speed, velocity, and acceleration are all key
  components to robotics. This first experiment will introduce
  you to using the Accelerometer sensor on the RedBot.

  Hardware setup:
  You'll need to attach the RedBot Accelerometer board to hader on the upper
  right side of the mainboard. See the manual for details on how to do this.

  This sketch was written by SparkFun Electronics, with lots of help from
  the Arduino community. This code is completely free for any use.

  8 Oct 2013 M. Hord
  Revised, 31 Oct 2014 B. Huang
  Adapted for pymata-aio 9 Oct 2015 L. Mathews
  
  This experiment was inspired by Paul Kassebaum at Mathworks, who made
  one of the very first non-SparkFun demo projects and brought it to the
  2013 Open Hardware Summit in Boston. Thanks Paul!
 """

from pymata_aio.pymata3 import PyMata3
from rosebot.rosebot_accelerometer import RoseBotAccel
import rosebot.rosebot as rb
import sys


def setup():
    pass


def loop():
    if accelerometer.available():
        accelerometer.read()
        """Display out the X, Y, and Z - axis "acceleration" measurements and also
        the relative angle between the X-Z, Y-Z, and X-Y vectors. (These give us
        the orientation of the RedBot in 3D space."""
        print("({}, {}, {}) -- [{:4.2f}, {:4.2f}, {:4.2f}]".format(accelerometer.x, accelerometer.y, accelerometer.z,
                                                               accelerometer.angleXZ, accelerometer.angleYZ,
                                                               accelerometer.angleXY))

        board.sleep(0.1)  # short delay in between readings


# --------------------------------------------------------------------------------------------------
#  Initializes the robot, instantiating the required board, motor and sensor objects
# --------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    board = PyMata3(ip_address='r03.wlan.rose-hulman.edu')  # change the 'rXX' value
    board.keep_alive(2)
    accelerometer = RoseBotAccel(board)

    try:
        setup()
        while 1:
            loop()
    # control-C can cause exceptions - the following suppresses them
    except:
        board.shutdown()
        sys.exit(0)

