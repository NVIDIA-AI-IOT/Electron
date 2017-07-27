#!/usr/bin/env python
import os
import time
from slackclient import SlackClient
from nltk.tag import pos_tag

import rospy
from std_msgs.msg import String

import setNavGoal as ng

# bot's ID as an environment variable
BOT_ID = os.environ.get("BOT_ID")
AT_BOT = "<@" + BOT_ID + ">"
slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))

'''def sendItem(item):
	pub = rospy.Publisher('slackitem', String, queue_size=10)
	rate = rospy.Rate(10) # 10hz
	pub.publish(str(item))'''

def sendGoal(loc):
	try:
		rospy.init_node('Goal', anonymous=False)

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

	

'''**************
Slack bot methods
**************'''

def handle_command(command, channel, points, location = False):
    response = "Oh so you want a "
    try:
        tagged_sent = pos_tag(command.split())
        propernouns = [word for word,pos in tagged_sent if pos == 'NN']
        if len(propernouns) is not 0: response+=str(propernouns[len(propernouns)-1])
        response+="! Is that correct?"
        if 'ye' in command and 'yel' not in command:
            print "yo"
            response = "Cool! What's your location?"
            slack_client.api_call("chat.postMessage", channel=channel,
                                  text=response, as_user=True)
            return True
        elif "no" in command:
            response = "Oh ok. What do you want then?"
            slack_client.api_call("chat.postMessage", channel=channel,
                                  text=response, as_user=True)
            return False

        if len(command.split()) is 1 and "Sorry" not in response and "Cool" not in response and "Is that correct" not in response:
            response = "please use more than one word to tell me what you want. I.E. get me some salad"
    except ValueError:
        response = "Sorry! I'm confused. Please tell me what you want again."
    if location:
        try:
	    slack_client.api_call("chat.postMessage", channel=channel,
                          text="Thanks! Your order will soon be delivered", as_user=True)
            sendGoal(point_list[command])
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
    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
    f = open('points.txt', 'r')
    point_list = eval(str('{')+f.readline()+str('}'))
    print(point_list)
    if slack_client.rtm_connect():
        print("Bot connected and running!")
        is_loc = False
	item = ""
	temp_item =''
        while True:
            command, channel = parse_slack_output(slack_client.rtm_read())
            if command and channel:
		temp_item = item
                is_loc = handle_command(command, channel, point_list, location = is_loc)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")
