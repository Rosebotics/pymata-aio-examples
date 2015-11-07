"""
Exp9_SerialDrive -- RoseBot Experiment 9

  The first step to controlling the RoseBot remotely is to first drive it
  from the Serial Monitor.

 ***********************************************************************/
"""
import rosebot.rosebot as rb

def main():
    board = rb.RoseBotConnection(ip_address='r03.wlan.rose-hulman.edu')  # change the 'rXX' value
    # The heartbeat keep_alive() message does not work with the input() function,
    # so disable keep_alive by setting the parameter to 0.
    board.keep_alive(0)
    motors = rb.RoseBotMotors(board)
    while True:
        speed = int(input())  # input any integer from -255 (reverse full speed) to 255 (full speed forward)
        motors.drive_pwm(speed)
main()


