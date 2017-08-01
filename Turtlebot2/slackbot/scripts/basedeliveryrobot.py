#!/usr/bin/env python
import os
import sys
import time
from slackclient import SlackClient
from nltk.tag import pos_tag

import rospy
from std_msgs.msg import String
from slackbot.srv import *

import setNavGoal as ng

# bot's ID as an environment variable
BOT_ID = os.environ.get("BOT_ID")
AT_BOT = "<@" + BOT_ID + ">"
slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
rospy.init_node('slackbot', anonymous=False)
pub = rospy.Publisher('/dstate', String, queue_size=10)

'''def sendItem(item):
	pub = rospy.Publisher('slackitem', String, queue_size=10)
	rate = rospy.Rate(10) # 10hz
	pub.publish(str(item))'''

def sendGoal(loc):
	try:

		clearCostMap()

		nav = ng.GoToPose()
	
		position = {'x': loc[0], 'y' : loc[1]}
	        quaternion = {'r1' : loc[2], 'r2' : loc[3], 'r3' : loc[4], 'r4' : loc[5]}
	
		success = nav.goto(position,quaternion)
	
		if success:
		    rospy.loginfo("Reached destination")
	        else:
	            rospy.loginfo("FAILED")
	
	except rospy.ROSInterruptException:
        	rospy.loginfo("Ctrl-C caught. Quitting")

	
def clearCostMap():
	rospy.wait_for_service('move_base/clear_costmaps')
	try:
		clear_costmaps = rospy.ServiceProxy('move_base/clear_costmaps',Empty)
		clear_costmaps()
	except rospy.ServiceException, e:
		print "Service call failed %s"%e
'''**************
Slack bot methods
**************'''

def handle_command(command, channel, points):
    if("deliver" in command):
	pub.publish(str("deliver"))
    else:
	pub.publish(str("fetch"))
    try:
	slack_client.api_call("chat.postMessage", channel=channel,
                          text="Thanks! Your order will soon be delivered", as_user=True)
        sendGoal(point_list[command.split(' ', 1)[1]])
    except rospy.ROSInterruptException:
       pass
    response = "Your order has been delivered!"
    slack_client.api_call("chat.postMessage", channel=channel,
                          text=response, as_user=True)
    return False


def parse_slack_output(slack_rtm_output):
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and AT_BOT in output['text']:
                # return text after the @ mention, whitespace removed
                return output['text'].split(AT_BOT)[1].strip(), \
                       output['channel']
    return None, None


if __name__ == "__main__":
    rate = rospy.Rate(10)
    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
    f = open('/home/nvidia/catkin_ws/src/Electron/Turtlebot2/slackbot/scripts/points.txt', 'r')
    point_list = eval(str('{')+f.readline()+str('}'))
    print(point_list)
    if slack_client.rtm_connect():
        print("Bot connected and running!")
        while True:
	    try:
		    command, channel = parse_slack_output(slack_client.rtm_read())
		    if command and channel:
		        handle_command(command, channel, point_list)
		    time.sleep(READ_WEBSOCKET_DELAY)
	    except KeyboardInterrupt:
		    print "fdsad"
		    sys.quit()
    else:
        print("Connection failed. Invalid Slack token or bot ID?")
