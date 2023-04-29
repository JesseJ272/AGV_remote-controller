import keyboard
import time
from pyModbusTCP.client import ModbusClient


vel_l = 0
vel_r = 0
V_MAX = 3000
V_MAX_BACK = -2000
VEL_LEFT_ADDR = 2
VEL_RIGHT_ADDR = 3



print("This script lets you control your connected AGV with your keyboard.\n")
print("Use w / x to accelerate / decelerate.")
print("Use a / d to turn left / right.")
print("Use s to stop.\n")

print("To stop the program use Ctrl+c.\n")

print("velocity left:  %s", vel_l)
print("velocity right:  %s", vel_r)


#client = ModbusClient(host="192.168.0.200", port=502, auto_open=True, auto_close=False)

while True:
    #Gerade vorwaerts, rueckwaerts und stop
    if keyboard.is_pressed('w'):
        if ((vel_l < V_MAX) and (vel_r < V_MAX)): 
            vel_l += 200
            vel_r += 200
            print("Left:  %s", vel_l)
            print("Right:  %s", vel_r)
            time.sleep(0.2)
    if keyboard.is_pressed('x'):
        if ((vel_l > V_MAX_BACK) and (vel_r > V_MAX_BACK)): 
            vel_l -= 200
            vel_r -= 200
            print("Left:  %s", vel_l)
            print("Right:  %s", vel_r)
            time.sleep(0.2)
    if keyboard.is_pressed('s'): 
        vel_l = 0
        vel_r = 0
        print("Left:  %s", vel_l)
        print("Right:  %s", vel_r)
        time.sleep(0.2)
    #Lenken und vorwaerts
    if keyboard.is_pressed('a'):
        if ((vel_l > 0) and (vel_r > 0) and (vel_l < V_MAX) and (vel_r < V_MAX)):
            vel_r += 200
            print("Left:  %s", vel_l)
            print("Right:  %s", vel_r)
            time.sleep(0.2)
    if keyboard.is_pressed('d'):
        if ((vel_l > 0) and (vel_r > 0) and (vel_l < V_MAX) and (vel_r < V_MAX)): 
            vel_l += 200
            print("Left:  %s", vel_l)
            print("Right:  %s", vel_r)
            time.sleep(0.2)
    #Lenken und rueckwaerts
    if keyboard.is_pressed('a'):
        if ((vel_l < 0) and (vel_r < 0) and (vel_l < V_MAX) and (vel_r < V_MAX)):
            vel_l += 200
            print("Left:  %s", vel_l)
            print("Right:  %s", vel_r)
            time.sleep(0.2)
    if keyboard.is_pressed('d'):
        if ((vel_l < 0) and (vel_r < 0) and (vel_l < V_MAX) and (vel_r < V_MAX)): 
            vel_r += 200
            print("Left:  %s", vel_l)
            print("Right:  %s", vel_r)
            time.sleep(0.2)
    
    #client.write_single_register(VEL_LEFT_ADDR, vel_l)
    #client.write_single_register(VEL_RIGHT_ADDR, vel_r)
        