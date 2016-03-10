"""
Uses the tkinter/ttk graphics library that comes with Python to drive a RoseBot.
"""
import tkinter
from tkinter import ttk
import rosebot.rosebot as rb

# Global Variables
straight_speed = 150
turning_speed = 100
last_button = None
PIXY_CENTER = 160
servo_position = 90
# Creating the board object
board = rb.RoseBotConnection(ip_address='r08.wlan.rose-hulman.edu', use_log_file=False)  # change the 'rXX' value
# Motor Object
motors = rb.RoseBotMotors(board)
# Encoder Object
encoders = rb.RoseBotEncoder(board)
# Pixy Board
pixy = None
buzzer = rb.RoseBotBuzzer(board)
test_pid_control = rb.RoseBotPid(kp=0.05, set_point=PIXY_CENTER)
# IR Sensors
line_sensor_left = rb.RoseBotAnalogInput(board, rb.RoseBotPhysicalConstants.PIN_A3)
line_sensor_center = rb.RoseBotAnalogInput(board, rb.RoseBotPhysicalConstants.PIN_A6)
line_sensor_right = rb.RoseBotAnalogInput(board, rb.RoseBotPhysicalConstants.PIN_A7)
ir_sensor_left = rb.RoseBotAnalogInput(board, rb.RoseBotPhysicalConstants.PIN_A0)
ir_sensor_center = rb.RoseBotAnalogInput(board, rb.RoseBotPhysicalConstants.PIN_A4)
ir_sensor_right = rb.RoseBotAnalogInput(board, rb.RoseBotPhysicalConstants.PIN_A5)
# Bumper Sensors
bumper_left = rb.RoseBotDigitalInput(board, rb.RoseBotPhysicalConstants.PIN_3)
bumper_right = rb.RoseBotDigitalInput(board, rb.RoseBotPhysicalConstants.PIN_10)
# D12 Button
button_d12 = rb.RoseBotDigitalInput(board, rb.RoseBotPhysicalConstants.PIN_BUTTON)

def main():

    print("RoseBot Hardware Unit Test")

    while True:
        update_values()
        root.update_idletasks()
        board.sleep(0.05)
        root.update()


def update_values():
    root.grid_columnconfigure(0, minsize=20, pad=10)
    root.grid_columnconfigure(0, minsize=20, pad=10)
    if pixy:

        blocks = pixy.get_blocks()

        pixy_tracking_update()
        pixy_object_display.configure(text="Objects Detected = " + str(len(blocks)) + "\t\t\t")
        bumper_left_display.configure(text="Bumpers: INACTIVE")
        bumper_right_display.configure(text="Bumpers: INACTIVE")
    else:
        pixy_object_display.configure(text="Objects Detected = PIXY NOT ACTIVE \t\t.")
        if bumper_left.read() == 0:
            bumper_left_display.configure(text="Left Bumper: BUMPED")
        else:
            bumper_left_display.configure(text="Left Bumper: NOT BUMPED")
        if bumper_right.read() == 0:
            bumper_right_display.configure(text="Right Bumper: BUMPED")
        else:
            bumper_right_display.configure(text="Right Bumper: NOT BUMPED")
        if button_d12.read() == 0:
            button_display.configure(text="Button: PRESSED")
        else:
            button_display.configure(text="Button: NOT PRESSED")


    encoder_right_display.configure(text="Right Encoder Count: " + str(encoders.count_right))
    encoder_left_display.configure(text="Left Encoder Count: " + str(encoders.count_left))

    speedo_display_straight.configure(text="Straight speed = " + str(straight_speed))  # Updates the values on the# tkinter GUI
    speedo_display_turn.configure(text="Turning speed = " + str(turning_speed))

    ir_left_display.configure(text="Left IR Value: " + str(ir_sensor_left.read()))
    ir_center_display.configure(text="Center IR Value: " + str(ir_sensor_center.read()))

    ir_right_display.configure(text="Right IR Value: " + str(ir_sensor_right.read()))
    line_sensor_left_display.configure(text="Left Line Follower Value: " + str(line_sensor_left.read()))
    line_sensor_center_display.configure(text="Center Line Follower Value: " + str(line_sensor_center.read()))
    line_sensor_right_display.configure(text="Right Line Follower Value: " + str(line_sensor_right.read()))





def drive_forward(event=None):
    print("Go forward")
    motors.drive_pwm(straight_speed)
    last_button_pushed("up")


