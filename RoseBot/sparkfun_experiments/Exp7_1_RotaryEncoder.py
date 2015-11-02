"""
  Exp7_1_RotaryEncoder -- RoseBot Experiment 7

  Knowing where your robot is can be very important. The RoseBot supports
  the use of an encoder to track the number of revolutions each wheel has
  made, so you can tell not only how far each wheel has traveled but how
  fast the wheels are turning.

 """
import rosebot.rosebot as rb


def main():
    board = rb.RoseBotConnection(ip_address='r03.wlan.rose-hulman.edu')  # change the 'rXX' value
    motors = rb.RoseBotMotors(board)
    IR_sensor_center = rb.RoseBotAnalogInput(board, rb.RoseBotPhysicalConstants.PIN_A6)
    encoders = rb.RoseBotEncoder(board)
    button = rb.RoseBotDigitalInput(board, rb.RoseBotPhysicalConstants.PIN_BUTTON)

    print("Left     Right")
    print("==============")
    while True:
        # wait for a button press to start driving.
        if button.read() == 0:
            encoders.reset_encoder_counts()  # Reset the counters
            motors.drive_pwm(150)  # Start driving forward
        count_left = encoders.count_left
        count_right = encoders.count_right

        print("{}       {}".format(count_left, count_right))  # stores the encoder count to a variable

        #  if either left or right motor are more than 5 revolutions, stop
        if count_left >= 5 * rb.RoseBotPhysicalConstants.COUNTS_PER_REV or count_right >= 5 * rb.RoseBotPhysicalConstants.COUNTS_PER_REV:
            motors.brake()


main()
