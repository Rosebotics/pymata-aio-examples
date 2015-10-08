#!/usr/bin/python3
"""
  Stops before hitting the wall using the front distance sensor.

"""

import sys
import signal

from pymata_aio.pymata3 import PyMata3
from pymata_aio.constants import Constants
from library.redbot import RedBotMotors, RedBotSensor


WIFLY_IP_ADDRESS = None            # Leave set as None if not using WiFly
WIFLY_IP_ADDRESS = "10.0.1.18"  # If using a WiFly on the RedBot, set the ip address here.
if WIFLY_IP_ADDRESS:
  board = PyMata3(ip_address=WIFLY_IP_ADDRESS)
else:
  # Use a USB cable to RedBot or an XBee connection instead of WiFly.
  COM_PORT = None # Use None for automatic com port detection, or set if needed i.e. "COM7"
  board = PyMata3(com_port=COM_PORT)

motors = RedBotMotors(board)
distance_sensor_center = RedBotSensor(board, 6)

BUTTON_PIN = 12

def signal_handler(sig, frame):
    """Helper method to shutdown the RedBot if Ctrl-c is pressed"""
    print('\nYou pressed Ctrl+C')
    if board is not None:
        board.send_reset()
        board.shutdown()
    sys.exit(0)


def setup():
    signal.signal(signal.SIGINT, signal_handler)
    board.set_pin_mode(BUTTON_PIN, Constants.INPUT)
    board.digital_write(BUTTON_PIN, 1)
    print("Wall stop")


def loop():
  if board.digital_read(BUTTON_PIN) == 0:
    motors.left_fwd(180)
    motors.right_fwd(155)
    while distance_sensor_center.read() < 300:
      board.sleep(0.1)

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





