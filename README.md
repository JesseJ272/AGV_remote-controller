# AGV_remote-controller
The repository contains a simple python-script that lets you control an AGV with your keyboard.


# Description
## Prerequisites
<ul>
	<li>AGV (differential drive) with PLC running ModbusTCP-Server</li>
	<li>Server-address and addresses of your following PLC-registers</li>
		<ul>
			<li>one register for the value of the target value for the left wheel velocity (int) [m/min]</li>
 			<li>one register for the value of the target value for the right wheel velocity (int) [m/min]</li>
		</ul>
	<li>Ethernet/Wifi -connection between your AGV and the remote control device</li>
</ul>

## Setup
You can install this script by navigating to the folder where you want to install it and do a git clone.<br>
In cmd:<br>

```
cd </PATH/TO/YOUR/DIRECTORY>
git clone https://github.com/JesseJ272/AGV_remote-controller.git
```

After git clone open the python script with a code editor to configure the following parameters:
| parameter | format | description |
| --- | --- | --- |
| V_MAX | int | max velocity [m/min] for driving forward |
| V_MAX_BACK | int | max velocity [m/min] for driving backwards |
| VEL_LEFT_ADDR | int | register address for the PLC register where you want to write the left target velocity |
| VEL_RIGHT_ADDR | int | register address for the PLC register where you want to write the right target velocity |
| HOST_IP | string | IP address of your ModbusTCP server |
| PORT | int | port number of the server (default is 502) |


After configuration you can start the script.<br>
A command prompt like the following will open where you can control your AGV with your keyboard.<br>

![Screenshot of running remote_controller.py in cmd](https://github.com/JesseJ272/AGV_remote-controller/blob/main/remote_controller.png)

# Sources
Code from other authors used in this repository:<br>
<ul>
	<li>Editor: sourceperl</li>
	<li>Link to repository: https://github.com/sourceperl/pyModbusTCP</li>
</ul>

