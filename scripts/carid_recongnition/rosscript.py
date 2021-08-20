#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image as sensor_Image
import plate_detector
from  plate_detector import detector_inference #这儿替换模型
import cv2
from .hyperlpr import LPR
import numpy as np
import time
from os import path
import json

class ROSNode():
    def __init__(self):
        rospy.init_node(name="input_datastream",anonymous=True)
        self.topic_subscriber_parm=rospy.get_param("~image_input")
        self.topic_publisher=rospy.Publisher("/Car_plate",String,queue_size=5)


    def image_subscriber(self):
        rospy.Subscriber(self.topic_subscriber_parm,sensor_Image,self.callback)
        rospy.spin()

    def callback(self,img_msg):
        Detect_Result=detector_inference(img_msg)
        self.topic_publisher.publish(Detect_Result)

if __name__ == '__main__':

    try:
        while not rospy.is_shutdown():
            image = ROSNode()
            image.image_subscriber()

    except rospy.ROSException:
        pass






