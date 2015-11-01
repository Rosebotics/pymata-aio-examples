"""
  Exp7_2_DriveDistance -- RoseBot Experiment 7.2

  In an earlier experiment, we used a combination of speed and time to
  drive a certain distance. Using the encoders, we can me much more accurate.
  In this example, we will show you how to setup your robot to drive a certain
  distance regardless of the motor speed.
"""
import rosebot.rosebot as rb
def main():
    board = rb.RoseBotConnection(ip_address='r03.wlan.rose-hulman.edu')  # change the 'rXX' value
    motors = rb.RoseBotMotors(board)
    encoders = rb.RoseBotEncoder(board)
    button = rb.RoseBotDigitalInput(board, rb.RoseBotPhysicalConstants.PIN_BUTTON)
    while True:
        # wait for a button press to start driving.
        if button.read() == 0:
            motors.drive_distance(12, 150)  # drive 12 inches at motor_power = 150

main()

