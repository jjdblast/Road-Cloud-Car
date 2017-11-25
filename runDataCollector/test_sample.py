#!/usr/bin/env python

import time
import numpy
import csv
from datetime import datetime

import rospy
import message_filters
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy, Image
# ROS Image message -> OpenCV2 image converter
from cv_bridge import CvBridge, CvBridgeError
import cv2

## init class
vel_cmd = Twist()
bridge = CvBridge()

## path
img_save_path = "/media/nvidia/UUI/rcc_data/images/"
twist_save_path = "/media/nvidia/UUI/rcc_data/twists/"
## define image topic
image_topic = "/usb_cam/image_raw"
twist_topic = "jetsoncar_teleop_joystick/cmd_vel"

def data_collector(img_msg, twist_msg):
    ## ros msg to cv2 image
    cv2_img = bridge.imgmsg_to_cv2(img_msg, "bgr8")
    ## throte
    vel_cmd.linear.x = twist_msg.linear.x
    ## steering
    vel_cmd.angular.z = twist_msg.angular.z
    ## timestamp
    (dt, micro) = datetime.now().strftime('%Y%m%d%H%M%S.%f').split('.')
    str_timestamp = str("%s%03d" % (dt, int(micro) / 1000))
    
    ## dump data
    img_filename = img_save_path + "Cam1_" + str_timestamp + ".jpg"
    twist_filename = twist_save_path + "Twist1_" + str_timestamp + ".csv"
    cv2.imwrite(img_filename, cv2_img)
    # open a file for writing.
    with open(twist_filename, 'wb') as csvfile:
        twistwriter = csv.writer(csvfile, delimiter=',')
	## throte, steering
        twistwriter.writerow([round(vel_cmd.linear.x, 5), round(vel_cmd.angular.z, 5)])
    #print("time=" + str_timestamp)
    #print("throte=%.5f, steering=%.5f") % (vel_cmd.linear.x, vel_cmd.angular.z)
    

def listener():
    rospy.init_node('test_sample', anonymous=True)
    img_msg = message_filters.Subscriber(image_topic, Image)
    twist_msg = message_filters.Subscriber(twist_topic, Twist)
    ts = message_filters.ApproximateTimeSynchronizer([img_msg, twist_msg], 10, 5, allow_headerless=True)
    ts.registerCallback(data_collector)
    rospy.spin()


if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
	pass




