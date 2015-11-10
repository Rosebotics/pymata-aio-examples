"""
RoseBot Tracking! 

This example uses the Pixy to track an object using basic PID control

"""
import rosebot.rosebot as rb

PIXY_CENTER = 160
servo_position = 90
# TODO: Put a pixy.track_object() function into the library
board = rb.RoseBotConnection(ip_address="r05.wlan.rose-hulman.edu")
pixy = rb.RoseBotPixy(board)

test_pid_control = rb.RoseBotPid(kp=0.05, set_point=PIXY_CENTER)
def pixy_value_update():
    """ Prints the Pixy blocks data."""
    global servo_position
    blocks = pixy.get_blocks()
    if len(blocks) > 0:
        pan_error = blocks[0]["x"]
        error = int(test_pid_control.update(pan_error))
        servo_position += error
    if servo_position > 180:
        servo_position = 180
    if servo_position < 0:
        servo_position = 0

    pixy.servo_pan_write(servo_position)
    board.sleep(0.05)


def main():

    while True:
        pixy.get_blocks()
        pixy_value_update()

main()
