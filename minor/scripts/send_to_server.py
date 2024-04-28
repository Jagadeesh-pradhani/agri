#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32
import socket
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

HOST = '0.0.0.0'  # Listen on all network interfaces
PORT = 8080  # Choose a port you want to use
global x
x=0


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        subscriber()
        global x

        # HTML to display received data
        html = """
        <html>
        <head><title>Raspberry Pi Data</title></head>
        <body>
            <h1>Moisture Data</h1>
            <p>{}</p>
        </body>
        </html>
        """.format(x)

        self.wfile.write(html.encode('utf-8'))

def callback(data):
    global x
    x = data.data
    return

def subscriber():
    rospy.init_node('Server_node', anonymous=True)
    rospy.Subscriber('moist_data', Float32 , callback)
    time.sleep(0.1)
    return

def start_server():
    server_address = (HOST, PORT)
    httpd = HTTPServer(server_address, RequestHandler)
    print('Server running on {}:{}'.format(HOST, PORT))
    httpd.serve_forever()


if __name__ == '__main__':
    start_server()



