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

## 
