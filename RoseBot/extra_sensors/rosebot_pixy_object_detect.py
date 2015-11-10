"""
Demo of using the obbject_found method in the RoseBotPixy library.
When a Pixy detects an object it returns a bunch of useful values, such as the x-y position,
object height and object width. The object_found() method is able to filter your search for 
objects only of a certain height, length or area if you choose. This example shows you how 
to filter your search only for an object of a given area
"""
import rosebot.rosebot as rb

MIN_SIZE_PIXELS = 500
MIN_WIDTH_PIXELS = 20
MIN_HEIGHT_PIXELS = 20

def main():
    board = rb.RoseBotConnection(ip_address="r05.wlan.rose-hulman.edu")
    pixy = rb.RoseBotPixy(board)

    while True:
        print(pixy.object_found(MIN_SIZE_PIXELS))  # detecting an object of a minimum size in pixels^2
#         print(pixy.object_found(min_object_width=MIN_WIDTH_PIXELS)  #  Only searching for an object 20 pixels wide
#         print(pixy.object_found(min_object_length=MIN_HEIGHT_PIXELS)  #  Only searching for an object 20 pixels wide
#         pixy.print_blocks()  # prints out all detected objects

        board.sleep(0.1)


main()
