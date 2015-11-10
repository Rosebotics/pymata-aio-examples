import rosebot.rosebot as rb

board = rb.RoseBotConnection(ip_address="r05.wlan.rose-hulman.edu", use_log_file=False)

#  board = rb.RoseBotConnection(use_log_file=False)

motors = rb.RoseBotMotors(board)
encoders = rb.RoseBotEncoder(board)
def main():
    print("Here is the RoseBot driving Normally (no control inbuilt) ")
    motors.drive_at_speed(30, 30, True)
    board.sleep(15)
    motors.brake()
    board.sleep(2)


    print("Here is an example of PID control to drive the RoseBot straight")
    motors.drive_at_speed(30, 30, True)
    board.sleep(8)
    motors.brake()
    board.sleep(2)
    board.shutdown()


main()
