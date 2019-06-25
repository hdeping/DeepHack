#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-
 
"""

============================

    @author       : Deping Huang
    @mail address : xiaohengdao@gmail.com
    @date         : 2019-06-23 22:50:33
                    2019-06-25 02:39:39
    @project      : hacker for WoodCutter
    @version      : 0.1
    @source file  : TrainSVM.py

============================
"""
from sklearn import svm
import joblib
import  os
import cv2
import numpy as np

# train a svm classifier
class TrainSVM():
    """docstring for TrainSVM"""
    def __init__(self):
        super(TrainSVM, self).__init__()
        # train data and test data
        self.__version__ = "0.1.0"
        self.__author__ = "Deping Huang"
        self.train_data  = []
        self.test_data   = []
        # labels
        self.train_label = []
        self.test_label  = []
        # svm model
        self.model = svm.LinearSVC()
        # load model
        self.loadModel()
        # self.model = svm.SVC()
        # data list
        self.data_list = {}
        # train list and test list
        self.train_list = []
        self.test_list = []
        # three kinds of labels
        # data type
        self.datatype = ["left","right","over"]
        # labels 
        self.labels = {"left":0,"right":1,"over":2}
        # 80% of the data are used for training
        # and 20% of the data are used for testing
        self.proportion = 0.99

    # input_sample: (30,54)
    def predict(self,input_sample):
        input_sample = np.array(input_sample)
        input_sample = input_sample.reshape((1,60*32))
        # preparing the model 
        res = self.model.predict(input_sample)
        return res

    def train(self):
        # prepare for the data
        print("preparing for the data")
        
        self.makeData()

        print("data is prepared now")

        # train the model
        self.model.fit(self.train_data,self.train_label)
        self.saveModel()
        # self.loadModel()
        # predict the test data
        predict_label = self.model.predict(self.test_data)
        print(predict_label)
        print(self.test_label)
    
    # save model into pkl file    
    def saveModel(self):
        filename = "model/svm1.pkl"
        print("save model into file %s"%(filename))
        path = "model"
        if not os.path.exists(path):
            os.system("mkdir %s"%(path))
        
        with open(filename,"wb") as fp:
            joblib.dump(self.model,fp)

    # load model parameters from a pkl file
    def loadModel(self):
        filename = "model/svm1.pkl"
        print("load model from file %s"%(filename))
        path = "model"
        if not os.path.exists(path):
            os.system("mkdir %s"%(path))
        
        with open(filename,"rb") as fp:
            self.model = joblib.load(fp)


    # get data from the disk
    # stay,tran,over
    def makeData(self):
        # prepare the file list
        self.getDataList()
        # read image file with opencv
        self.train_data = self.readData(self.train_list)
        self.test_data = self.readData(self.test_list)

        
        print(self.train_data.shape)
        print(self.test_data.shape)
        print(self.train_label.shape)
        print(self.test_label.shape)
    
    # read image
    def readImage(self,image_name):
        img = cv2.imread(image_name)
        # BGR to Gray
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        return img

    def readData(self,name_list):
        array = []
        for line in name_list:
            img = self.readImage(line)
            array.append(img)
            # display the image
            # if self.showImage(img):
            #     break
        
        # transform into numpy array
        array = np.array(array)
        array = array.reshape((-1,60*32))
        return array

    def showImage(self,img):
        cv2.imshow("image",img)
        key = cv2.waitKey(0)
        if chr(key) == "q":
            return 1 
        else:
            return 0

    # get the list of train data as well as test data
    def getDataList(self):
        # initialize the dictionary for the data files
        for type in self.datatype:
            self.data_list[type] = 0
            self.getFileList(type)

        # print(self.data_list)
        # split the data into two parts: train and test
        self.splitData()
        
    def splitData(self):
        # number of training data for each type
        thresholds = {}
        lengths = {}
        for type in self.datatype:
            # print(type)
            lengths[type] = len(self.data_list[type])
            thresholds[type] = int(lengths[type]*self.proportion)
        # print(thresholds)

        # get the train list and test list
        for type in self.datatype:
            # train list
            for i in range(thresholds[type]):
                self.train_list.append(self.data_list[type][i])
                self.train_label.append(self.labels[type])

            # test list
            for i in range(thresholds[type],lengths[type]):
                self.test_list.append(self.data_list[type][i])
                self.test_label.append(self.labels[type])

        # transform into numpy array
        self.test_label = np.array(self.test_label)
        self.train_label = np.array(self.train_label)
        # print(self.train_list)
        # print(self.test_list)
        # print(len(self.train_list))
        # print(len(self.test_list))
        
    # get the file list of the specific label data
    def getFileList(self,type):
        # get the path
        path = "data/%s/*png"%(type)
        # get the png file list of the path
        command = "ls %s"%(path)
        file_list = os.popen(command)
        file_list = file_list.read().split("\n")
        # get rid of the final element which is null
        file_list.pop()
        self.data_list[type] = file_list
