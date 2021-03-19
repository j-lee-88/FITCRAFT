from PIL import Image
import cv2
import numpy as np

#create blank 64x64 png to paint on
#image = Image.new('RGB', (64, 64))
path = "default.png"
original = Image.open("default.png")
#edited = original.copy()

def draw_shirt(path, workingSkin, boxes, color):
    if (workingSkin == ""):
        image = cv2.imread(path)
    else:
        image = cv2.imread(workingSkin)
    img = image.copy()
    #cv2.imshow("test", image)
    #cv2.waitKey(0)
    for name, value in boxes.items():
        cv2.rectangle(img, (value[0], value[1]), (value[2], value[3]), color, -1)
    temp = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    _,alpha = cv2.threshold(temp,0,255,cv2.THRESH_BINARY)
    b, g, r = cv2.split(img)
    rgba = [b,g,r, alpha]
    img = cv2.merge(rgba,4)
    #cv2.imwrite("test.png", dst)
    cv2.imwrite("skin.png", img)
    return "skin.png"

head = {
    'top' : [8,0,16,8],
    'bottom' : [16,0,24,8],
    'right' : [0,8,8,16],
    'front' : [8,8,16,16],
    'left' : [16,8,24,16],
    'back' : [24,8,32,16]
}

right_leg = {
    'top' : [4,16,7,20],
    'right' : [0,20,3,29],
    'front' : [4,20,7,29],
    'left' : [8,20,11,29],
    'back' : [12,20,15,29]
}

right_shoe = {
    'bottom' : [8,16,12,20],
    'right' : [0,30,4,31],
    'front' : [4,30,8,31],
    'left' : [8,30,12,31],
    'back' : [12,30,16,31]
}

torso = {
    'top' : [20,16,28,20],
    'bottom' : [28,16,36,20],
    'right' : [16,20,20,32],
    'front' : [20,20,28,32],
    'left' : [28,20,32,32],
    'back' : [32,20,40,32]
}

right_arm = {
    'top' : [44,16,48,20],
    'bottom' : [48,16,52,20],
    'right' : [40,20,44,32],
    'front' : [44,20,48,32],
    'left' : [48,20,52,32],
    'back' : [52,20,56,32]
}


left_leg = {
    'top' : [20,48,23,52],
    'right' : [16,52,19,61],
    'front' : [20,52,23,61],
    'left' : [24,52,27,61],
    'back' : [28,52,31,61]
}

left_shoe = {
    'bottom' : [24,48,28,52],
    'right' : [16,62,20,64],
    'front' : [20,62,24,64],
    'left' : [24,62,28,64],
    'back' : [28,62,32,64]
}

left_arm = {
    'top' : [36,48,40,52],
    'bottom' : [40,48,44,52],
    'right' : [32,52,36,64],
    'front' : [36,52,40,64],
    'left' : [40,52,44,64],
    'back' : [44,52,48,64]
}

right_leg_2 = {
    'top' : [4,48,8,36],
    'bottom' : [8,48,12,36],
    'right' : [0,36,4,48],
    'front' : [4,36,12,48],
    'left' : [8,36,16,48],
    'back' : [12,36,16,48]
}

torso_2 = {
    'top' : [20,47,28,36],
    'bottom' : [28,47,36,36],
    'right' : [16,36,20,48],
    #'front' : [20,36,28,48],
    #'left' : [28,36,32,48],
    'back' : [32,36,39,48]
}

right_arm_2 = {
    'top' : [44,32,47,36],
    #'bottom' : [48,48,52,36],
    'right' : [40,36,43,40],
    'front' : [44,36,47,40],
    'left' : [48,36,52,40],
    'back' : [52,36,55,40]
}

left_leg_2 = {
    'top' : [4,48,8,52],
    'bottom' : [8,48,12,52],
    'right' : [0,52,4,64],
    'front': [4,52,8,64],
    'left' : [8,52,12,64],
    'back' : [12,52,16,64]
}

left_arm_2 = {
    'top' : [52,48,55,52],
    #'bottom' : [56,48,60,52],
    'right' : [48,52,52,56],
    'front' : [52,52,56,56],
    'left' : [56,52,60,56],
    'back' : [60,52,64,56]
}

#draw_shirt(path, torso, (0,255,0))
#draw_shirt(path, torso_2, (178,181,186))
