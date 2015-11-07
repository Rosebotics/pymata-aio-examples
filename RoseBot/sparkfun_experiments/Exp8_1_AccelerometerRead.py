"""
  Exp8_1_AccelerometerRead -- RedBot Experiment 8.1

  Measuring speed, velocity, and acceleration are all key
  components to robotics. This first experiment will introduce
  you to using the Accelerometer sensor on the RedBot.

 """


import rosebot.rosebot as rb

board = rb.RoseBotConnection(ip_address='10.0.1.19', use_log_file=False)
accelerometer = rb.RoseBotAccelerometer(board)

def main():
    """Display out the X, Y, and Z - axis "acceleration" measurements and also
            the relative angle between the X-Z, Y-Z, and X-Y vectors. (These give us
            the orientation of the RedBot in 3D space."""
    while True:
        if accelerometer.available():
            values = accelerometer.read()
            #print("values = " + str(values))
            x = values[rb.RoseBotAccelerometer.VAL_X]
            y = values[rb.RoseBotAccelerometer.VAL_Y]
            z = values[rb.RoseBotAccelerometer.VAL_Z]
            angle_xz = values[rb.RoseBotAccelerometer.VAL_ANGLE_XZ]
            angle_yz = values[rb.RoseBotAccelerometer.VAL_ANGLE_YZ]
            angle_xy = values[rb.RoseBotAccelerometer.VAL_ANGLE_XY]
            
            tap = accelerometer.read_tap()
            if tap:
                tap = 'TAPPED'
            else:
                tap = 'NO TAP'
                
            port_land = accelerometer.read_portrait_landscape()
            if port_land == accelerometer.LOCKOUT:
                port_land = 'Flat   '
            elif port_land == 0:
                port_land = 'Tilt Lf'
            elif port_land == 1:
                port_land = 'Tilt Rt'
            elif port_land == 2:
                port_land = 'Tilt Up'
            else:
                port_land = 'Tilt Dn'
            print('x-val: {:.2f}, y-val: {:.2f}, z-val: {:.2f} \t angle x-z:{:.2f}, angle y-z: {:.2f}, angle x-y: {:.2f} \t Tapped: {} \t Orientation: {}'.format( \
                  x, y, z, angle_xz, angle_yz, angle_xy, tap, port_land))
        else:
            print("Accelerometer not available.  Please try again.")
            board.sleep(2.0)
        board.sleep(0.025)
        
main()