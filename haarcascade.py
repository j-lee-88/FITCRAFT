import numpy as np
import cv2
import translateskin

from ast import literal_eval as make_tuple
from PIL import Image
from translateskin import draw_shirt
from translateskin import torso_2, left_leg_2, right_leg_2, left_leg, right_leg, left_shoe, right_shoe


def quantize(rectangle):
    im = Image.open(image_path)
    width, height = im.size

    #left = rectangle[2]
    #top = rectangle[3]
    #right = rectangle[0]
    #bottom = rectangle[1]
    left = rectangle[0]
    top = rectangle[1]
    right = rectangle[0]+rectangle[2]
    bottom = rectangle[1]+rectangle[3]

    (im.crop((left, top, right, bottom))).save('temp.jpg')

def find_color(weights):
    quantize(weights)
    
    img = cv2.imread('temp.jpg')
    #img = cv2.cvtColor(image, cv2.COLOR_BGR2Lab)
    #img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    #img = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)

    x, y = img.shape[:2]
    return img[x//2, y//2]

#find largest confidence rectangle since multiple objects can be detected with same confidence
def largest_confident_rectangle(detections, weights):
    if len(weights) > 0:
        minWeight = weights[np.argmin(weights)]
        maxWeight = weights[np.argmax(weights)]
        minRectangleList = []
        maxRectangleList = []
        #place all rectangles with min/max confidence in their respective lists
        for i in range(len(weights)):
            if (weights[i] == minWeight):
                minRectangleList.append(detections[i])
            elif(weights[i] == maxWeight):
                maxRectangleList.append(detections[i])

        #find the largest max confident rectangle
        maxConfidenceSize = 0
        maxConfidenceRectangle = (0,0,0,0)
        for local in maxRectangleList:
            local_large = local[2] * local[3]
            if local_large > maxConfidenceSize:
                maxConfidenceSize = local_large
                maxConfidenceRectangle = local
        
        #find the largest min confident reactangle
        minConfidenceSize = 0
        minConfidenceRectangle= (0,0,0,0)
        for local in minRectangleList:
            local_large = local[2] * local[3]
            if local_large > minConfidenceSize:
                minConfidenceSize = local_large
                minConfidenceRectangle = local

        #print(maxConfidenceRectangle, minConfidenceRectangle)
        #print(maxConfidenceSize, minConfidenceSize)
        return maxConfidenceRectangle, minConfidenceRectangle, maxConfidenceSize, minConfidenceSize
    else:
        return [], [], 0, 0

#image processing
#shirtCascade = cv2.CascadeClassifier('haarcascade1/cascade.xml')
#shirtCascade = cv2.CascadeClassifier('haarcascade2/cascade.xml')
#pantsCascade = cv2.CascadeClassifier('pantshaarcascade/cascade.xml')
#pantsCascade = cv2.CascadeClassifier('pantshaarcascade2/cascade.xml')
pantsCascade = cv2.CascadeClassifier('pantshaarcascade3/cascade.xml')
shirtCascade = cv2.CascadeClassifier('shirtcascade/cascade.xml')
shoeCascade = cv2.CascadeClassifier('shoecascade/cascade.xml')
image_path = 'examples/tshirtpants.jpeg'
image = cv2.imread(image_path)
finalSkin = ""

#Color space experimentation

#BGR
##cv2.imshow('image', image)
##cv2.waitKey(0)
##cv2.destroyAllWindows()

#LAB = CIE
##image = cv2.cvtColor(image, cv2.COLOR_BGR2Lab)
##cv2.imshow('image', image)
##cv2.waitKey(0)
##cv2.destroyAllWindows()

#HSV
##image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
##cv2.imshow('image', image)
##cv2.waitKey(0)
##cv2.destroyAllWindows()

#Close approximation to YUV
##image = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
##cv2.imshow('image', image)
##cv2.waitKey(0)
##cv2.destroyAllWindows()

image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

shirtDetections, shirtReject, shirtWeights = shirtCascade.detectMultiScale3(gray, scaleFactor=1.09, minNeighbors=0, flags=0, outputRejectLevels=True)
shirtMaxCon, shirtMinCon, shirtMaxRectSize, shirtMinRectSize = largest_confident_rectangle(shirtDetections, shirtWeights)

pantsDetections, pantsReject, pantsWeights = pantsCascade.detectMultiScale3(gray, scaleFactor=1.07, minNeighbors=0, flags=0, outputRejectLevels=True)
pantsMaxCon, pantsMinCon, pantsMaxRectSize, pantsMinRectSize = largest_confident_rectangle(pantsDetections, pantsWeights)

shoeDetections, shoeReject, shoeWeights = shoeCascade.detectMultiScale3(gray, scaleFactor=1.07, minNeighbors=0, flags=0, outputRejectLevels=True)
shoeMaxCon, shoeMinCon, shoeMaxRectSize, shoeMinRectSize = largest_confident_rectangle(shoeDetections, shoeWeights)

min_shirt_weight, max_shirt_weight = (10, 0), (0, 0)
min_pants_weight, max_pants_weight = (10, 0), (0, 0)
min_shoe_weight, max_shoe_weight = (10, 0), (0, 0)

i = 1.01
avg_shirt_weight, avg_pants_weight, avg_shoe_weight = (0, 0), (0, 0), (0, 0)

bestMinShirt = []
bestMaxShirt = []
bestMinPants = []
bestMaxPants = []
bestMinshoe = []
bestMaxshoe = []

while i < 1.5:
    shirtDetections, shirtReject, shirtWeights = shirtCascade.detectMultiScale3(gray, scaleFactor=i, minNeighbors=0, flags=0, outputRejectLevels=True)
    shirtMaxCon, shirtMinCon, shirtMaxRectSize, shirtMinRectSize = largest_confident_rectangle(shirtDetections, shirtWeights)
    if (len(shirtWeights) > 0):
        avg_shirt_weight = sum(shirtWeights)/len(shirtWeights)

    pantsDetections, pantsReject, pantsWeights = pantsCascade.detectMultiScale3(gray, scaleFactor=i, minNeighbors=0, flags=0, outputRejectLevels=True)
    pantsMaxCon, pantsMinCon, pantsMaxRectSize, pantsMinRectSize = largest_confident_rectangle(pantsDetections, pantsWeights)
    if (len(pantsWeights) > 0):
        avg_pants_weight = sum(pantsWeights)/len(pantsWeights)

    shoeDetections, shoeReject, shoeWeights = shoeCascade.detectMultiScale3(gray, scaleFactor=i, minNeighbors=0, flags=0, outputRejectLevels=True)
    shoeMaxCon, shoeMinCon, shoeMaxRectSize, shoeMinRectSize = largest_confident_rectangle(shoeDetections, shoeWeights)
    if (len(shoeWeights) > 0):
        avg_shoe_weight = sum(shoeWeights)/len(shoeWeights)

    if avg_shirt_weight < min_shirt_weight[0]:
        min_shirt_weight = (avg_shirt_weight, i)
    if avg_shirt_weight > max_shirt_weight[0]:
        max_shirt_weight = (avg_pants_weight, i)
    if avg_pants_weight < min_pants_weight[0]:
        min_pants_weight = (avg_pants_weight, i)
    if avg_pants_weight > max_pants_weight[0]:
        max_pants_weight = (avg_pants_weight, i)
    if avg_shoe_weight < min_shoe_weight[0]:
        min_shoe_weight = (avg_shoe_weight, i)
    if avg_shoe_weight > max_shoe_weight[0]:
        max_shoe_weight = (avg_shoe_weight, i)

    i+=0.02

print("Max shirt weight and scale factor")
print(max_shirt_weight)
print("Min pants weight and scale factor")
print(min_shirt_weight)
print("Max pants weight and scale factor")
print(max_pants_weight)
print("Min pants weight and scale factor")
print(min_pants_weight)
print("Max shoe weight and scale factor")
print(max_shoe_weight)
print("Min shoe weight and scale factor")
print(min_shoe_weight)

print(shirtMaxRectSize, shirtMinRectSize, pantsMaxRectSize, pantsMinRectSize)
#draw rectangle for detected objects if they exist and don't include if it's not at least 40,000 pixels since that is likely too small

#print("test: " + str(minShirtScale))
shirtDetections, shirtReject, shirtWeights = shirtCascade.detectMultiScale3(gray, scaleFactor=min_shirt_weight[1], minNeighbors=0, flags=0, outputRejectLevels=True)
shirtMaxCon, shirtMinCon, shirtMaxRectSize, shirtMinRectSize = largest_confident_rectangle(shirtDetections, shirtWeights)

pantsDetections, pantsReject, pantsWeights = pantsCascade.detectMultiScale3(gray, scaleFactor=min_pants_weight[1], minNeighbors=0, flags=0, outputRejectLevels=True)
pantsMaxCon, pantsMinCon, pantsMaxRectSize, pantsMinRectSize = largest_confident_rectangle(pantsDetections, pantsWeights)

shoeDetections, shoeReject, shoeWeights = shoeCascade.detectMultiScale3(gray, scaleFactor=min_shoe_weight[1], minNeighbors=0, flags=0, outputRejectLevels=True)
shoeMaxCon, shoeMinCon, shoeMaxRectSize, shoeMinRectSize = largest_confident_rectangle(shoeDetections, shoeWeights)

#shirts
if len(shirtWeights) > 0 and shirtMinRectSize > 40000:
    #cv2.rectangle(image, (shirtMaxCon[0], shirtMaxCon[1]), (shirtMaxCon[0] + shirtMaxCon[2], shirtMaxCon[1] + shirtMaxCon[3]), (0,255,0), 3)
    cv2.rectangle(image, (shirtMinCon[0], shirtMinCon[1]), (shirtMinCon[0] + shirtMinCon[2], shirtMinCon[1] + shirtMinCon[3]), (0,255,0), 3)
    cv2.imshow('examples/jacket_1.jpg', image)
    cv2.waitKey(0)
else:
    print("no shirt found")
#pants
if len(pantsWeights) > 0 and pantsMinRectSize > 10000:
    #cv2.rectangle(image, (pantsMaxCon[0], pantsMaxCon[1]), (pantsMaxCon[0] + pantsMaxCon[2], pantsMaxCon[1] + pantsMaxCon[3]), (0,255,0), 3)
    cv2.rectangle(image, (pantsMinCon[0], pantsMinCon[1]), (pantsMinCon[0] + pantsMinCon[2], pantsMinCon[1] + pantsMinCon[3]), (0,255,0), 3)
    cv2.imshow('examples/jacket_1.jpg', image)
    cv2.waitKey(0)
else:
    print("no pants found")

#shoes
if len(shoeWeights) > 0 and shoeMinRectSize > 24000:
    cv2.rectangle(image, (shoeMaxCon[0], shoeMaxCon[1]), (shoeMaxCon[0] + shoeMaxCon[2], shoeMaxCon[1] + shoeMaxCon[3]), (0,255,0), 3)
    cv2.rectangle(image, (shoeMinCon[0], shoeMinCon[1]), (shoeMinCon[0] + shoeMinCon[2], shoeMinCon[1] + shoeMinCon[3]), (0,255,0), 3)
    cv2.imshow('examples/jacket_1.jpg', image)
    cv2.waitKey(0)
else:
    print("no shoe found")

#quantize
if len(shirtWeights) > 0 and shirtMinRectSize > 10000:
    #parse pixel color and convert to integers
    shirtColor = find_color(shirtMinCon)
    stringTuple = str(shirtColor)
    stringTuple = stringTuple.replace('  ', ' ')
    newTuple = stringTuple.split(" ")
    firstNumString = newTuple[0].split("[")
    secondNumString = newTuple[1]
    thirdNumString = newTuple[2].split("]")
    #print(stringTuple)
    firstNum = int(firstNumString[1])
    secondNum = int(secondNumString)
    thirdNum = int(thirdNumString[0])

    finalSkin = draw_shirt("default.png", finalSkin, torso_2, (firstNum,secondNum,thirdNum))

if len(pantsWeights) > 0 and pantsMinRectSize > 10000:
    pantsColor = find_color(pantsMinCon)
    stringTuple = str(pantsColor)
    stringTuple = stringTuple.replace('  ', ' ')
    newTuple = stringTuple.split(" ")
    firstNumString = newTuple[0].split("[")
    secondNumString = newTuple[1]
    thirdNumString = newTuple[2].split("]")
    
    firstNum = int(firstNumString[1])
    secondNum = int(secondNumString)
    thirdNum = int(thirdNumString[0])

    finalSkin = draw_shirt("default.png", finalSkin, left_leg, (firstNum, secondNum, thirdNum))
    finalSkin = draw_shirt("default.png", finalSkin, right_leg, (firstNum, secondNum, thirdNum))

if len(shoeWeights) > 0 and shoeMinRectSize > 24000:
    shirtColor = find_color(shoeMinCon)
    stringTuple = str(shirtColor)
    newTuple = stringTuple.split(" ")
    firstNumString = newTuple[0].split("[")
    secondNumString = newTuple[1]
    thirdNumString = newTuple[2].split("]")
    
    firstNum = int(firstNumString[1])
    secondNum = int(secondNumString)
    thirdNum = int(thirdNumString[0])

    finalSkin = draw_shirt("default.png", finalSkin, left_shoe, (firstNum, secondNum, thirdNum))
    finalSkin = draw_shirt("default.png", finalSkin, right_shoe, (firstNum, secondNum, thirdNum))
