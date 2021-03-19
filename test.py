import numpy as np
import cv2
import tensorflow as tf
import keras
import random

from PIL import Image, ImageOps

from keras.datasets import fashion_mnist
from haarcascade import largest_confident_rectangle


#image processing
pantsCascade = cv2.CascadeClassifier('pantshaarcascade3/cascade.xml')
shirtCascade = cv2.CascadeClassifier('shirtcascade/cascade.xml')
shoeCascade = cv2.CascadeClassifier('shoecascade/cascade.xml')

stringCount = ""

shirtCount = 0
falseShirt = 0
pantsCount = 0
falsePants = 0
shoeCount = 0
falseShoe = 0

shirtAccuracy = 0.0
pantsAccuracy = 0.0
shoeAccuracy = 0.0

count = 0
randomList = [-1]
r = -1
#shirts
for x in range(1000):
    while (r in randomList):
        r = random.randint(0, 999)
    randomList.append(r)
    if (count % 2 == 0):
        stringCount = "shirts/" + str(r) + ".jpg"
    else:
        stringCount = "neg/" + str(r) + ".jpg"

    print(stringCount)
    
    image_path = stringCount
    image = cv2.imread(image_path)

    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    shirtDetections, shirtReject, shirtWeights = shirtCascade.detectMultiScale3(gray, scaleFactor=1.09, minNeighbors=0, flags=0, outputRejectLevels=True)
    shirtMaxCon, shirtMinCon, shirtMaxRectSize, shirtMinRectSize = largest_confident_rectangle(shirtDetections, shirtWeights)

    min_shirt_weight, max_shirt_weight = (10, 0), (0, 0)
    avg_shirt_weight = 0.0

    bestMinShirt = []
    bestMaxShirt = []

    i = 1.01
    while i < 1.5:
        shirtDetections, shirtReject, shirtWeights = shirtCascade.detectMultiScale3(gray, scaleFactor=i, minNeighbors=0, flags=0, outputRejectLevels=True)
        shirtMaxCon, shirtMinCon, shirtMaxRectSize, shirtMinRectSize = largest_confident_rectangle(shirtDetections, shirtWeights)
        if (len(shirtWeights) > 0):
            avg_shirt_weight = sum(shirtWeights)/len(shirtWeights)

        #print("avg:" + avg_shirt_weight)
        #print("min:" + min_shirt_weight)
        if avg_shirt_weight < min_shirt_weight[0]:
            min_shirt_weight = (avg_shirt_weight, i)
        if avg_shirt_weight > max_shirt_weight[0]:
            max_shirt_weight = (avg_shirt_weight, i)

        i+=0.02
    
    shirtDetections, shirtReject, shirtWeights = shirtCascade.detectMultiScale3(gray, scaleFactor=min_shirt_weight[1], minNeighbors=0, flags=0, outputRejectLevels=True)
    shirtMaxCon, shirtMinCon, shirtMaxRectSize, shirtMinRectSize = largest_confident_rectangle(shirtDetections, shirtWeights)

    if len(shirtWeights) > 0 and (count % 2 == 0):
        shirtCount+=1
    elif len(shirtWeights) > 0 and (count % 2 == 1):
        falseShirt +=1

    count+=1
    
