#!/usr/bin/env python

import time
import numpy
from datetime import datetime
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy
#import tensorflow as tf
import cv2


vel_cmd = Twist()

## define the target numpy arrays
## 1000 images in one txt files
target_sampling = numpy.zeros(shape=[1000,3], dtype=tf.float32)


def sample():
    # Constant (Do not change)
    CV_CAP_PROP_FRAME_WIDTH = 3
    CV_CAP_PROP_FRAME_HEIGHT = 4
    data_direction = "/home/yichen/Work/Human_Following/data/img_ros/"

    # Image size of capture
    IMAGE_HEIGHT = 240
    IMAGE_WIDTH = 320

    # Sample frequqncy (Hz)
    SAMPLE_RATE = 1

    def base_vel_callback(twist):
        (dt, micro) = datetime.now().strftime('%Y%m%d%H%M%S.%f').split('.')
        str_timestamp = str("%s%03d" % (dt, int(micro) / 1000))

        vel_cmd.linear.x = twist.linear.x
        vel_cmd.linear.y = twist.angular.y
        vel_cmd.angular.z = twist.angular.z

    cmd_vel_sub = rospy.Subscriber(
        "base_plate/cmd_vel", Twist, base_vel_callback, queue_size=1)

    # Init ros node
    rospy.init_node("data_aquizition", anonymous=True)
    sample_rate = rospy.Rate(SAMPLE_RATE)

    cam1 = cv2.VideoCapture(0)

    # define index
    index = 0

    while not rospy.is_shutdown():

        # Filenames
        (dt, micro) = datetime.now().strftime('%Y%m%d%H%M%S.%f').split('.')
        str_timestamp = str("%s%03d" % (dt, int(micro) / 1000))

        filename1 = data_direction + "Cam1_" + str_timestamp + ".jpg"

        # Start time point to captures
        start_time = time.time()
        # Capture frames
        ret1, frame1 = cam1.read()

        capture_time = time.time() - start_time
        # Save frames to images
        # cv2.imwrite(filename1, frame1)

        rospy.Subscriber("base_plate/cmd_vel", Twist,
                         base_vel_callback, queue_size=1)

        loop_time = time.time() - start_time
        print("Start @ t = %6f, Capture in %1f ms, Loop timer: %6f ms" % (
            start_time, 1000 * capture_time, 1000 * loop_time))
        print "time=" + str_timestamp
        print"vx=%.3f, vy=%.3f, wz=%.3f" % (
            vel_cmd.linear.x,
            vel_cmd.linear.y,
            vel_cmd.angular.z)


        sample_rate.sleep()

if __name__ == '__main__':
    try:
        sample()
    except rospy.ROSInterruptException:
pass




