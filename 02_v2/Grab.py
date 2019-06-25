#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-
 
"""

============================

    @author       : Deping Huang
    @mail address : xiaohengdao@gmail.com
    @date         : 2019-06-24 09:41:17
                    2019-06-25 01:33:55
    @project      : grab the screen
    @version      : 0.1
    @source file  : Grab.py

============================
"""

from PIL import ImageGrab
import cv2
import time
import numpy as np


# class for grabing the screen
class GrabScreen():
    """docstring for GrabScreen"""
    def __init__(self):
        super(GrabScreen, self).__init__()
    def grab(self):
        x = 36  
        y = 462   
        width = 300 
        height = 160
        screen = ImageGrab.grab([x,y,x+width,y+height])
        screen = np.array(screen)
        screen = cv2.cvtColor(screen,cv2.COLOR_RGB2BGR)
        screen = cv2.cvtColor(screen,cv2.COLOR_BGR2GRAY)
        # write the image
        # cv2.imwrite("image%d.png"%(index),screen)
        # print(index,screen.shape)
        return screen

    def run(self):
        for i in range(500):
            self.grab(i+1)
        
# grab = GrabScreen()

# grab.run()
