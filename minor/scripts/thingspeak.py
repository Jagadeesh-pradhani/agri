#python thingspeak.py

import thingspeak
import time

channel_id = 2553991 # put here the ID of the channel you created before
write_key = '3YXOPN3GBY4QJQ1R' # update the "WRITE KEY"


def measure(channel):
    temp=1
    try:
        response = channel.update({'field1': temp})
        temp=temp+1
        if temp > 10:
            temp=1
    except:
           print("connection failure")

if __name__ == "__main__":
        channel = thingspeak.Channel(id=channel_id, write_key=write_key)
        while True:
            measure(channel)
        #free account has a limitation of 15sec between the updates
            time.sleep(15)