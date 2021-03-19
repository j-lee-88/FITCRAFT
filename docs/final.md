---
layout: default
title: Final Report
---

## Video
Embed video here

# Project Summary
The project we have chosen to approach is parsing images of outfits into corresponding Minecraft skins using computer vision techniques and algorithms. Our overall plan has not changed significantly in its theme since the start of the project, but we notably lost a team member, and so are working as a two-person group now. With that in mind, we have adjusted the scope and complexity of our final version to be more in line with our reduced group size. We are currently planning to support outfits including up to a shirt, jacket, hat, pants/shorts, and shoes using a standardized Minecraft skin template that we will overlay each clothing piece on. We think this approach will help people quickly create skins from existing photographs instead of spending time to manually create skins on a website.

# Approaches
Use another level-two header calledApproaches, In this section, describe both the baselinesand your proposed approach(es). Describe precisely what the advantages and disadvantages of each are,for example, why one might be more accurate, need less data, take more time, overfit, and so on. Includeenough technical information to be able to (mostly) reproduce your project, in particular, use pseudocodeand equations as much as possible.

We are using the Haar feature-based cascade classifier (known for learning to detect faces) to detect objects in images. Haar-cascade extracts important features from an image and tests if those features are present in an image. To classify an object in an image, it extracts a smaller part of the whole image and tests if the features are there. The important features are determined during the adaboost training part where features are individually tested and produce an error rate. Important features are placed into multiple stages. These stages are for quickly testing if a spot in an image is our desired object. For example, the classifier zooms in on one part of an image and detects if it has enough features from stage one of the classifier. If it does not, then we stop testing that spot in the image and move on immediately instead of testing that spot for all desired features. For our cascade classifiers, we set it to 10 stages with a "max false alarm rate" of 0.3. This means that while training each stage on positive images, we continue extracting features until that stage can classify incorrectly less than 30% of the time. We used 500 images from the Fashion MNIST dataset for each of our clothing objects and an equal amount of negative images to train our classifier. The shoes had 1500 images since MNIST had 1000 images each for sneakers, boots, and sandals.

However, Haar-cascade is only good for detecting shapes but our project requires color. For now, our plan is to detect the object in the image and extract the color from pixels in the image to choose the one that appears the most. We will then repeat this process with a classifier for each type of clothing, eventually including shirts, jackets, pants, shorts, shoes, and possibly hats. We use OpenCV's functions to detect objects in an image by making rectangles. We use the classifiers to detect the object and get confident weights for each possible detection. We use the most confident detection and extract its color by averaging the color within the rectangle. Then we use the color and map it to the appropriate clothing piece by coloring the default skin at the correct coordinates.

One of the major difficulties we ran into was finding a good clothing dataset with proper annotations, which are images that outline coordinates to an object in an image. We need proper annotations so that our classifier can learn to detect the outlined object from thousands of images. In the end, we had to stick with the Fashion MNIST dataset since all the images were simple clothing objects with no background, and therefore no need for annotations since the whole image is the object. However, this limited dataset has weakened our classifier since the images are simple and not diverse in angles.

We initially looked into masked rcnn but ran into a lot of difficulty in finding a dataset that can provide all the information that masked rcnn requires. This includes bounding boxes for the object in an image, prediction confidence or weights from a previously defined model, and an object mask (polygon outline for object). Masked RCNN is known to be more accurate than Haar Cascade since it makes use of convultional neural networks, which is the modern approach to machine learning. Haar Cascade is simply for feature extraction and detection on objects whereas Masked RCNN is more detailed image segmentation where we get an outline instead of a rectangle around an object.

# Evaluation
An important aspect of your project, as I’ve mentioned several times now, is evaluating yourproject. Be clear and precise about describing the evaluation setup, for both quantitative and qualitativeresults. Present the results to convince the reader that you havesolvedthe problem, to whatever extent youclaim you have. Use plots, charts, tables, screenshots, figures, etc. as needed. I expect you will need at leasta few paragraphs to describe each type of evaluation that you perform.

# References
Make a list of work you’re citing in your description above (starting with a level-two header).This should include any papers you think are relevant, third-party source code you used, sources for any ofthe images that you didn’t create, and any other websites/links you found useful.

https://minecraft.novaskin.me/ for minecraft skin uploading

https://stackoverflow.com/questions/40527769/removing-black-background-and-make-transparent-from-grabcut-output-in-python-ope for making an image with no background.

https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_objdetect/py_face_detection/py_face_detection.html opencv information about Haar Cascades.

https://docs.opencv.org/2.4/doc/user_guide/ug_traincascade.html the documentation behind Opencv's Haar Cascade functions.

https://pythonprogramming.net/haar-cascade-object-detection-python-opencv-tutorial/ A tutorial on Haar Cascade.

https://www.kaggle.com/zalando-research/fashionmnist Information on the Fashion MNIST dataset.

https://opencv-python-tutroals.readthedocs.io/en/latest/index.html Opencv documentation behind a lot of its functionality.

https://github.com/JoakimSoderberg/haarcascade-negatives Negative image dataset.

https://machinelearningmastery.com/how-to-perform-object-detection-in-photographs-with-mask-r-cnn-in-keras/ Attempted Masked RCNN tutorial but could not get it to work.

https://github.com/minotar/skin-spec Minecraft skin coordinates
