#!/usr/bin/python3
"""
  Stops before hitting the wall using the front distance sensor.

"""

import sys
import signal

from pymata_aio.pymata3 import PyMata3
from pymata_aio.constants import Constants
import library.rosebot as rb


WIFLY_IP_ADDRESS = None            # Leave set as None if not using WiFly
WIFLY_IP_ADDRESS = "10.0.1.18"  # If using a WiFly on the RoseBot, set the ip address here.
WIFLY_IP_ADDRESS = "r05.wlan.rose-hulman.edu"  # If using a WiFly on the RoseBot, set the ip address here.
if WIFLY_IP_ADDRESS:
    board = PyMata3(ip_address=WIFLY_IP_ADDRESS)
else:
    # Use a USB cable to RoseBot or an XBee connection instead of WiFly.
    COM_PORT = None # Use None for automatic com port detection, or set if needed i.e. "COM7"
    board = PyMata3(com_port=COM_PORT)

motors = rb.RoseBotMotors(board)
distance_sensor_center = rb.RoseBotAnalogSensor(board, 6)
pushbutton = rb.RoseBotDigitalSensor(board, rb.PIN_BUTTON);

def signal_handler(sig, frame):
    """Helper method to shutdown the RoseBot if Ctrl-c is pressed"""
    print('\nYou pressed Ctrl+C')
    if board is not None:
        board.send_reset()
        board.shutdown()
    sys.exit(0)


def setup():
    signal.signal(signal.SIGINT, signal_handler)
    print("Wall stop")


def loop():
    if pushbutton.read() == 0:
        motors.drive_left(180)
        motors.drive_right(155)
        while distance_sensor_center.read() < 300:
            board.sleep(rb.DEFAULT_SLEEP_S)
        motors.brake()
        board.sleep(0.1)
        motors.drive(-155)
        board.sleep(0.5)
        motors.brake()
        board.sleep(0.1)


if __name__ == "__main__":
    setup()
    while True:
        loop()
        board.sleep(rb.DEFAULT_SLEEP_S)





