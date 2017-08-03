#!/usr/bin/env python

import rospy
import actionlib
import geometry_msgs
import sys
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import Pose, Point, Quaternion, PoseWithCovarianceStamped
from actionlib_msgs.msg import *

class GoToPose():
    def __init__(self):
	
        self.goal_sent = False
	
	# What to do if shut down (e.g. Ctrl-C or failure)
	rospy.on_shutdown(self.shutdown)
	
	# Tell the action client that we want to spin a thread by default
	self.move_base = actionlib.SimpleActionClient("move_base", MoveBaseAction)
	rospy.loginfo("Wait for the action server to come up")

	# Allow up to 5 seconds for the action server to come up
	self.move_base.wait_for_server(rospy.Duration(5))

    def goto(self, pos, quat):
	
        # Send a goal
        self.goal_sent = True
	goal = MoveBaseGoal()
	goal.target_pose.header.frame_id = 'map'
	goal.target_pose.header.stamp = rospy.Time.now()
        goal.target_pose.pose = Pose(Point(pos['x'], pos['y'], 0.000),
                                     Quaternion(quat['r1'], quat['r2'], quat['r3'], quat['r4']))

	try:	
		# Start moving
		self.move_base.send_goal(goal)
		rospy.loginfo("Goal Sent")

		# Allow TurtleBot up to 5 minutes to complete task
		success = self.move_base.wait_for_result(rospy.Duration(300)) 

		state = self.move_base.get_state()
		result = False

		rospy.loginfo("success: " + str(success))
		rospy.loginfo("state: " + str(state))
		if(not success): sys.exit()
		if success and state == GoalStatus.SUCCEEDED:
		    # We made it!
		    result = True
		else:
		    self.move_base.cancel_goal()

		self.goal_sent = False
	except KeyboardInterrupt:
		sys.exit()
        return result

    def shutdown(self):
        if self.goal_sent:
            self.move_base.cancel_goal()
        rospy.loginfo("Stop")
        rospy.sleep(1)

'''
if __name__ == '__main__':
    try:
        rospy.init_node('nav_test', anonymous=False)
        navigator = GoToPose()

        # Change the following values based on which coordinate you want to go to on the map! Usually only x and y need to be changed.
        position = {'x': 9.76595, 'y' : 4.42364}
        quaternion = {'r1' : 0.000, 'r2' : 0.000, 'r3' : 0.98473, 'r4' : 0.17403}

        rospy.loginfo("Go to (%s, %s) pose", position['x'], position['y'])
        success = navigator.goto(position, quaternion)

        if success:
            rospy.loginfo("YAYY, reached the desired pose")
        else:
            rospy.loginfo(":'( Base failed to reach the desired pose")

        # Sleep to give the last log messages time to be sent
        rospy.sleep(1)

    except rospy.ROSInterruptException:
        rospy.loginfo("Ctrl-C caught. Quitting")
'''
