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

<p align="center">
  <img src="http://i.imgur.com/8u2dQ3u.jpg">
</p>

## Navigating on Turtlebot
In order to move around a building autonomously, our robot creates a map of the building using SLAM with an RPLidar A1 and odometry and later, utilizes the same map to navigate throughout the building by localizing itself. We do most of this through ROS (Robot Operating System) and we are able to visualize all of this with RVIZ.

<p align="center">
  <img src="http://i.imgur.com/cF9dbGn.png">
</p>

## Making your delivery bot more aware: Using ItemNet trained on top of GoogleNet
Because we want our robot to be smarter, you want the robot to know when an object is placed or taken off of it and what the object is, so that it can act accordingly. ItemNet is a neural network trained on NVIDIA DIGITS with the Caffe framework on high-end NVIDIA GPUs. It has the ability to classify various classes of objects you find in an office space. We were able to learn how to do this from the ground up by following Dusty's tutorial on Jetson Inference.
https://github.com/dusty-nv/jetson-inference 

Below is an example of the visualization of the training of one of our models. We ended up using the transfer learning method and used GoogleNet as a base network to train upon for our image classification. We also used data from the ImageNet Challenge to train. You can access this data by going to the ImageNet Challenge website. All information about how to train such models is on the linked repo above although we do have models that you can use in our repo right now which you can use for your bot.
<p align="center">
  <img src="http://i.imgur.com/yvEDrfE.png">
</p>

## User Interface: using a slackbot
In our project, we use a slackbot to request the robot to go somewhere. We thought this was a simple and easy way anyone in an office environment could request the bot or some other food or item. We used the slackclient api as well as nltk (Natural Language Toolkit) to process user commands and respond to them.
<p align="center">
  <img src="http://i.imgur.com/nyPYhMP.png">
</p>
