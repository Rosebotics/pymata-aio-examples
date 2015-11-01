#!/usr/bin/python
"""
  Turns on an LED on for one second, then off for one second, repeatedly.

  Most Arduinos have an on-board LED you can control. On the Uno and
  Leonardo, it is attached to digital pin 13. If you're unsure what
  pin the on-board LED is connected to on your Arduino model, check
  the documentation at http://www.arduino.cc
"""

from pymata_aio.pymata3 import PyMata3
from pymata_aio.constants import Constants
import asyncio

BOARD_LED = 13
board = PyMata3(ip_address="r03.wlan.rose-hulman.edu")


def setup():
    board.set_pin_mode(BOARD_LED, Constants.OUTPUT)
    board.set_pin_mode(12, Constants.INPUT, callback=my_callback, cb_type=Constants.CB_TYPE_DIRECT)
    board.digital_write(12, 1)


def loop():
    print("LED On")
#     board.digital_write(BOARD_LED, 1)
#     board.sleep(1.0)
    print("LED Off")
    loop = asyncio.get_event_loop()
    if loop.is_running():
        print("in while the loop is running don't use Pymata3")
    else:
        print("Fine to call Pymata3")

#     board.digital_write(BOARD_LED, 0)
    board.sleep(1.0)

def my_second_callback():
    print("Called second callback")

    # board.digital_write(BOARD_LED, 1)
    # loop.run_until_complete(board.core.digital_write(BOARD_LED, value[1]))


def my_callback(value):
    print("Called Value = {}".format(value))
    # board.digital_write(BOARD_LED, value[1])  # RuntimeError: Event loop is running
    # board.core.digital_write(BOARD_LED, value[1]) # gives error first time, but never works
    loop = asyncio.get_event_loop()
    if loop.is_running():
        print("the loop is running don't use Pymata3")

    if loop.is_running():
        print("the loop is running don't use Pymata3")
        loop = asyncio.ensure_future(board.core.digital_write(BOARD_LED, 0))  # RuntimeError: Event loop is running

    else:
        print("stopped the loop")
    asyncio.ensure_future(board.core.digital_write(BOARD_LED, value[1]))  # RuntimeError: Event loop is running

    # loop.call_later(0.1, my_second_callback)




if __name__ == "__main__":
    setup()
    while True:
        loop()
