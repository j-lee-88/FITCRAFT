---
layout: default
title: status
---
## Video Link
https://youtu.be/KSB06SVjTK4

## Project Summary
The project we have chosen to approach is parsing images of outfits into corresponding Minecraft skins using computer vision techniques and algorithms.  Our overall plan has not changed significantly in its theme since the start of the project, but we notably lost a team member, and so are working as a two-person group now.  With that in mind, we have adjusted the scope and complexity of our final version to be more in line with our reduced group size.  We are currently planning to support outfits including up to a shirt, jacket, hat, pants/shorts, and shoes using a standardized Minecraft skin template that we will overlay each clothing piece on.

## Approach
We are using the Haar feature-based cascade classifier (known for learning to detect faces) to detect objects in images. Haar-cascade extracts important features from an image and tests if those features are present in an image. To classify an object in an image, it extracts a smaller part of the whole image and tests if the features are there. The important features are determined during the adaboost training part where features are individually tested and produce an error rate. To train our shirt classifier, we grabbed 200 shirt images from the public fashion-mnist dataset and an equal amount of negative images from a public tutorial online. Our classifier was trained on 15 stages when learning which features were the most important.

However, Haar-cascade is only good for detecting shapes but our project requires color. For now, our plan is to detect the object in the image and extract the color from pixels in the image to choose the one that appears the most.  We will then repeat this process with a classifier for each type of clothing, eventually including shirts, jackets, pants, shorts, shoes, and possibly hats.

## Evaluation
Our classifier can currently detect shirts in an image to an extent. However, it is not complex enough to detect them at strange angles.  The OpenCV implementation of Haar-cascade does not support quantitative evaluation metrics, but we can qualitatively assess the accuracy of our classifier after each training by manual checking.  Examples of our current classifier's accuracy are shown below:

![Example 1](https://github.com/j-lee-88/FITCRAFT/blob/main/docimg/classifyexample1.png)
![Example 2](https://github.com/j-lee-88/FITCRAFT/blob/main/docimg/classifyexample2.png)
>>>>>>> 13dd6d1ed85aad13f306c42448a07f9a8d7ca237

## Remaining Goals and Challenges
We plan on increasing our detection to include shoes and pants at the minimum. We will also need to implement the portion in our project where we use the information gained from object detection and apply it to a Minecraft skin.  In addition, we will explore different training parameters and methods to enhance the performance of our classifier so that it can detect pieces of clothing at non-head-on angles.  

## Resources Used
Opencv docs gave much information about computer vision. This one in particular is a tutorial for cascade training https://docs.opencv.org/3.4/dc/d88/tutorial_traincascade.html.
We got our negative images from here https://github.com/handaga/tutorial-haartraining/tree/master/data/negatives and our positive images are part of the keras library so we extracted the images from there. Important libraries we use include keras, tensorflow, python image library, and cv2 (opencv).
