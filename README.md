# agri 

## Step-1
  Connect to Raspberry pi via ssh (wi-fi)<br>
  Type the following in terminal
  ```
  ssh pi@raspberrypi.local
  ```

## Step-2
Source the workspace
```
cd catkin_ws
source devel/setup.bash
```

## Step-3
Launch the agri.launch file to runn all sensor nodes
```
roslaunch minor agri.launch
```

## Step-4 
For send_to_server.py <br>
Open browser and see the agri data
```
http://rpi-ip-address:8080
```

## Step-5
For send_to_thing.py <br>
Login to thingspeak account and got your key->private view <br>
Every 15 sec data will updated <br>

![image](https://github.com/Jagadeesh-pradhani/agri/assets/97280653/2c6e4516-fde9-4d7e-bc3e-20c9045eaff5)


## Nodes
  1) Mositure sensor node
  2) Server node

