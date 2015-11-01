"""
Exp9_SerialDrive -- RoseBot Experiment 9

  The first step to controlling the RoseBot remotely is to first drive it
  from the Serial Monitor.

 ***********************************************************************/
"""
import rosebot.rosebot as rb

def main():
    board = rb.RoseBotConnection(ip_address='r03.wlan.rose-hulman.edu')  # change the 'rXX' value
    motors = rb.RoseBotMotors(board)
    while True:
        speed = int(input())  # input any integer from -255 (reverse full speed) to 255 (full speed forward)
        motors.drive_pwm(speed)
main()


