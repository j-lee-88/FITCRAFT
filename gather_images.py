import urllib.request
import cv2
import numpy as numpy
import os
import tensorflow as tf
import keras

from keras.datasets import fashion_mnist
from PIL import Image, ImageOps

#load data in variables
(trainX, trainY), (testX, testY) = fashion_mnist.load_data()

#load data into shirt values
print("train: ", (trainX.shape))
print("test: ", testX.shape)

#print("y values: ", testY)
#print("testx: ", testX)
count = 0
for x in range(10000):
    if (testY[x] == 0):
        #save shirt into folder
        img = "'{}'.jpg".format(count)
        con = Image.fromarray(testX[x])
        convert = ImageOps.invert(con)
        convert.save(img)
        count += 1