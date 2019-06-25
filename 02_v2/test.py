#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-
 
"""

============================

    @author       : Deping Huang
    @mail address : xiaohengdao@gmail.com
    @date         : 2019-06-24 01:08:44
    @project      : test reading data
    @version      : 0.1
    @source file  : test.py

============================
"""

fp = open("new","rb")
data = fp.read()

import numpy as np
import cv2


data = np.frombuffer(data,np.uint8)
data = data[16:].reshape((2248,1080,4))
data = cv2.cvtColor(data,cv2.COLOR_RGBA2BGRA)
print(data.shape)

cv2.imshow("show",data)
key = cv2.waitKey(0)
cv2.destroyAllWindows()
