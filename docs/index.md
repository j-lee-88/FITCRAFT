---
layout: default
title:  Home
---

Source code: https://github.com/j-lee-88/FITCRAFT

Reports:

- [Proposal](proposal.html)
- [Status](status.html)
- [Final](final.html)

[Team](team.html)

## Summary
The project our team has chosen to undertake is converting images of humans in outfits into Minecraft skins, based on a haarcascading classifier algorithm. The input will be in the form of an array of pixels with color value, which then is parsed by the algorithm to produce a corresponding Minecraft skin that most closely matches the input. To be specific, we will take an image, identify the clothing objects in that image, and translate those objects to a minecraft skin. Applications of this project could include easy generation of content for the game, as well as being an example of computer vision. We are currently using the fashion mnist dataset since there are 1000 images of each clothing item. We will have a set of pre-made skins that we will generate in the Minecraft skin creator Minecraftskins, and then categorize each input as one of those pre-made skins, seeking to accurately match the color of the torso, arms, legs, and head. For example, this picture should translate to something like the skin:

![image](images/goal1.jpg)
![image](images/goal2.png)

Here are examples of what the minecraft skin layout to real skin look like:

![image](images/bluelayout.png)
![image](images/bluelayoutshirt.png)
![image](images/greenlayout.png)
![image](images/greenlayoutshirt.png)
![image](images/redlayout.png)
![image](images/redlayoutshirt.png)

## Team Members
Justin Lee
Cedric Ngo

## Relevant Material
[OpenCV Haar-Cascade documentation](https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html)
