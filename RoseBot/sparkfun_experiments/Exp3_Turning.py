"""
  Exp3_Turning -- RoseBot Experiment 3

  Explore turning with the RoseBot by controlling the Right and Left motors
  separately.

  Hardware setup:
  This code requires only the most basic setup: the motors must be
  connected, and the board must be receiving power from the battery pack.
"""

import rosebot.rosebot as rb

def main():
    board = rb.RoseBotConnection(ip_address="r01.wlan.rose-hulman.edu")  # change the 'rXX' value
    motors = rb.RoseBotMotors(board)

    print("Driving forward")
    motors.drive_pwm(150, 150)
    board.sleep(1.0)
    motors.brake()

    print("Pivot-- turn to right")
    motors.drive_pwm(100, -100)  # Turn on left motor counter clockwise medium power (motorPower = 150)
    board.sleep(0.5)
    motors.brake()

    print("Driving reverse")
    motors.drive_pwm(-150, -150)
    board.sleep(1.0)
    motors.brake()
    
    while True:
        # Figure 8 pattern -- Turn Right, Turn Left, Repeat
        print("Veering Right")
        motors.drive_pwm(150, 80)
        board.sleep(2.0)
        print("Veering Left")
        motors.drive_pwm(80, 150)
        board.sleep(2.0)

main()