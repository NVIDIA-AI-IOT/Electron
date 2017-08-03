<p align="center">
  <img src="https://github.com/NVIDIA-Jetson/turtlebot3/blob/master/images/electron.png">
</p>

**The code in this repository has only been tested on the NVIDIA Jetson TX2. For installation instructions please look to installation guide in the wiki [here](https://github.com/NVIDIA-Jetson/Electron/wiki/Installation)**

# The project overview
This is the GitHub repo for Electron, an indoor delivery robot. The goal of the robot is to deliver items to cubicles in an office building, be it office supplies or food. The robot must be able to autonomously drive around a building while successfully retrieving and delivering these items constantly upon user request. We do this using ROS, deep learning, and various sensors.

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
In order to move around a building autonomously, our robot creates a map of the building using SLAM (gmapping) with an RPLidar A1 and odometry. It later utilizes the same map to navigate throughout the building by localizing itself using AMCL (adaptive monte carlo localization). We do most of this using ROS (Robot Operating System) and RVIZ for visualization.

<p align="center">
  <img src="http://i.imgur.com/cF9dbGn.png">
</p>

## Making your delivery bot more aware: Using ItemNet trained on top of GoogleNet
We added a neural network for the robot to know what kind of object is placed on it and when an object is placed or taken off- so it can act accordingly. ItemNet is a neural network trained on NVIDIA DIGITS with the Caffe framework on high-end NVIDIA GPUs. It has the ability to classify various classes of objects you find in an office space. We were able to learn how to do this from the ground up by following Dusty's tutorial on Jetson Inference.
https://github.com/dusty-nv/jetson-inference 

Below is an example of the visualization of the training of one of our models. We used transfer learning with GoogleNet as a base network to train upon for our image classification. We also used data from the ImageNet Challenge to train. You can access this data by going to the ImageNet Challenge website. All information about how to train such models is on the linked repo above, although we included models in this repo that can be implemented directly on your bot.
<p align="center">
  <img src="http://i.imgur.com/yvEDrfE.png">
</p>

## User Interface: using a slackbot
In our project, we use a slackbot to request the robot to go somewhere. We thought this was a simple and easy way anyone in an office environment could request the bot or some other food or item. We used the slackclient api.
<p align="center">
  <img src="http://i.imgur.com/nyPYhMP.png">
</p>
