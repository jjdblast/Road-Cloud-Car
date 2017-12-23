#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import Twist # This is the message type the robot uses for velocities

import rospy
from geometry_msgs.msg import Twist
from math import pi

class test_velo_ctl():
    def __init__(self):
        # Give the node a name
        rospy.init_node('test_velo_ctl', anonymous=False)
        # Set rospy to execute a shutdown function when exiting       
        rospy.on_shutdown(self.shutdown)
        
        # Publisher to control the robot's speed
        self.cmd_vel = rospy.Publisher('/jetsoncar_teleop_joystick/cmd_vel', Twist, queue_size=10)
        #self.cmd_vel = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

        # How fast will we update the robot's movement?
        rate = 10 
        # Set the equivalent ROS rate variable
        r = rospy.Rate(rate)
        
        # Set the forward linear speed to 0.2 meters per second 
        linear_speed = 0.2
        # Set the travel distance to 1.0 meters
        goal_distance = 1
        # How long should it take us to get there?
        linear_duration = goal_distance / linear_speed
       
	# Initialize the movement command
	move_cmd = Twist()
	# Set the forward speed
	move_cmd.linear.x = linear_speed
	# Move forward for a time to go the desired distance
	ticks = int(linear_duration * rate)

	for t in range(ticks):
	    rospy.loginfo("Sending commands")
	    self.cmd_vel.publish(move_cmd)
	    r.sleep()

        # Stop the RCC
        self.cmd_vel.publish(Twist())
        
    def shutdown(self):
        # Always stop the robot when shutting down the node.
        rospy.loginfo("Stopping the robot...")
        self.cmd_vel.publish(Twist())
        rospy.sleep(1)
 
def run():
    try:
        test_velo_ctl()
    except:
        rospy.loginfo("test_velo_ctl node terminated.")

if __name__ == '__main__':
    run()
