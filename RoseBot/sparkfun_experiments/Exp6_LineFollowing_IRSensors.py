"""
  Exp6_LineFollowing_IRSensors -- RoseBot Experiment 6
 
  This code reads the three line following sensors on A3, A6, and A7
  and prints them out to the Serial Monitor. Upload this example to your
  RoseBot and open up the Serial Monitor by clicking the magnifying glass
  in the upper-right hand corner.
 
  This sketch was written by SparkFun Electronics,with lots of help from
  the Arduino community. This code is completely free for any use.
 
  8 Oct 2013 M. Hord
  Revised, 31 Oct 2014 B. Huang
  Adapted for pymata-aio 9 Oct 2015 L. Mathews
"""

from pymata_aio.pymata3 import PyMata3
import rosebot.rosebot as rb
import sys




def setup():
    print("Welcome to Experiment 6!")
    print("------------------------")


def loop():
    while 1:
        board.sleep(0.1)
        print("IR Sensor Readings: {},   {},    {}".format(IR_sensor_1.read(), IR_sensor_2.read(), IR_sensor_3.read()))


# --------------------------------------------------------------------------------------------------
#  Initializes the robot, instantiating the required board, motor and sensor objects
# --------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    board = PyMata3(ip_address='r03.wlan.rose-hulman.edu')  # change the 'rXX' value
    board.keep_alive(2)
    motors = rb.RoseBotMotors(board)
    IR_sensor_1 = rb.RoseBotAnalogInput(board, rb.PIN_A3)
    IR_sensor_2 = rb.RoseBotAnalogInput(board, rb.PIN_A6)
    IR_sensor_3 = rb.RoseBotAnalogInput(board, rb.PIN_A7)
    try:
        setup()

    # control-C can cause exceptions - the following suppresses them
    except:
        board.shutdown()
        sys.exit(0)
