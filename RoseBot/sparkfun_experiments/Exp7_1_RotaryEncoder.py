"""
  Exp7_1_RotaryEncoder -- RoseBot Experiment 7

  Knowing where your robot is can be very important. The RoseBot supports
  the use of an encoder to track the number of revolutions each wheel has
  made, so you can tell not only how far each wheel has traveled but how
  fast the wheels are turning.
  
  Make sure the Pixy is not connected for this experiment (since it uses the button)

 """
import rosebot.rosebot as rb


def main():
    board = rb.RoseBotConnection(ip_address='r01.wlan.rose-hulman.edu', use_log_file=False)  # change the 'rXX' value
    #board = rb.RoseBotConnection(use_log_file=False)  # change the 'rXX' value
    motors = rb.RoseBotMotors(board)
    encoders = rb.RoseBotEncoder(board)
    button = rb.RoseBotDigitalInput(board, rb.RoseBotPhysicalConstants.PIN_BUTTON)

    print("Left     Right")
    print("==============")
    while True:
        # wait for a button press to start driving (note make sure Pixy is NOT connected so you can use the button).
        if button.read() == 0:
            print("Detected a button press")
            encoders.reset_encoder_counts()  # Reset the counters
            motors.drive_pwm(150)  # Start driving forward
        count_left = encoders.count_left
        count_right = encoders.count_right

        print("{}       {}".format(count_left, count_right))  # stores the encoder count to a variable
        board.sleep(rb.RoseBotConstants.SAMPLING_INTERVAL_S)

        #  if either left or right motor are more than 5 revolutions, stop
        if count_left >= 5 * rb.RoseBotPhysicalConstants.COUNTS_PER_REV or count_right >= 5 * rb.RoseBotPhysicalConstants.COUNTS_PER_REV:
            motors.brake()


main()
