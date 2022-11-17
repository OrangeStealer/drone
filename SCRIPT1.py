import time

import keyboard
from codrone_edu.drone import *

#Inits drone library and pairs to the drone
drone = Drone()
#drone.pair(portname)
drone.pair()
 
#Variables
battery = drone.get_battery()
Temp = drone.get_drone_temp()

#print drone status
drone.get_flight_state()
print('Temp: ' + str(Temp) + 'C')
startpos = get_position_data()
print(startpos)

#Resets the drones sensor and sleeps for 3 seconds
drone.reset_sensor() 
time.sleep(3)

#If batter is less than 30% then wont start
if battery <= 30:
    exit()

#127 x 63 pixels
#create controller screen UI
drone.controller_clear_screen()
drone.sendDisplayDrawString(0, 0, "Hello, world!")

#make controller LED green to indicate that drone is ready
drone.set_controller_LED(21, 162, 12, 100)

#press S to start 
while True:
    time.sleep(0.1)
    if drone.s_pressed():
    drone.takeoff()

#Movement
drone.hover(1)
drone.keep_distance(10, 600)
fcd1 = drone.get_front_color()
print(fcd1)

#land and close drone connection
drone.land()
drone.close()