#!/bin/sh
# Install the Jetson Car support files
# This includes the code for the Arduino Car interface
# The packages needed for installing ROS on an Arduino
# Joystick support for the Nyko game controller
# This repository
# git clone https://github.com/jetsonhacks/installJetsonCar.git

# Make the jetsonbot catkin workspace
./setupCatkinWorkspace.sh jetsoncar
cd ~/jetsoncar
sudo apt-get install arduino
sudo apt-get install ros-kinetic-joy -y
cd src
git clone https://github.com/jetsonhacks/jetsoncar_teleop.git
cd ..
catkin_make

# Copy Arduino code 
cd ~/jetsonhacks/installjetsoncar
cp -r ~/jetsonhacks/installjetsoncar/Arduino\ Firmware/* '/home/ubuntu/sketchbook'
sudo apt-get install ros-kinetic-rosserial-arduino ros-kinetic-rosserial ros-kinetic-angles -y
cd ~/sketchbook/libraries
rm -rf ros_lib
source ~/jetsoncar/devel/setup.bash
rosrun rosserial_arduino make_libraries.py ~/sketchbook/libraries
cd ~/jetsonhacks/installJetsonCar

