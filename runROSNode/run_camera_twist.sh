#!/bin/bash

# 1. start xbox360 stick drive
# 2. start cmd_vel node
# 3. start camera node
xboxdrv && \
roslaunch jetsoncar_teleop nyko_teleop.launch && \
rosrun rosserial_python serial_node.py /dev/ttyUSB0 && \
rosrun usb_cam usb_cam_node
