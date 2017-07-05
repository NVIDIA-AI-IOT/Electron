# Electron
This is the GitHub repo for Electron, a delivery robot. The goal of the robot is to succefully be able to deliver items to cubicles in an office building be it office supplies or food. The robot must be able to autonomously drive around a building while successfully retrieving and delivering these items, constantly.

# LegNet
Because we need our robot to be able to not bump into things, we decided to create LegNet. LegNet is a neural network trained on NVIDIA DIGITS with the Caffe framework on high-end NVIDIA GPUs. It has the ability to detect people's legs. The reason we wanted to create this neural network is because legs were one of the few moving objects in the hallways of an office building. Although there are many other objects we need to move around, legs and people are one of the few moving objects in the building. This newtwork can be used not only to move around people's legs but can also be used to identify people when delivering objects. We were able to learn how to do this from the ground up by following Dusty's tutorial on Jetson Inference.
https://github.com/dusty-nv/jetson-inference
