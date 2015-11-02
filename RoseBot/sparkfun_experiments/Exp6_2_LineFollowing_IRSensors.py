"""
  Exp6_2_LineFollowing_IRSensors -- RoseBot Experiment 6

  This code reads the three line following sensors on A3, A6, and A7
  and prints them out to the Serial Monitor. Upload this example to your
  RoseBot and open up the Serial Monitor by clicking the magnifying glass
  in the upper-right hand corner.
 
  This is a real simple example of a line following algorithm. It has
  a lot of room for improvement, but works fairly well for a curved track.
  It does not handle right angles reliably -- maybe you can come up with a
  better solution?
"""
import rosebot.rosebot as rb
board = rb.RoseBotConnection(ip_address='r03.wlan.rose-hulman.edu', use_log_file=False)  # change the 'rXX' value


LINE_THRESHOLD = 800  # level to detect if the sensor is on the line or not. If the sensor value is greater than this the sensor is above a DARK line.
SPEED = 50  # sets the nominal speed. Set to any number 0-255

motors = rb.RoseBotMotors(board)
left_ir_sensor = rb.RoseBotAnalogInput(board, rb.RoseBotPhysicalConstants.PIN_A3)  # pin number assignments for each IR sensor
center_ir_sensor = rb.RoseBotAnalogInput(board, rb.RoseBotPhysicalConstants.PIN_A6)
right_ir_sensor = rb.RoseBotAnalogInput(board, rb.RoseBotPhysicalConstants.PIN_A7)


def main():
    print("Welcome to Experiment 6.2 - Line Following")
    print("------------------------------------------")
    print("IR Sensor Readings:")
    board.sleep(0.5)



    while True:
        left_ir_reading = left_ir_sensor.read()
        center_ir_reading = center_ir_sensor.read()
        right_ir_reading = right_ir_sensor.read()

        print("IR Sensor Readings: {},   {},    {}".format(left_ir_reading, center_ir_reading, right_ir_reading))

        if center_ir_reading > LINE_THRESHOLD:
            left_speed = -SPEED
            right_speed = SPEED
        elif right_ir_reading > LINE_THRESHOLD:
            left_speed = -(SPEED + 50)
            right_speed = SPEED - 50
        elif left_ir_reading > LINE_THRESHOLD:
            left_speed = -(SPEED - 50)
            right_speed = SPEED + 50
        else:
            left_speed = 50  # If all sensors are seeing black, then set speed to slow until a sensor picks up
            # white again
            right_speed = 50

        if (left_ir_reading > LINE_THRESHOLD) & (center_ir_reading > LINE_THRESHOLD) & (right_ir_reading > LINE_THRESHOLD):
            motors.brake()
        else:
            pass
            motors.drive_at_speed(left_speed, right_speed)
        board.sleep(0.1)  # add a delay to decrease sensitivity
main()


