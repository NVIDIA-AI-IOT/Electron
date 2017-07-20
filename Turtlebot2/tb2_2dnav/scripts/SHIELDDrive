#!/usr/bin/env python

import rospy

from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy

import sys, select, termios, tty, time

rospy.init_node('turtlebot3_teleop')
pub = rospy.Publisher('/cmd_vel_mux/input/teleop', Twist, queue_size=5)
throttle = 0.0
turn = 0.0

twist = Twist()

def clip(lo, x, hi):
    return lo if x <= lo else hi if x >= hi else x

def callback(data):
    global throttle, turn, twist 
    
    #throttle = clip(-0.09, data.axes[1], 0.09)
    #throttle = clip(-0.18, data.axes[1], 0.18)
    throttle = clip(-1, data.axes[1], 1) * 2
    turn = data.axes[3] * 2

    twist.linear.x = throttle; twist.linear.y = 0; twist.linear.z = 0
    twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = turn
    pub.publish(twist)

    print (throttle)
    print (turn)

def listener():
    rospy.Subscriber('/joy', Joy, callback)
    rospy.spin()

if __name__=="__main__":
    listener()
 	
