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
startpos = drone.get_position_data()
print(startpos)

#Resets the drones sensor and sleeps for 3 seconds
drone.reset_sensor() 
time.sleep(3)

#If batter is less than 20% then wont start
if battery <= 20:
    print("Drone battery too low to start")
    exit()

if Temp >= 45:
    print("Drone Overheated")
    exit()

#127 x 63 pixels
#create controller screen UI
drone.set_controller_LED(255,0,0,100)
drone.controller_clear_screen()
drone.sendDisplayDrawString(0, 0, "SCRIPT1 V3.5")
time.sleep(2)
drone.controller_clear_screen()
drone.sendDisplayDrawString(0, 0, "LOADING.")
time.sleep(1)
drone.sendDisplayDrawString(0,0,"LOADING..")
time.sleep(1)
drone.sendDisplayDrawString(0,0,"LOADING...")
time.sleep(1)
drone.sendDisplayDrawString(0,0,"LOADING.")
time.sleep(1)
drone.sendDisplayDrawString(0,0,"LOADING..")

#get takeoff location data
takeoffloc = drone.get_position_data()
print(takeoffloc)
drone.set_waypoint()

#draw controller screen UI
drone.controller_clear_screen()
drone.sendDisplayDrawString(0, 0, "SCRIPT1 V3.5")
drone.sendDisplayDrawString(0, 10, "Battery: " + str(battery) + "%")
drone.sendDisplayDrawString(0, 20, "Temp: " + str(Temp) + "C")

#make controller LED green to indicate that drone is ready
drone.set_controller_LED(21, 162, 12, 100)
drone.sendDisplayDrawString(0,0,"Press S to start Drone!")
#drone.controller_preview_canvas(image)

#press S to start 
while True:
    time.sleep(0.1)
    if drone.s_pressed():
         drone.takeoff()
         drone.controller_clear_screen()
         drone.sendDisplayDrawString(0,0,"Code Running")
         break

#Movement
color_data = drone.get_front_color()
print(color_data)

#drone landing indicator
drone.set_controller_LED(255, 0, 0, 100)
drone.controller_buzzer(600, 1000)

#go to landing pad
drone.goto_waypoint(drone.waypoint_data[0], 0.5)

#land and close drone connection
drone.land()
drone.close()
