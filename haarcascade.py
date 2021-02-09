import numpy as np
import cv2

#cascade = cv2.CascadeClassifier('haarcascade1/cascade.xml')
cascade = cv2.CascadeClassifier('haarcascade2/cascade.xml')
#image = cv2.imread('pos/0.jpg')
#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#image = cv2.imread('examples/blueShirt.jpeg')
#image = cv2.imread('examples/blankblueshirt.jpg')
image = cv2.imread('examples/blueShirt.jpeg')
rectangle = cascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=0, flags=0)
print(rectangle)
#since the classifier finds many incorrect small rectangles at the moment, I search for the largest one as it is most likely correct in the photos we use
if len(rectangle) > 0:
    largest = 0
    large_rectangle = (0,0,0,0)
    for local in rectangle:
        local_large = abs(local[0] - local[2])
        local_large += abs(local[1] - local[3])
        if local_large > largest:
            largest = local_large
            large_rectangle = local
    cv2.rectangle(image, (large_rectangle[0], large_rectangle[1]), (large_rectangle[2], large_rectangle[3]), (0,255,0), 3)
    #for shapes in rectangle:
        #print(rectangle[0])
        #cv2.rectangle(image, (shapes[0], shapes[1]), (shapes[2], shapes[3]), (0,255,0), 3)
        #cv2.rectangle(image, (rectangle[0][0], rectangle[0][1]), (rectangle[0][2], rectangle[0][3]), (0, 255, 0), 3)
    cv2.imshow('examples/blankblueshirt.jpg', image)
    cv2.waitKey(0)