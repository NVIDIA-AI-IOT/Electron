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
<<<<<<< HEAD:Turtlebot2/tb2_2dnav/scripts/ImageNet2Drive.py
    	if "0" in str(data):
=======
    	if "0" in data and self.state is "deliver":
>>>>>>> 3a900a9b13103ddd7107a955d98ea847013d9267:Turtlebot2/tb2_2dnav/scripts/ImageNetDrive.py
        	print('set to 0')
        	self.twist.linear.x = 0; self.twist.linear.y = 0; self.twist.linear.z = 0
        	self.twist.angular.x = 0; self.twist.angular.y = 0; self.twist.angular.z = 0
	self.send_item = True
    
    def callback_state(self, data):
    	print('twist callback')
   	self.state = data

    def __init__(self):
	
	#self.pub_msg = Twist()
	self.item = ""
	self.twist = Twist()
	self.send_item = False
	self.state = "deliver"

	rospy.Subscriber('/cmd_vel', Twist, self.callback_twist)
    	rospy.Subscriber('/item', String, self.callback_item)
<<<<<<< HEAD:Turtlebot2/tb2_2dnav/scripts/ImageNet2Drive.py
	
=======
	rospy.Subscriber('/dstate', String, self.callback_item)

>>>>>>> 3a900a9b13103ddd7107a955d98ea847013d9267:Turtlebot2/tb2_2dnav/scripts/ImageNetDrive.py
	pub = rospy.Publisher("/cmd_vel_mux/input/teleop", Twist, queue_size=5)
	
	while not rospy.is_shutdown():
		if self.send_item:
			pub.publish(self.twist)
<<<<<<< HEAD:Turtlebot2/tb2_2dnav/scripts/ImageNet2Drive.py
=======
			self.send_twist = False
>>>>>>> 3a900a9b13103ddd7107a955d98ea847013d9267:Turtlebot2/tb2_2dnav/scripts/ImageNetDrive.py
			self.send_item = False

if __name__ == '__main__':
	rospy.init_node("syncro")
	try:
	   sync = Synchronize()
	except rospy.ROSInterruptException: pass
