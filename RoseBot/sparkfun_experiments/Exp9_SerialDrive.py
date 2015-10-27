"""
Exp9_SerialDrive -- RoseBot Experiment 9

  The first step to controlling the RoseBot remotely is to first drive it
  from the Serial Monitor in a tethered setup.

  Hardware setup:
  After uploading this sketch, keep the RoseBot tethered to your computer with
  the USB cable. Open up the Serial Monitor to send commands to the RoseBot to
  drive.

  This sketch was written by SparkFun Electronics, with lots of help from
  the Arduino community. This code is completely free for any use.

  15 Dec 2014 B. Huang
  Adapted for pymata-aio 9 Oct 2015 L. Mathews
  
  This experiment was inspired by Paul Kassebaum at Mathworks, who made
  one of the very first non-SparkFun demo projects and brought it to the
  2013 Open Hardware Summit in Boston. Thanks Paul!
 ***********************************************************************/
"""

from pymata_aio.pymata3 import PyMata3
import rosebot.rosebot as rb
import sys


def setup():
    pass

def loop():
    speed = int(input())
    speed = throttle(speed)
    motors.drive(speed)


   # function for constraining the speed value between -255:255
def throttle(n, minn=-255, maxn=255):
    return max(min(maxn, n), minn)

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
