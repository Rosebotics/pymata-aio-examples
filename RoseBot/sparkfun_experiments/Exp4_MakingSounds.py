"""
  Exp4_MakingSounds -- RoseBot Experiment 4

  Push the button (D12) to make some noise and start running!

  Hardware setup:
  Plug the included RoseBot Buzzer board into the Servo header labeled 9.
  Make sure the Pixy is NOT connected (it conflicts with the pushbutton on D12)

  This sketch was written by SparkFun Electronics, with lots of help from
  the Arduino community. This code is completely free for any use.
"""

import rosebot.rosebot as rb

def main():
    board = rb.RoseBotConnection(ip_address="r01.wlan.rose-hulman.edu")  # change the 'rXX' value
    motors = rb.RoseBotMotors(board)
    button = rb.RoseBotDigitalInput(board, rb.RoseBotPhysicalConstants.PIN_BUTTON)
    buzzer = rb.RoseBotBuzzer(board, rb.RoseBotPhysicalConstants.PIN_9)
    while True:
        if button.read() == rb.RoseBotConstants.LOW:
            buzzer.play_tone(400, 0.5)
            board.sleep(0.75)
            buzzer.play_tone(400, 0.5)
            board.sleep(0.75)
            buzzer.play_tone(2000, None)
            board.sleep(0.75)
            buzzer.stop()

            motors.drive_pwm(255)  # Drive forward for a while
            board.sleep(1.0)
            motors.brake()
        else:
            board.sleep(rb.RoseBotConstants.SAMPLING_INTERVAL_S)

main()
