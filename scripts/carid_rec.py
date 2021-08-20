#!/usr/bin/python3
from __future__ import print_function
from license_plate_recognition.srv import carsrv,carsrvResponse
import rospy
import numpy as np 
from carid_recongnition import *

#get information from srv request
def Automatic_license_plate_recognition(req):
    image_data = np.frombuffer(req.image.data, dtype='uint8').reshape((req.image.height, req.image.width, 3))
    print("success get the req!")
    car_inf=recognition_carid(image_data)
    #return srv response
    return carsrvResponse(car_inf[0][0],car_inf[0][2][0],car_inf[0][2][1],car_inf[0][2][2],car_inf[0][2][3])

#set node and get srv request
def get_car_inf_server():
    rospy.init_node('carid_rec')
    s = rospy.Service('carid_rec_srv', carsrv, Automatic_license_plate_recognition)
    print("Ready to recognize license plate.")
    rospy.spin()

#get car information from image
def recognition_carid(img):
    car_id=HyperLPR_plate_recognition(img)
    print(car_id)
    return car_id

if __name__ == "__main__":
    get_car_inf_server()
