#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32
import requests  # Import requests library for HTTP calls

def callback(data):
  """
  This function is called whenever a new message is received on the /moist_data topic.
  It sends the moisture data to ThingSpeak using the API key and channel ID.
  """
  # Replace with your ThingSpeak API key and channel ID
  thingspeak_api_key = "3YXOPN3GBY4QJQ1R"
  thingspeak_channel_id = "2553991"

  # Prepare the URL for sending data to ThingSpeak
  #append '&field2={val}' for 2 values
  url = f"https://api.thingspeak.com/update?api_key={thingspeak_api_key}&field1={data.data}"   

  # Send data to ThingSpeak using a POST request
  response = requests.post(url)

  # Check for successful response
  if response.status_code == 200:
    print(f"Moisture data sent to ThingSpeak successfully! Response: {response.text}")
  else:
    print(f"Error sending data to ThingSpeak. Status code: {response.status_code}")

def main():
  """
  This function initializes a ROS node, subscribes to the /moist_data topic, and spins the ROS event loop.
  """
  rospy.init_node('moist_data_subscriber')

  # Subscribe to the /moist_data topic
  sub = rospy.Subscriber('/moist_data', Float32, callback)

  # Spin the ROS event loop
  rospy.spin()

if __name__ == '__main__':
  main()

