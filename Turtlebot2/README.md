# Description of Nodes

### Jetson-Inference
Node for image classification. This node is a deployed neural net model that we trained following [Two Days to a Demo](https://github.com/dusty-nv/jetson-inference). We trained the model off of ImageNet Challenge data to train for objects such as pens and computer mice. The node cannot yet be run with `rosrun`. To run, `catkin_make` in the catkin workspace and then navigate the `build` directory under the catkin workspace to find and run `./imagenet-camera`. The node publishes to the topic `/item` with a String that ends with a `0` or `1` that refers to whether an object is present respectively.
### Robot_Setup_tf
Scripts that make the tf transformations between `base_laser` and `base_link`; and `base_footprint` and `base_link`. Follow [this guide](http://wiki.ros.org/navigation/Tutorials/RobotSetup/TF) to learn how to setup and connect your tf tree. Should be merged into the TB2_2DNAV.
### RPLidar
The RPLidar node unchanged to publish scans to the topic `/scan`. [Reference here](https://github.com/robopeak/rplidar_ros) for the RoboPEAK repository.
### Slackbot
Node for sending navigation goals from slack. The package communicates with a created slackbot by exporting the `SLACK_BOT_TOKEN` and `BOT_ID` each time or by exporting the variables in `.bashrc` file. The slackbot sends an actionlib goal to the navigation stack.
### TB2_2DNAV
Includes all of the navigation stack. SLAM (Simultaneous Localization and Mapping) [gmapping](http://wiki.ros.org/gmapping) and [AMCL](http://wiki.ros.org/amcl) (Adaptive Monte Carlo Localization). The launch files also bringup the Turtlebot if the respective bringup is installed.
