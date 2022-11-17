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
print('Temp: ' + str(Temp) + 'C')

#Resets the drones sensor and sleeps for 1 second
drone.reset_sensor() 
time.sleep(1)

#If batter is less than 30% then wont start
if battery <= 30:
    exit()

#Movement
drone.takeoff()
drone.hover(1)

#land and close drone connection
drone.land()
drone.close()
