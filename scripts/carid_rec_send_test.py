#!/usr/bin/env python3
#coding utf-8
#from __future__ import print_function
import os
import sys
import rospy
import cv2
from license_plate_recognition.srv import *
from sensor_msgs.msg import Image
import numpy as np
import platform 

#get the path of the srv class which we need to send
#add the path to the system path
root_dir = os.path.abspath('.')
srv_path='devel/lib/python2.7/dist-packages/license_plate_recognition/srv'
srv_path=os.path.join(root_dir,srv_path)
sys.path.append(srv_path)

#get srv class
from _carsrv import carsrvRequest

#get image information
def publish_image(imgdata):
    image_temp = Image()
    image_temp.encoding = 'rgb8'
    image_temp.data = np.array(imgdata).tostring()
    image_temp.height = imgdata.shape[0]
    image_temp.width = imgdata.shape[1]
    return image_temp




def send_image(srv_send):
    #wait for service
    rospy.wait_for_service('carid_rec_srv')
    try:
        #send our srv request and get srv Response
        carid_rec_srv = rospy.ServiceProxy('carid_rec_srv', carsrv)
        resp = carid_rec_srv(srv_send)
        print(resp.carid)
        return resp

    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)


if __name__ == "__main__":
    #read local picture for test
    #we can use 'print(root_dir = os.path.abspath('.'))' to see the root directory
    #we can locate the required files from the root directory
    img = cv2.imread('src/license_plate_recognition/scripts/test_pic/test1.jpg')
    imagedata = publish_image(img)
    print("client get image")
    
    
    #define the srv object which we need to send
    image_send=carsrvRequest()

    image_send.image=imagedata
    image_info=send_image(image_send)

    # show image and frame
    cv2.rectangle(img, (image_info.left,image_info.top ), (image_info.right,image_info.bottom), (0, 255, 0), 2)
    cv2.imshow("image", img)
    cv2.waitKey(0)

