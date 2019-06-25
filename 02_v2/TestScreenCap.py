#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-
 
"""

============================

    @author       : Deping Huang
    @mail address : xiaohengdao@gmail.com
    @date         : 2019-06-24 09:23:44
    @project      : hacker for WoodCutter
    @version      : 0.1
    @source file  : Testscreencap.py

============================
"""

import os
import cv2
from PIL import Image
from io import StringIO
import subprocess

import numpy as np

from TrainSVM import TrainSVM
from Grab import GrabScreen
import  pymouse 

# class for hacker
class TestScreenCap():
    """docstring for TestScreencap"""
    def __init__(self):
        super(TestScreenCap, self).__init__()
        self.operator = 0
        # screenshot
        self.screen = None
        self.train = TrainSVM()
        # self.train.train()
        self.grab = GrabScreen()
        # mouse click
        self.mouse = pymouse.PyMouse()
    def get_screen(self):
        # resize from (300,160) to (60,32)
        screen = self.grab.grab()
        self.screen = cv2.resize(screen,(60,32))
        
        #print(self.screen.shape)
        
    def run(self):
        score = 0
        while 1:
            self.get_screen()
            y = self.train.predict(self.screen)[0]
            if y == 0:
                self.mouse.click(90,560)
            elif y == 1:
                self.mouse.click(290,560)
            else:
                break

            # cut the wood
            score += 1
            print("score",score,y)
            
            # cv2.imshow("screenshot of MI 8",self.screen)

            # key = cv2.waitKey(1) & 0xFF
            # # ESC or "q"
            # if key == 27 or chr(key) == "q":
            #     break

        cv2.destroyAllWindows()
