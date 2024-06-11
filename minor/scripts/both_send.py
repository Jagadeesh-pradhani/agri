#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32, Int32
import requests
import time

# Global variables to store the latest sensor data
latest_moisture_data = 50.0
latest_temp_data = 29.0
persons = 0
Water = 0
cam = 0

# Replace with your ThingSpeak API key and channel ID
thingspeak_api_key = "3YXOPN3GBY4QJQ1R"
thingspeak_channel_id = "2553991"

def send_to_thingspeak():
    """
    Sends the moisture, temperature, water, and cam data to ThingSpeak using the API key and channel ID.
    """
    global latest_moisture_data, latest_temp_data, Water, cam

    if latest_moisture_data is not None and latest_temp_data is not None and Water is not None and cam is not None:
        # Prepare the URL for sending data to ThingSpeak
        url = f"https://api.thingspeak.com/update?api_key={thingspeak_api_key}&field1={latest_moisture_data}&field2={latest_temp_data}&field3={Water}&field4={cam}"

        # Send data to ThingSpeak using a POST request
        response = requests.get(url)

        # Check for successful response
        if response.status_code == 200:
            rospy.loginfo(f"Data sent to ThingSpeak successfully! Response: {response.text}")
        else:
            rospy.logerr(f"Error sending data to ThingSpeak. Status code: {response.status_code}")

def cam_callback(data):
    global cam
    global persons
    persons = data.data
    cam = 1 if persons != 0 else 0

def moisture_callback(data):
    """
    This function is called whenever a new message is received on the /moist_data topic.
    """
    global latest_moisture_data
    global Water
    latest_moisture_data = data.data
    Water = 1 if latest_moisture_data < 50 else 0
    rospy.loginfo(f"Received moisture data: {latest_moisture_data}")

def temp_callback(data):
    """
    This function is called whenever a new message is received on the /temp topic.
    """
    global latest_temp_data
    latest_temp_data = data.data
    rospy.loginfo(f"Received temperature data: {latest_temp_data}")

def timer_callback(event):
    """
    This function is called by the ROS timer every 15 seconds to send data to ThingSpeak.
    """
    send_to_thingspeak()

def main():
    """
    This function initializes a ROS node, subscribes to the /moist_data and /temp topics, and sets up a timer to periodically send data to ThingSpeak.
    """
    rospy.init_node('data_subscriber')
    global latest_moisture_data, latest_temp_data, Water, cam

    # Subscribe to the /persons, /moist_data, and /temp topics
    rospy.Subscriber('/persons', Int32, cam_callback)
    rospy.Subscriber('/moist_data', Float32, moisture_callback)
    rospy.Subscriber('/temp', Float32, temp_callback)

    # Create a timer to call the timer_callback function every 15 seconds
    rospy.Timer(rospy.Duration(15), timer_callback)

    # Spin the ROS event loop
    rospy.spin()

if __name__ == '__main__':
    main()
