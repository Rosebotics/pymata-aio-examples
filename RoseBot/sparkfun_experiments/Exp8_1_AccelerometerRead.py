"""
  Exp8_1_AccelerometerRead -- RedBot Experiment 8.1

  Measuring speed, velocity, and acceleration are all key
  components to robotics. This first experiment will introduce
  you to using the Accelerometer sensor on the RedBot.

 """

import rosebot.rosebot as rb


def main():
    board = rb.RoseBotConnection(ip_address='r03.wlan.rose-hulman.edu')  # change the 'rXX' value
    accelerometer = rb.RoseBotAccelerometer(board)



    while True:
        if accelerometer.available():
            accelerometer.read()
            """Display out the X, Y, and Z - axis "acceleration" measurements and also
            the relative angle between the X-Z, Y-Z, and X-Y vectors. (These give us
            the orientation of the RedBot in 3D space."""
            print("({}, {}, {}) -- [{:4.2f}, {:4.2f}, {:4.2f}]".format(accelerometer.x, accelerometer.y, accelerometer.z,
                                                                   accelerometer.angleXZ, accelerometer.angleYZ,
                                                                   accelerometer.angleXY))

            board.sleep(0.1)  # short delay in between readings
main()
