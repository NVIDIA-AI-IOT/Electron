#!/usr/bin/env python

import rospy

from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy

import sys, select, termios, tty, time
print("herro")

rospy.init_node('turtlebot2_drive')
pub = rospy.Publisher('/cmd_vel_mux/input/teleop', Twist, queue_size=5)

def callback(data):
    print(data)
    pub.publish(data)

def listener():
    rospy.Subscriber('/cmd_vel', Twist, callback)
    rospy.spin()

if __name__=="__main__":
    listener()
 	
