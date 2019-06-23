#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-
 
"""

============================

    @author       : Deping Huang
    @mail address : xiaohengdao@gmail.com
    @date         : 2019-06-23 10:40:45
    @project      : make data for the gamer training
    @version      : 0.1
    @source file  : makeData.py

============================
"""

import cv2
# class for labelling the data
# get_image
#    get the image after cropped
# save_image
#    save the image into the assigned directory
# labelling the data
#    There are three kinds of status
#    stay: 1, stay in the current position 
#    tran: 2, get into the another position
#    over: 3, game over
class DataLabelling():
    """docstring for DataLabelling"""
    def __init__(self):
        super(DataLabelling, self).__init__()
        # image array
        self.img = None
        # the label of the image
        self.label = "stay"
        # image name
        self.image_name = None
    
    # get the image
    def getImage(self):
        # read the image
        img = cv2.imread(self.image_name)
        # crop the image
        self.img = img[1080:1680]
        

    # save the image
    def saveImage(self):
        # get the correct path
        path = "data/%s/%s"%(self.label,self.image_name)
        # convert BGR to gray mode
        self.img = cv2.cvtColor(self.img,cv2.COLOR_BGR2GRAY)
        # resize from (600,1080) to (30,54)
        self.img = cv2.resize(self.img,(54,30))
        # write the image into the path
        cv2.imwrite(path,self.img)

        # keys info
        self.keys = {}
        self.keys["j"] = 0
        self.keys["k"] = 0
        self.keys["i"] = 0
        self.keys["E"] = 0

    # get the labels
    def getLabels(self):

        for i in range(0,250):
            self.image_name = "%d.png"%(i)
            # read the image
            self.getImage()
            cv2.imshow("label",self.img)
            key = cv2.waitKey(0)
            print(i,key,chr(key),self.img.shape)

            # label the current image
            if chr(key) == "j":
                self.label = "stay"
                self.saveImage()
            elif chr(key) == "k":
                self.label = "tran"
                self.saveImage()
            elif chr(key) == "i":
                self.label = "over"
                self.saveImage()
            else:
                key = ord("E")
                print("key error")
            self.keys[chr(key)] += 1
            
                
        cv2.destroyAllWindows()
        print("keys: ",self.keys)
        

label = DataLabelling()
label.getLabels()


