#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-
 
"""

============================

    @author       : Deping Huang
    @mail address : xiaohengdao@gmail.com
    @date         : 2019-06-21 14:08:56
                    2019-06-23 00:05:36
    @project      : test adb screencap
    @version      : 0.1
    @source file  : main.py

============================
"""

import os
import cv2
from PIL import Image
from io import StringIO


class TestScreencap():
    """docstring for TestScreencap"""
    def __init__(self):
        super(TestScreencap, self).__init__()
        command = "/Users/huangdeping/Library/Android/sdk/platform-tools/adb"
        self.command = "%s shell screencap -p"%(command)
    def get_screen(self):
        # screen = os.popen(self.command, mode = "rb").read()
        screen = os.popen(self.command, mode = "r").read()
        
        # binary to string
        screen = StringIO(screen)
        # string to PIL array
        screen = Image.open(screen)
        # PIL array to numpy array
        screen = np.array(screen)
        return screen

    def run(self):
        while 1:
            screen = self.get_screen()
            cv2.imshow("screenshot of MI 8",screen)
            key = cv2.waitKey(1)
            # ESC or "q"
            if key == 27 or key == 113:
                break

        cv2.destroyAllWindows()
control = TestScreencap()
screen = control.get_screen()
# control.run()