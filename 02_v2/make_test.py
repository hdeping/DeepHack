#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-
 
"""

============================

    @author       : Deping Huang
    @mail address : xiaohengdao@gmail.com
    @date         : 2019-06-23 10:15:14
    @project      : make data for the woodcutter game
    @version      : 0.1
    @source file  : make_test.py

============================
"""

# print(binary(tmp_var))
fp = open("0.png","rb")
data = fp.read()
# print(data)
from PIL import Image

from io import StringIO
import cv2
import numpy as np

# data = StringIO(data)
# img_arr = Image.open(data)

# data = cv2.imdecode(data, cv2.LOAD_IMAGE_COLOR)
data = np.frombuffer(data,np.uint8)
print(data.shape)
img = cv2.imdecode(data,cv2.COLOR_RGB2GRAY)
img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
print(img.shape)
cv2.imshow("test",img[1080:1680])
key = cv2.waitKey(0)