def ccw_spin(event=None):
    print("Spin counter clockwise")
    motors.drive_pwm_left(-turning_speed)
    motors.drive_pwm_right(turning_speed)
    last_button_pushed("left")


def stop(event=None):
    print("Stop")
    motors.brake()
    last_button_pushed("space")


def cw_spin(event=None):
    print("Clockwise spin")
    motors.drive_pwm_left(turning_speed)
    motors.drive_pwm_right(-turning_speed)
    last_button_pushed("right")


def drive_reverse(event=None):
    print("Go Reverse")
    motors.drive_pwm(-straight_speed)
    last_button_pushed("down")


def speed_increase(event=None):
    global straight_speed
    global turning_speed
    speed_adjust = 30
    straight_speed += speed_adjust
    straight_speed = min(straight_speed, 255)
    turning_speed += speed_adjust
    turning_speed = min(turning_speed, 255)
    resend_last_speed()

def speed_decrease(event=None):

    speed_adjust = 20
    straight_speed -= speed_adjust
    straight_speed = max(straight_speed, 0)
    turning_speed -= speed_adjust
    turning_speed = max(turning_speed, 0)
    resend_last_speed()


def last_button_pushed(last_button_pushed):
    global last_button
    last_button = last_button_pushed


def reset_speed():
    global straight_speed, turning_speed
    straight_speed = 150
    turning_speed = 100
    resend_last_speed()


def resend_last_speed():
    if last_button == "down":
        drive_reverse()
    elif last_button == "up":
        drive_forward()
    elif last_button == "left":
        ccw_spin()
    elif last_button == "right":
        cw_spin()

    global speedo_display_straight, speedo_display_turn
    speedo_display_straight.configure(text="Straight speed = " + str(straight_speed))  # Updates the values on the
    # tkinter GUI
    speedo_display_turn.configure(text="Turning speed = " + str(turning_speed))


# TODO: Find out how to put in encoders without blowing everything else up


def shutdown(event=None):
    try:
        board.shutdown()
    except RuntimeError:
        print("Shutdown, goodbye!")


def buzzer_on(event=None):
    buzzer.play_tone(1000)

def buzzer_off(event=None):
    buzzer.stop()

def clear_encoders(event=None):
    encoders.reset_encoder_counts()

def next_test(event=None):
    global pixy
    if pixy is None:
        pixy = rb.RoseBotPixy(board)
        next_test_button.config(text="Turn Pixy Off")
    else :
        pixy = None
        next_test_button.config(text="Turn Pixy On")





def pixy_tracking_update():
    """ Prints the Pixy blocks data."""
    global servo_position
    blocks = pixy.get_blocks()
    if len(blocks) > 0:
        pan_error = blocks[0].x
        error = int(test_pid_control.update(pan_error))
        servo_position += error
    if servo_position > 180:
        servo_position = 180
    if servo_position < 0:
        servo_position = 0

    pixy.servo_pan_write(servo_position)
    board.sleep(0.05)


















# --------------------------------------------------------------------------------------------------
#  Initializes the robot, instantiating the required board, motor and sensor objects
# --------------------------------------------------------------------------------------------------

root = tkinter.Tk()
root.title("RoseBot Hardware Unit Test")
main_frame = ttk.Frame(root, padding=50, relief="raised")
main_frame.grid()


speedo = ttk.Label(main_frame, text="PWM Readings for Motors")
speedo.grid(column=7, row=3, sticky='w')
speedo_display_straight = ttk.Label(main_frame, text="Straight speed: " + str(straight_speed))
speedo_display_straight.grid(column=7, row=4, sticky='w')
speedo_display_turn = ttk.Label(main_frame, text="Turning speed: " + str(turning_speed))
speedo_display_turn.grid(column=7, row=5, sticky='w')

pixy_text = ttk.Label(main_frame, text="Pixy")
pixy_text.grid(column=7, row=0, sticky='w')
pixy_object_display = ttk.Label(main_frame, text="Pixy Objects Detected: ")
pixy_object_display.grid(column=7, row=1, sticky='w')

encoder_display = ttk.Label(main_frame, text="Encoders")
encoder_display.grid(column=7, row=7, sticky='w')
encoder_left_display = ttk.Label(main_frame, text="Left Encoder Count: ")
encoder_left_display.grid(column=7, row=8, sticky='w')
encoder_right_display = ttk.Label(main_frame, text="Right Encoder Count: ")
encoder_right_display.grid(column=7, row=9, sticky='w')

