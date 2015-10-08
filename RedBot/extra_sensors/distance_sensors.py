"""
Distance sensor readings

  This code reads the three distance sensors on A3, A6, and A7
  and prints them out to the Serial Monitor.
"""

import sys
import signal

from pymata_aio.pymata3 import PyMata3
from library.rosebot import RoseBotAnalogSensor

WIFLY_IP_ADDRESS = None            # Leave set as None if not using WiFly
WIFLY_IP_ADDRESS = "10.0.1.18"  # If using a WiFly on the RedBot, set the ip address here.
WIFLY_IP_ADDRESS = "r05.wlan.rose-hulman.edu"  # If using a WiFly on the RedBot, set the ip address here.
if WIFLY_IP_ADDRESS:
    board = PyMata3(ip_address=WIFLY_IP_ADDRESS)
else:
    # Use a USB cable to RedBot or an XBee connection instead of WiFly.
    COM_PORT = None # Use None for automatic com port detection, or set if needed i.e. "COM7"
    board = PyMata3(com_port=COM_PORT)

distance_sensor_left = RoseBotAnalogSensor(board, 3)
distance_sensor_center = RoseBotAnalogSensor(board, 6)
distance_sensor_right = RoseBotAnalogSensor(board, 7)


def signal_handler(sig, frame):
    """Helper method to shutdown the RedBot if Ctrl-c is pressed"""
    print('\nYou pressed Ctrl+C')
    if board is not None:
        board.send_reset()
        board.shutdown()
    sys.exit(0)


def setup():
    signal.signal(signal.SIGINT, signal_handler)
    print("Distance sensor readings")
    print("------------------------")


def loop():
    board.sleep(0.3)
    print("IR Distance Sensor Readings: {},   {},    {}".format(
          distance_sensor_left.read(), distance_sensor_center.read(), distance_sensor_right.read()))


if __name__ == "__main__":
    setup()
    while True:
        loop()
