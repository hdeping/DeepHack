#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-
 
"""

============================

    @author       : Deping Huang
    @mail address : xiaohengdao@gmail.com
    @date         : 2019-06-21 14:08:56
                    2019-06-23 00:05:36
                    2019-06-23 19:27:55
    @project      : test adb screencap
    @version      : 0.1
    @source file  : main.py

============================
"""

import os
import cv2
from PIL import Image
from io import StringIO
import subprocess

import numpy as np

from TrainSVM import TrainSVM



class TestScreencap():
    """docstring for TestScreencap"""
    def __init__(self):
        super(TestScreencap, self).__init__()
        command = "/Users/huangdeping/Library/Android/sdk/platform-tools/adb"
        # self.command = "%s shell screencap -p"%(command)
        self.command = "%s shell screencap -p"%(command)
        self.command = self.command.split(" ")
        policy = "%s shell input tap %d 1500"
        self.policy = [policy%(command,180),policy%(command,900)]
        self.operator = 0
        # screenshot
        self.screen = None
        self.train = TrainSVM()
    def get_screen(self):
        # get the result from the command
        screen = subprocess.Popen(self.command, stdout=subprocess.PIPE)
        # data transfer
        screen,err = screen.communicate()

        # string buffer to numpy array
        screen = np.frombuffer(screen,np.uint8)
        # numpy to cv2
        screen = cv2.imdecode(screen,cv2.COLOR_RGB2GRAY)
        # crop the image
        screen = screen[1080:1680]
        print(screen.shape)
        
        # convert BGR to gray mode
        screen = cv2.cvtColor(screen,cv2.COLOR_BGR2GRAY)
        # resize from (600,1080) to (30,54)
        self.screen = cv2.resize(screen,(54,30))
        
        print(self.screen.shape)
        
    def run(self):
        score = 0
        while 1:
            self.get_screen()
            y = self.train.predict(self.screen)[0]
            if y:
                self.operator = 1 - self.operator
            # cut the wood
            os.system(self.policy[self.operator])
            # cv2.imshow("screenshot of MI 8",self.screen)

            # key = cv2.waitKey(1) & 0xFF
            # # ESC or "q"
            # if key == 27 or chr(key) == "q":
            #     break

        cv2.destroyAllWindows()
control = TestScreencap()
control.get_screen()
control.run()
