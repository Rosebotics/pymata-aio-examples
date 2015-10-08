#!/usr/bin/python3
"""
  Stops before hitting the wall using the front distance sensor.

"""

import sys
import signal

from pymata_aio.pymata3 import PyMata3
from pymata_aio.constants import Constants
from library.redbot import RedBotMotors, RedBotSensor
import time

current_milli_time = lambda: int(round(time.time() * 1000))


WIFLY_IP_ADDRESS = None            # Leave set as None if not using WiFly
WIFLY_IP_ADDRESS = "10.0.1.18"  # If using a WiFly on the RedBot, set the ip address here.
WIFLY_IP_ADDRESS = "137.112.217.96"
#WIFLY_IP_ADDRESS = "r05.wlan.rose-hulman.edu"  # If using a WiFly on the RedBot, set the ip address here.
if WIFLY_IP_ADDRESS:
  board = PyMata3(ip_address=WIFLY_IP_ADDRESS)
else:
  # Use a USB cable to RedBot or an XBee connection instead of WiFly.
  COM_PORT = None # Use None for automatic com port detection, or set if needed i.e. "COM7"
  board = PyMata3(com_port=COM_PORT)

motors = RedBotMotors(board)


counter = 0
left_distance = 0
ALPHA = 0.3
def left_distance_changed(values):
  global counter
  global left_distance
  counter += 1
  if counter % 100 == 0:
    print("counter = {} time expected counts = {:0.1f}".format(counter, (current_milli_time() - start_time) / 25))
  #left_distance = distance_sensor_left.read()
  left_distance = left_distance * (1.0 - ALPHA) + values[1] * ALPHA


distance_sensor_left = RedBotSensor(board, 3, value_changed_callback=left_distance_changed)

BUTTON_PIN = 12

def signal_handler(sig, frame):
    """Helper method to shutdown the RedBot if Ctrl-c is pressed"""
    print('\nYou pressed Ctrl+C')
    if board is not None:
        board.send_reset()
        board.shutdown()
    sys.exit(0)


def setup():
    global start_time
    signal.signal(signal.SIGINT, signal_handler)
    start_time = current_milli_time()
    board.set_pin_mode(BUTTON_PIN, Constants.INPUT)
    board.digital_write(BUTTON_PIN, 1)
    print("Wall follow")

BASE_LEFT_SPEED = 160
BASE_RIGHT_SPEED = 140

def loop():
  global counter
  global left_distance
  if left_distance < 100:
    motors.left_fwd(BASE_LEFT_SPEED)
    motors.right_fwd(BASE_RIGHT_SPEED + 60)
  if left_distance < 200:
    motors.left_fwd(BASE_LEFT_SPEED)
    motors.right_fwd(BASE_RIGHT_SPEED + 30)
  if left_distance < 300:
    motors.left_fwd(BASE_LEFT_SPEED)
    motors.right_fwd(BASE_RIGHT_SPEED + 15)
  elif left_distance > 400:
    motors.left_fwd(BASE_LEFT_SPEED + 30)
    motors.right_fwd(BASE_RIGHT_SPEED)
  elif left_distance > 500:
    motors.left_fwd(BASE_LEFT_SPEED + 50)
    motors.right_fwd(BASE_RIGHT_SPEED)
  elif left_distance > 600:
    motors.left_fwd(BASE_LEFT_SPEED + 80)
    motors.right_fwd(BASE_RIGHT_SPEED)
  else:
    motors.left_fwd(BASE_LEFT_SPEED)
    motors.right_fwd(BASE_RIGHT_SPEED)
  print("filter {:0.1f} raw {}".format(left_distance, distance_sensor_left.read()))


if __name__ == "__main__":
    setup()
    while True:
        loop()
        board.sleep(0.1)





