"""
  Exp1_BasicTest -- RoseBot Experiment 1 (blink)

  Time to make sure the electronics work! To test everything out, we're
  going to blink the LED on the board.
"""

import rosebot.rosebot as rb


def main():
    board = rb.RoseBotConnection(ip_address='r01.wlan.rose-hulman.edu')  # change the 'rXX' value
    led = rb.RoseBotDigitalOutput(board, rb.RoseBotPhysicalConstants.PIN_LED)
    while True:
        print("Blink sequence") # The total delay period is 1000 ms, or 1 second.
        led.digital_write(rb.RoseBotConstants.HIGH)  # Turns LED ON -- HIGH puts 5V on pin 13.
        board.sleep(0.5)  # "pauses" the program for 500 milliseconds
        led.digital_write(rb.RoseBotConstants.LOW)  # Turns LED ON -- HIGH puts 5V on pin 13.
        board.sleep(0.5)  # "pauses" the program for 500 milliseconds
        
main()