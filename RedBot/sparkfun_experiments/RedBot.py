#!/usr/bin/python3.4
"""
  This class is a port from the https://github.com/sparkfun/RedBot Arduino library into Pymata-aio
  It is NOT a complete port. It just shows some of the main basic features.
"""

from pymata_aio.constants import Constants

# RedBot motor pins from RedBot.h
L_CTRL_1 = 2
L_CTRL_2 = 4
PWM_L = 5

R_CTRL_1 = 7
R_CTRL_2 = 8
PWM_R = 6

class RedBotEncoder:
    # TODO: Implement
    pass

encoderObject = RedBotEncoder()

class RedBotMotors:
    """Controls the motors on the RedBot"""

    def __init__(self, board):
        """Constructor for pin setup"""
        self.board = board
        # The interface to the motor driver is kind of ugly. It's three pins per
        # channel: two that define role (forward, reverse, stop, brake) and one
        # PWM input for speed.
        board.set_pin_mode(L_CTRL_1, Constants.OUTPUT)
        board.set_pin_mode(L_CTRL_2, Constants.OUTPUT)
        board.set_pin_mode(PWM_L, Constants.PWM) # Not done in RedBot motors but I just went ahead and added it.
        board.set_pin_mode(R_CTRL_1, Constants.OUTPUT)
        board.set_pin_mode(R_CTRL_2, Constants.OUTPUT)
        board.set_pin_mode(PWM_R, Constants.PWM) # Not done in RedBot motors but I just went ahead and added it.

    def drive(self, speed):
        """
            Starts both motors. It figures out whether the motors should go
            forward or revers, then calls the appropriate individual functions. Note
            the use of a 16-bit integer for the speed input; an 8-bit integer doesn't
            have the range to reach full speed. The calls to the actual drive functions
            are only 8-bit, since we only have 8-bit PWM.
        """
        if speed > 0:
            self.leftFwd(max(speed, 255))
            self.rightFwd(max(speed, 255))
        else:
            self.leftRev(max(abs(speed), 255))
            self.rightRev(max(abs(speed), 255))


    def stop(self):
        """
            stop() allows the motors to coast to a stop, rather than trying to stop them
            quickly. As will be the case with functions affecting both motors, the
            global stop just calls the individual stop functions for each wheel.
        """
        self.leftStop()
        self.rightStop()

    def leftStop(self):
        """allows left motor to coast to a stop"""
        self.board.digital_write(L_CTRL_1, 0)
        self.board.digital_write(L_CTRL_2, 0)
        self.board.analog_write(PWM_L, 0)


    def rightStop(self):
        """allows left motor to coast to a stop"""
        self.board.digital_write(R_CTRL_1, 0)
        self.board.digital_write(R_CTRL_2, 0)
        self.board.analog_write(PWM_R, 0)


# ******************************************************************************
#  Private functions for RedBotMotor
# ******************************************************************************/
# These are the motor-driver level abstractions for turning a given motor the
#  right direction. Users never see them, and *should* never see them, so we
#  make them private.

    def leftFwd(self, spd):
        self.board.digital_write(L_CTRL_1, 1)
        self.board.digital_write(L_CTRL_2, 0)
        self.board.analog_write(PWM_L, spd)
        # If we have an encoder in the system, we want to make sure that it counts
        # in the right direction when ticks occur.
        if encoderObject:
            encoderObject.lDir = 1


    def leftRev(self, spd):
        self.board.digital_write(L_CTRL_1, 0)
        self.board.digital_write(L_CTRL_2, 1)
        self.board.analog_write(PWM_L, spd)
        # If we have an encoder in the system, we want to make sure that it counts
        # in the right direction when ticks occur.
        if encoderObject:
            encoderObject.lDir = -1


    def rightFwd(self, spd):
        self.board.digital_write(R_CTRL_1, 1)
        self.board.digital_write(R_CTRL_2, 0)
        self.board.analog_write(PWM_R, spd)
        # If we have an encoder in the system, we want to make sure that it counts
        # in the right direction when ticks occur.
        if encoderObject:
            encoderObject.rDir = 1


    def rightRev(self, spd):
        self.board.digital_write(R_CTRL_1, 0)
        self.board.digital_write(R_CTRL_2, 1)
        self.board.analog_write(PWM_R, spd)
        # If we have an encoder in the system, we want to make sure that it counts
        # in the right direction when ticks occur.
        if encoderObject:
            encoderObject.rDir = -1
