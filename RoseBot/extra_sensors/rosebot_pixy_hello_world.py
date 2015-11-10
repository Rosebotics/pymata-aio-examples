#!/usr/bin/env python3
"""
Basic demo of reporting Pixy data.

 This sketch is a good place to start if you're just getting started with
 Pixy and pymata-aio.  This program simply prints the detected object blocks
 much like the standard Pixy Hello World demo for Arduino.

 In order to run this example you of course you need a Pixy and a RedBot with an ICSP header.
 The cable goes such that the red wire of the ribbon cable is on bottom.
 Also make sure you have nothing plugged into pin 11 which is just above that header.
 The Pixy uses pins 11 and 12, but the button does not seem to interfere with Pixy as long as
 it doesn't get pressed (just don't try to use the button and Pixy at the same time).

 You also need to make sure the Pixy has been trained to track a color
  (http://cmucam.org/projects/cmucam5/wiki/Teach_Pixy_an_object).
"""

import rosebot.rosebot as rb

board = rb.RoseBotConnection(ip_address="r05.wlan.rose-hulman.edu")
pixy = rb.RoseBotPixy(board)

def main():
    while 1:
        board.sleep(0)
        pixy.print_blocks()


main()
