"""
Distance sensor readings

  This code reads the three distance sensors on A3, A6, and A7
  and prints them out to the Serial Monitor.
"""

import rosebot.rosebot as rb

board = rb.RoseBotConnection(ip_address="r05.wlan.rose-hulman.edu")

distance_sensor_left = rb.RoseBotAnalogInput(board, 3)
distance_sensor_center = rb.RoseBotAnalogInput(board, 6)
distance_sensor_right = rb.RoseBotAnalogInput(board, 7)



def setup():
    print("Distance sensor readings")
    print("------------------------")


def loop():
    print("IR Distance Sensor Readings: {},   {},    {}".format(
          distance_sensor_left.read(), distance_sensor_center.read(), distance_sensor_right.read()))
    board.sleep(1.0) # Additional sleep to slow down printing.


if __name__ == "__main__":
    setup()
    while True:
        loop()
        board.sleep(rb.DEFAULT_SLEEP_S)
