"""
  Exp6_LineFollowing_IRSensors -- RoseBot Experiment 6
 
  This code reads the three line following sensors on A3, A6, and A7
  and prints them out to the console. 
"""
import rosebot.rosebot as rb

def main():
    board = rb.RoseBotConnection(ip_address='r03.wlan.rose-hulman.edu')  # change the 'rXX' value
    motors = rb.RoseBotMotors(board)
    IR_sensor_1 = rb.RoseBotAnalogInput(board, rb.RoseBotPhysicalConstants.PIN_A3)
    IR_sensor_2 = rb.RoseBotAnalogInput(board, rb.RoseBotPhysicalConstants.PIN_A6)
    IR_sensor_3 = rb.RoseBotAnalogInput(board, rb.RoseBotPhysicalConstants.PIN_A7)
    print("Welcome to Experiment 6!")
    print("------------------------")

    while True:
        board.sleep(0.1)
        print("IR Sensor Readings: {},   {},    {}".format(IR_sensor_1.read(), IR_sensor_2.read(), IR_sensor_3.read()))

main()
