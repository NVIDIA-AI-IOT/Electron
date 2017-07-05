# Electron
This is the GitHub repo for Electron, a delivery robot. The goal of the robot is to succefully be able to deliver items to cubicles in an office building be it office supplies or food. The robot must be able to autonomously drive around a building while successfully retrieving and delivering these items, constantly.

# Setting up your Jetson as SBC 
We are using the Jetson TX2 as the SBC (Single Board Computer) to control the turtlebot3 waffle. The Dynamixel motors on the Turtlebot3 are controlled by the OpenCR board. The OpenCR board connection is an ACM port to the Jetson, which is disabled in the kernel, and so is the cp210 port to the HLS-LFCD LDS lidar that comes with the Turtlebot. In order to reconfigure the kernel, first flash your Jetson with Jetpack 3.0. Follow the instructions [here](http://www.jetsonhacks.com/2017/03/21/jetpack-3-0-nvidia-jetson-tx2-development-kit/). 

Next, follow the Jetsonhacks instructions [here](http://www.jetsonhacks.com/2017/03/25/build-kernel-and-modules-nvidia-jetson-tx2/) to reconfigure the kernel and stop after running 
`./getKernelSources.sh`
The last line 
`make xconfig` 
will bring up the GUI for kernel configuration. Enable the ACM and cp210 ports: 
![](https://github.com/NVIDIA-Jetson/Electron/blob/master/common/kernelcp210.png)
![](https://github.com/NVIDIA-Jetson/Electron/blob/master/common/kernelcp210.png)

Make sure to save your changes to the config file, and go through the rest of the instructions to finish making the kernel. If no errors occur, reboot the Jetson. Plug in your OpenCR board and Lidar, and `cd /dev` in terminal. If the kernel reconfiguration worked, you should be able to see 'ttyACM0' and 'ttyUSB0'. 

# LegNet
Because we need our robot to be able to not bump into things, we decided to create LegNet. LegNet is a neural network trained on NVIDIA DIGITS with the Caffe framework on high-end NVIDIA GPUs. It has the ability to detect people's legs. The reason we wanted to create this neural network is because legs were one of the few moving objects in the hallways of an office building. Although there are many other objects we need to move around, legs and people are one of the few moving objects in the building. This newtwork can be used not only to move around people's legs but can also be used to identify people when delivering objects. We were able to learn how to do this from the ground up by following Dusty's tutorial on Jetson Inference.
https://github.com/dusty-nv/jetson-inference

