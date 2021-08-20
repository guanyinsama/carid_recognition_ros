#!/usr/bin/env python3
import sys
from hyperlpr import LPR
import os

def plate_recognition(Input_BGR,minSize=30,charSelectionDeskew=True , region = "CH"):
    return PR.plate_recognition(Input_BGR,minSize,charSelectionDeskew)

def img_processor():
    return

def detector_inference():
    return

PR = LPR(os.path.join(os.path.split(os.path.realpath(__file__))[0],"models"))

