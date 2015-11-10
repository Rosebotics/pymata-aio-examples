"""
Demo of using the pan and tilt servo kit.
This code assumes you have connected the servos connected to the Pixy board directly.
Due to power limitations we only use the pan servo in this demo.
"""
import rosebot.rosebot as rb
board = rb.RoseBotConnection(ip_address="r05.wlan.rose-hulman.edu")
pixy = rb.RoseBotPixy(board)

def main():
    while True:
        for pos in range(0, 180, 2):
            pixy.servo_pan_write(pos)
            board.sleep(0.1)
        for pos in range(180, 0, -2):
            pixy.servo_pan_write(pos)
            board.sleep(0.1)
        print("Sweep complete")
        board.sleep(1.0)

main()
