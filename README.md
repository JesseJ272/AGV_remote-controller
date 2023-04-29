# AGV_remote-controller
The repository contains a simple python-script that lets you control an AGV with your keyboard.


# Description
Prerequisites:
	-AGV (differential drive) with PLC running ModbusTCP-Server
	-Server-address and addresses of your following PLC-registers:
  	-one register for the value of the target value for the left wheel velocity (int)
  	-one register for the value of the target value for the right wheel velocity (int)
