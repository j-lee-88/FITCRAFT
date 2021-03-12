import numpy as np
import cv2

from PIL import Image


def quantize(rectangle):
    im = Image.open(image_path)
    width, height = im.size

    left = rectangle[2]
    top = rectangle[3]
    right = rectangle[0]
    bottom = rectangle[1]

    (im.crop((left, top, right, bottom))).save('temp.jpg')

def find_color(weights):
    quantize(weights)
    
    img = cv2.imread('temp.jpg')
    #img = cv2.cvtColor(image, cv2.COLOR_BGR2Lab)
    #img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    #img = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)

    Z = img.reshape((-1,3))
    Z = np.float32(Z)

    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    K = 1
    ret,label,center = cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

    center = np.uint8(center)
    res = center[label.flatten()]
    res2 = res.reshape((img.shape))

    cv2.imshow('res2', res2) 
    cv2.waitKey(0)

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

        print(maxConfidenceRectangle, minConfidenceRectangle)
        print(maxConfidenceSize, minConfidenceSize)
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
image_path = 'examples/redShirt.jpg'
image = cv2.imread(image_path)

#Color space experimentation

#BGR
cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#LAB = CIE
image = cv2.cvtColor(image, cv2.COLOR_BGR2Lab)
cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#HSV
image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Close approximation to YUV
image = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

shirtDetections, shirtReject, shirtWeights = shirtCascade.detectMultiScale3(gray, scaleFactor=1.09, minNeighbors=0, flags=0, outputRejectLevels=True)

shirtMaxCon, shirtMinCon, shirtMaxRectSize, shirtMinRectSize = largest_confident_rectangle(shirtDetections, shirtWeights)

pantsDetections, pantsReject, pantsWeights = pantsCascade.detectMultiScale3(gray, scaleFactor=1.07, minNeighbors=0, flags=0, outputRejectLevels=True)
pantsMaxCon, pantsMinCon, pantsMaxRectSize, pantsMinRectSize = largest_confident_rectangle(pantsDetections, pantsWeights)

min_shirt_weight, max_shirt_weight = (0, 0), (0, 0)
min_pants_weight, max_pants_weight = (0, 0), (0, 0)

i = 1.01
avg_shirt_weight, avg_pants_weight = (0, 0), (0, 0)

while i < 1.5:
    shirtDetections, shirtReject, shirtWeights = shirtCascade.detectMultiScale3(gray, scaleFactor=i, minNeighbors=0, flags=0, outputRejectLevels=True)
    shirtMaxCon, shirtMinCon, shirtMaxRectSize, shirtMinRectSize = largest_confident_rectangle(shirtDetections, shirtWeights)
    if (len(shirtWeights) > 0):
        avg_shirt_weight = sum(shirtWeights)/len(shirtWeights)

    pantsDetections, pantsReject, pantsWeights = pantsCascade.detectMultiScale3(gray, scaleFactor=i, minNeighbors=0, flags=0, outputRejectLevels=True)
    pantsMaxCon, pantsMinCon, pantsMaxRectSize, pantsMinRectSize = largest_confident_rectangle(pantsDetections, pantsWeights)
    if (len(pantsWeights) > 0):
        avg_pants_weight = sum(pantsWeights)/len(pantsWeights)

    if avg_shirt_weight < min_shirt_weight[0]:
        min_shirt_weight = (avg_shirt_weight, i)
    if avg_shirt_weight > max_shirt_weight[0]:
        max_shirt_weight = (avg_pants_weight, i)
    if avg_pants_weight < min_pants_weight[0]:
        min_pants_weight = (avg_pants_weight, i)
    if avg_pants_weight > max_pants_weight[0]:
        max_pants_weight = (avg_pants_weight, i)

    i+=0.02

print("Max shirt weight and scale factor")
print(max_shirt_weight)
print("Min pants weight and scale factor")
print(min_shirt_weight)
print("Max pants weight and scale factor")
print(max_pants_weight)
print("Min pants weight and scale factor")
print(min_pants_weight)

print(shirtMaxRectSize, shirtMinRectSize, pantsMaxRectSize, pantsMinRectSize)
#draw rectangle for detected objects if they exist and don't include if it's not at least 40,000 pixels since that is likely too small
#shirts
if len(shirtWeights) > 0 and shirtMinRectSize > 40000:
    #cv2.rectangle(image, (shirtMaxCon[0], shirtMaxCon[1]), (shirtMaxCon[0] + shirtMaxCon[2], shirtMaxCon[1] + shirtMaxCon[3]), (0,255,0), 3)
    cv2.rectangle(image, (shirtMinCon[0], shirtMinCon[1]), (shirtMinCon[0] + shirtMinCon[2], shirtMinCon[1] + shirtMinCon[3]), (0,255,0), 3)
    cv2.imshow('examples/jacket_1.jpg', image)
    cv2.waitKey(0)
else:
    print("no shirt found")
#pants
if len(pantsWeights) > 0 and pantsMinRectSize > 40000:
    #cv2.rectangle(image, (pantsMaxCon[0], pantsMaxCon[1]), (pantsMaxCon[0] + pantsMaxCon[2], pantsMaxCon[1] + pantsMaxCon[3]), (0,255,0), 3)
    cv2.rectangle(image, (pantsMinCon[0], pantsMinCon[1]), (pantsMinCon[0] + pantsMinCon[2], pantsMinCon[1] + pantsMinCon[3]), (0,255,0), 3)
    cv2.imshow('examples/jacket_1.jpg', image)
    cv2.waitKey(0)
else:
    print("no pants found")

#quantize
if len(shirtWeights) > 0:
    find_color(shirtMinCon)

if (len(pantsWeights) > 0):
    find_color(pantsMinCon)