line_sensor_display = ttk.Label(main_frame, text="Line Followers")
line_sensor_display.grid(column=9, row=0, sticky='w')

line_sensor_left_display = ttk.Label(main_frame, text="Left Line Follower Value:")
line_sensor_left_display.grid(column=9, row=1, sticky='w')
line_sensor_center_display = ttk.Label(main_frame, text="Center Line Follower Value:")
line_sensor_center_display.grid(column=9, row=2, sticky='w')
line_sensor_right_display = ttk.Label(main_frame, text="Right Line Follower Value:")
line_sensor_right_display.grid(column=9, row=3, sticky='w')

ir_display = ttk.Label(main_frame, text="IR Distance Sensors")
ir_display.grid(column=9, row=5, sticky='w')
ir_left_display = ttk.Label(main_frame, text="Left IR Value: \t\t")
ir_left_display.grid(column=9, row=6, sticky='w')
ir_center_display = ttk.Label(main_frame, text="Center IR Value: \t\t")
ir_center_display.grid(column=9, row=7, sticky='w')
ir_right_display = ttk.Label(main_frame, text="Right IR Value: \t \t")
ir_right_display.grid(column=9, row=8, sticky='w')


bumpers_display = ttk.Label(main_frame, text="Bumpers ")
bumpers_display.grid(column=9, row=10, sticky='w')
bumper_left_display = ttk.Label(main_frame, text="Left Bumper: \t ")
bumper_left_display.grid(column=9, row=11, sticky='w')
bumper_right_display = ttk.Label(main_frame, text="Right Bumper:  \t\t")
bumper_right_display.grid(column=9, row=12, sticky='w')

button_display = ttk.Label(main_frame, text="Button:  ")
button_display.grid(column=7, row=11, sticky='w')






button = ttk.Button(main_frame, text="Forward")
button.grid(column=1, row=0)
button["command"] = drive_forward

button = ttk.Button(main_frame, text="CCW Spin")
button.grid(column=0, row=1)
button["command"] = ccw_spin

button = ttk.Button(main_frame, text="Stop")
button.grid(column=1, row=1)
button["command"] = stop

button = ttk.Button(main_frame, text="CW Spin")
button.grid(column=2, row=1)
button["command"] = cw_spin

button = ttk.Button(main_frame, text="Reverse")
button.grid(column=1, row=2)
button["command"] = drive_reverse

button = ttk.Button(main_frame, text="Speed + ")
button.grid(column=4, row=1)
button["command"] = speed_increase

button = ttk.Button(main_frame, text="Speed -")
button.grid(column=4, row=2)
button["command"] = speed_decrease

button = ttk.Button(main_frame, text="Reset Speeds")
button.grid(column=5, row=14)
button["command"] = reset_speed

button = ttk.Button(main_frame, text="Reset Encoders")
button.grid(column=5, row=15)
button["command"] = clear_encoders

buzzer_button = ttk.Button(main_frame, text="Buzzer On")
buzzer_button.grid(column=0, row=14)
buzzer_button["command"] = buzzer_on

buzzer_button = ttk.Button(main_frame, text="Buzzer Off")
buzzer_button.grid(column=0, row=15)
buzzer_button["command"] = buzzer_off

next_test_button = ttk.Button(main_frame, text="Turn Pixy On")
next_test_button.grid(column=1, row=15)
next_test_button["command"] = next_test

exit_button = ttk.Button(main_frame, text="Shutdown")
exit_button.grid(column=15, row=15)
exit_button["command"] = shutdown

# KEY PRESSES  #
root.bind("<w>", drive_forward)
root.bind("<a>", ccw_spin)
root.bind("<d>", cw_spin)
root.bind("<s>", drive_reverse)
root.bind("<KeyRelease-w>", stop)
root.bind("<KeyRelease-a>", stop)
root.bind("<KeyRelease-s>", stop)
root.bind("<KeyRelease-d>", stop)
root.bind("<space>", stop)
root.bind("<,>", speed_decrease)
root.bind("<.>", speed_increase)
root.bind("</>", reset_speed)
root.bind("<t>", buzzer_on)
root.bind("<KeyRelease-t>", buzzer_off)
root.bind("<c>", clear_encoders)


main()