count = 0
randomList.clear()
randomList.append(-1)
r -= 1
#pants
for x in range(1000):
    while (r in randomList):
        r = random.randint(0, 999)
    randomList.append(r)
    if (count % 2 == 0):
        stringCount = "pants/" + str(r) + ".jpg"
    else:
        stringCount = "neg/" + str(r) + ".jpg"
    
    print(stringCount)

    image_path = stringCount
    image = cv2.imread(image_path)

    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    pantsDetections, pantsReject, pantsWeights = pantsCascade.detectMultiScale3(gray, scaleFactor=1.07, minNeighbors=0, flags=0, outputRejectLevels=True)
    pantsMaxCon, pantsMinCon, pantsMaxRectSize, pantsMinRectSize = largest_confident_rectangle(pantsDetections, pantsWeights)

    min_pants_weight, max_pants_weight = (10, 0), (0, 0)
    avg_pants_weight = 0.0

    bestMinPants = []
    bestMaxPants = []

    i = 1.01
    while i < 1.5:
        pantsDetections, pantsReject, pantsWeights = pantsCascade.detectMultiScale3(gray, scaleFactor=i, minNeighbors=0, flags=0, outputRejectLevels=True)
        pantsMaxCon, pantsMinCon, pantsMaxRectSize, pantsMinRectSize = largest_confident_rectangle(pantsDetections, pantsWeights)
        if (len(pantsWeights) > 0):
            avg_pants_weight = sum(pantsWeights)/len(pantsWeights)
        if avg_pants_weight < min_pants_weight[0]:
            min_pants_weight = (avg_pants_weight, i)
        if avg_pants_weight > max_pants_weight[0]:
            max_pants_weight = (avg_pants_weight, i)

        i+=0.02
    pantsDetections, pantsReject, pantsWeights = pantsCascade.detectMultiScale3(gray, scaleFactor=min_pants_weight[1], minNeighbors=0, flags=0, outputRejectLevels=True)
    pantsMaxCon, pantsMinCon, pantsMaxRectSize, pantsMinRectSize = largest_confident_rectangle(pantsDetections, pantsWeights)

    if len(pantsWeights) > 0 and (count % 2 == 0):
        pantsCount+=1
    elif len(pantsWeights) > 0 and (count % 2 == 1):
        falsePants+=1
    
    count+=1

count = 0
randomList.clear()
randomList.append(-1)
r -= 1
#shoes
count = 0
for x in range(1000):
    while (r in randomList):
        r = random.randint(0, 999)
    randomList.append(r)
    if (count % 2 == 0):
        stringCount = "shoes/" + str(r) + ".jpg"
    else:
        stringCount = "neg/" + str(r) + ".jpg"
    
    print(stringCount)

    image_path = stringCount
    image = cv2.imread(image_path)

    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    shoeDetections, shoeReject, shoeWeights = shoeCascade.detectMultiScale3(gray, scaleFactor=1.07, minNeighbors=0, flags=0, outputRejectLevels=True)
    shoeMaxCon, shoeMinCon, shoeMaxRectSize, shoeMinRectSize = largest_confident_rectangle(shoeDetections, shoeWeights)

    min_shoe_weight, max_shoe_weight = (10, 0), (0, 0)

    i = 1.01
    avg_shoe_weight = 0.0

    bestMinshoe = []
    bestMaxshoe = []

    while i < 1.5:
        shoeDetections, shoeReject, shoeWeights = shoeCascade.detectMultiScale3(gray, scaleFactor=i, minNeighbors=0, flags=0, outputRejectLevels=True)
        shoeMaxCon, shoeMinCon, shoeMaxRectSize, shoeMinRectSize = largest_confident_rectangle(shoeDetections, shoeWeights)
        if (len(shoeWeights) > 0):
            avg_shoe_weight = sum(shoeWeights)/len(shoeWeights)
        if avg_shoe_weight < min_shoe_weight[0]:
            min_shoe_weight = (avg_shoe_weight, i)
        if avg_shoe_weight > max_shoe_weight[0]:
            max_shoe_weight = (avg_shoe_weight, i)

        i+=0.02

    shoeDetections, shoeReject, shoeWeights = shoeCascade.detectMultiScale3(gray, scaleFactor=min_shoe_weight[1], minNeighbors=0, flags=0, outputRejectLevels=True)
    shoeMaxCon, shoeMinCon, shoeMaxRectSize, shoeMinRectSize = largest_confident_rectangle(shoeDetections, shoeWeights)

    if len(shoeWeights) > 0 and (count % 2 == 0):
        shoeCount+=1
    elif len(shoeWeights) > 0 and (count % 2 == 1):
        falseShoe +=1
    
    count+=1


shirtAccuracy = shirtCount / 500
falseShirtAccuracy =  falseShirt / 500
pantsAccuracy = pantsCount / 500
falsePantsAccuracy = falsePants / 500
shoeAccuracy = shoeCount / 500
falseShoeAccuracy = falseShoe / 500

print("Shirt accuracy: " + str(shirtAccuracy))
print("False shirt accuracy: " + str(falseShirtAccuracy))
print("Pants accuracy: " + str(pantsAccuracy))
print("False pants accuracy: " + str(falsePantsAccuracy))
print("Shoe accuracy: " + str(shoeAccuracy))
print("False shoe accuracy: " + str(falseShoeAccuracy))