#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

import sys, select, termios, tty, time

class Synchronize:
    def callback_twist(self, data):
    	print('twist callback')
   	self.twist = data

    def callback_item(self, data):
    	print('item callback')
	self.item = str(data)
    	if "0" in data and self.state is "deliver":
        	print('set to 0')
        	self.twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
        	self.twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
	self.send_item = True
    
    def callback_state(self, data):
    	print('twist callback')
   	self.state = data

    def __init__(self):
	
	#self.pub_msg = Twist()
	self.item = ""
	self.twist = Twist()
	self.send_twist = False
	self.send_item = False
	self.state = "deliver"

	rospy.Subscriber('/cmd_vel', Twist, self.callback_twist)
    	rospy.Subscriber('/item', String, self.callback_item)
	rospy.Subscriber('/dstate', String, self.callback_item)

	pub = rospy.Publisher("/cmd_vel_mux/input/teleop", Twist, queue_size=5)
	
	while not rospy.is_shutdown():
		if self.send_item:
			pub.publish(self.twist)
			self.send_twist = False
			self.send_item = False

if __name__ == '__main__':
	rospy.init_node("syncro")
	try:
	   sync = Synchronize()
	except rospy.ROSInterruptException: pass
