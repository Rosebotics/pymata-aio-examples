"""
  Exp8_1_AccelerometerRead -- RedBot Experiment 8.1

  Measuring speed, velocity, and acceleration are all key
  components to robotics. This first experiment will introduce
  you to using the Accelerometer sensor on the RedBot.

 """


import rosebot.rosebot as rb

board = rb.RoseBotConnection(ip_address='r03.wlan.rose-hulman.edu', use_log_file=False)
accelerometer = rb.RoseBotAccelerometer(board)

def main():
    """Display out the X, Y, and Z - axis "acceleration" measurements and also
            the relative angle between the X-Z, Y-Z, and X-Y vectors. (These give us
            the orientation of the RedBot in 3D space."""
    while True:
        if accelerometer.available():
            values = accelerometer.read()
            print(
                'x-val: {:.2f},\t y-val: {:.2f},\t z-val: {:.2f}, \t angle x-z:{:.2f},\t angle y-z: {:.2f},\t angle x-y: {:.2f},\t Tapped?: {},\t Orientation?: {}'\
                .format(values[rb.RoseBotAccelerometer.VAL_X], values[rb.RoseBotAccelerometer.VAL_Y], \
                         values[rb.RoseBotAccelerometer.VAL_Z], values[rb.RoseBotAccelerometer.VAL_ANGLE_XZ]\
                         , values[rb.RoseBotAccelerometer.VAL_ANGLE_YZ], values[rb.RoseBotAccelerometer.VAL_ANGLE_XY]\
                         , values[rb.RoseBotAccelerometer.VAL_TAPPED], values[rb.RoseBotAccelerometer.VAL_PORT_LAND]))
        else:
            print("Where's the device?")
            board.sleep(.001)
main()