---
laout: default
title: status
---

## Project Summary

## Approach
We are using the Haar feature-based cascade classifier (Known for learning to detect faces) to detect objects in images. HaarCascade extracts important features from an image and tests if those features are present in an image. To classify an object in an image, it extracts a smaller part of the whole image and tests if the features are there. The important features are determined during the adaboost training part where features are individually tested and produce an error rate. To train our shirt classifier, we grabbed 200 shirt images from the public fashion-mnist dataset and an equal amount of negative images from a public tutorial online. Then we had to create an annotations txt file for our images so the trainer could identify the object in each positive image. Our classifier was trained on 19 stages when learning which features were the most important.

However, haarcascade is only good for detecting shapes but our project requires color. For now, our plan is to detect the object in the image and extract the color from pixels in the image to choose the one that appears the most.

## Evaluation
Our classifier can currently detect shirts in an image to an extent. However, it is not complex enough to detect them at strange angles because of our limited datset.

## Remaining Goals and Challenges
We plan on increasing our detection to include shoes and pants at the minimum. We will also need to implement the portion in our project where we use the information gained from object detection and apply it to a minecraft skin.

## Resources Used
Opencv docs gave much information about computer vision. This one in particular is a tutorial for cascade training https://docs.opencv.org/3.4/dc/d88/tutorial_traincascade.html.
We got our negative images from here https://github.com/handaga/tutorial-haartraining/tree/master/data/negatives and our positive images are part of the keras library so we extracted the images from there. Important libraries we use include keras, tensorflow, and cv2 (opencv).
