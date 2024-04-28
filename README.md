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
Open browser and see the agri data
```
http://rpi-ip-address:8080
```

## Nodes
  1) Mositure sensor node
  2) Server node

