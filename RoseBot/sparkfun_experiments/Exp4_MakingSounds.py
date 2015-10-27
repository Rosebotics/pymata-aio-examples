#!/usr/bin/python
"""
  Exp4_MakingSounds -- RoseBot Experiment 4

  Push the button (D12) to make some noise and start running!

  Hardware setup:
  Plug the included RoseBot Buzzer board into the Servo header labeled 9.

  This sketch was written by SparkFun Electronics, with lots of help from
  the Arduino community. This code is completely free for any use.
  
  
  23 Sept 2013 N. Seidle/M. Hord
  29 Oct 2014 B. Huang
  08 Oct 2015 L. Mathews
"""

from pymata_aio.pymata3 import PyMata3
import rosebot.rosebot as rb
from pymata_aio.constants import Constants
# This line "includes" the RoseBot library into your sketch.
# Provides special objects, methods, and functions for the RoseBot.

board = PyMata3()
# Instantiate the motor control object. This only needs to be done once.
motors = rb.RoseBotMotors(board)
PIN_BUZZER = rb.PIN_9


def setup():
    board.set_pin_mode(rb.PIN_BUTTON, Constants.INPUT)  # configures the button as an INPUT
    board.digital_write(rb.PIN_BUTTON, 1)  # Turns ON the pull up on the INPUT
    board.set_pin_mode(PIN_BUZZER, Constants.OUTPUT)  # configures the buzzerPin as an OUTPUT


def loop():
    if board.digital_read(rb.PIN_BUTTON) == 0:
        board.play_tone(PIN_BUZZER, Constants.TONE_TONE, 1000, None)
        board.sleep(0.125)  # Wait for 125ms.
        board.play_tone(PIN_BUZZER, Constants.TONE_NO_TONE, 0, 0)  # Stop playing the tone.

        # Turn on Tone again, at 2khz
        board.play_tone(PIN_BUZZER, Constants.TONE_TONE, 2000, 1000)  # Play a 2kHz tone on the buzzer pin
        motors.drive(255)  # Drive forward for a while
        board.sleep(1.0)
#         board.play_tone(BUZZER_PIN, Constants.TONE_NO_TONE, 0, 0)  # Not needed since set already.
        motors.brake()
    else:
        pass  # Otherwise do this.

if __name__ == "__main__":
    setup()
    while True:
        loop()
# import the API class





