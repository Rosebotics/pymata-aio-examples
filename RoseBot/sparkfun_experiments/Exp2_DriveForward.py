"""
  Exp2_DriveForward -- RoseBot Experiment 2

  Drive forward and stop.

  Hardware setup:
  The Power switch must be on, the motors must be connected, and the board must be receiving power
  from the battery. The motor switch must also be switched to RUN.
"""

import rosebot.rosebot as rb


def main():
    board = rb.RoseBotConnection(ip_address="r03.wlan.rose-hulman.edu")  # change the 'rXX' value
    motors = rb.RoseBotMotors(board)
    print("Left and right motors at full speed forward")
    motors.drive_pwm(255)  # Turn on Left and right motors at full speed forward.
    board.sleep(2.0)  # Waits for 2 seconds
    print("Stop both motors")
    motors.brake()  # Stops both motors
    board.shutdown()

main()
