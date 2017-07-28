<p align="center">
  <img src="https://github.com/NVIDIA-Jetson/turtlebot3/blob/master/images/electron.png">
</p>

**The code in this repository has only been tested on the NVIDIA Jetson TX2. For installation instructions please scroll down to the installation section**

# The project overview
This is the GitHub repo for Electron, a delivery robot. The goal of the robot is to succefully be able to deliver items to cubicles in an office building be it office supplies or food. The robot must be able to autonomously drive around a building while successfully retrieving and delivering these items, constantly, upon user request. We do this with the help of ROS, deep learning, and various other smart sensors.

## Hardware Expectations
  * Turtlebot
  * RPLidar A1
  * Jetson TX2
  * Logitech C920 Webcam
  * USB Hub (optional)

## Navigating on Turtlebot
In order to move around a building autonomously, our robot creates a map of the building using SLAM with an RPLidar A1 and odometry and later, utilizes the same map to navigate throughout the building by localizing itself. We do most of this through ROS (Robot Operating System) and we are able to visualize all of this with RVIZ.

<p align="center">
  <img src="http://i.imgur.com/cF9dbGn.png">
</p>

## Making your delivery bot more aware: Using ItemNet trained on top of GoogleNet
Because we want our robot to be smarter, you want the robot to know when an object is placed or taken off of it and what the object is, so that it can act accordingly. ItemNet is a neural network trained on NVIDIA DIGITS with the Caffe framework on high-end NVIDIA GPUs. It has the ability to classify various classes of objects you find in an office space. We were able to learn how to do this from the ground up by following Dusty's tutorial on Jetson Inference.
https://github.com/dusty-nv/jetson-inference 

> Below is an example of the visualization of the training of one of our models. We ended up using the transfer learning method and used GoogleNet as a base network to train upon for our image classification. We also used data from the ImageNet Challenge to train. You can access this data by going to the ImageNet Challenge website. All information about how to train such models is on the linked repo above although we do have models that you can use in our repo right now which you can use for your bot.
<p align="center">
  <img src="http://i.imgur.com/yvEDrfE.png">
</p>

## User Interface: using a slackbot
In our project, we use a slackbot to request the robot to go somewhere. We thought this was a simple and easy way anyone in an office environment could request the bot or some other food or item. We used the slackclient api as well as nltk (Natural Language Toolkit) to process user commands and respond to them.
<p align="center">
  <img src="http://i.imgur.com/nyPYhMP.png">
</p>

# Installation

## Setting up your catkin workspace and installing ROS Kinetic dependencies

## Setting up ItemNet
Make sure that you cd into your ```catkin_ws``` and also make sure that you have run ```catkin_make```. Then, `cd catkin_ws/build/Electron/Turtlebot2/jetson-inference/aarch64/bin`.

Finally, run the following:
`./imagenet-camera`

Keep this running in the background because you will need it when you start up the navigation (next step)

## Starting up navigation

## Getting the slackbot up and running
To create a slackbot, you will first need to create a slack team. Go to slack.com and create you own slack team.

Now go to https://my.slack.com/services/new/bot to create a new slackbot. After this, get the token from slack:

<p align="center">
  <img src="http://i.imgur.com/9NQbjPZ.png">
</p>

The above token has been hidden but when you normally go to the page, you'll find a token. Now copy that token.

`cd catkin_ws/src/Electron/Turtlebot2/slackbot/scripts`

Now you can `export SLACK_BOT_TOKEN='ADD_YOUR_TOKEN_HERE'`

Now run `python base_print_bot_id.py `

Finally, run the the following commands:

`
cd
gedit .bashrc
`

Now, edit the file by adding the following lines:

`
export SLACK_BOT_TOKEN='ADD_YOUR_TOKEN_HERE'
export BOT_ID='ADD_BOT_ID_FROM_THE_PYTHON_SCRIPT'
`

You are now ready to run the slackbot.

`
cd catkin_ws/src/Electron/Turtlebot2/slackbot/scripts
rosrun slackbot basedeliveryrobot.py
`

You can now go to slack and message it by doing "@deliveryrobot LOCATION" and specifying the location based on what you added to `points.txt`
