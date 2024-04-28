#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
from time import sleep



def publisher():
    rospy.init_node('moisture_node', anonymous=True)
    pub = rospy.Publisher('moist_data', Float32, queue_size=10)
    rate = rospy.Rate(1)  # 1 Hz

    # create the spi bus
    spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

    # create the cs (chip select)
    cs = digitalio.DigitalInOut(board.D5)

    # create the mcp object
    mcp = MCP.MCP3008(spi, cs)

    # create an analog input channel on pin 0
    chan = AnalogIn(mcp, MCP.P0)

    while not rospy.is_shutdown():
        #print("Raw ADC Value: ", chan.value)
        #print("ADC Voltage: " + str(chan.voltage) + "V")
        val = 100 - ((chan.voltage/3.3)*100)
        #print("Moisture = " + str(val) + "%")

        pub.publish(val)
        rate.sleep()


if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass




