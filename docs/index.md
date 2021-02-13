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
The project our team has chosen to undertake is converting images of humans in outfits into Minecraft skins, based on a multi-class classification algorithm trained with machine learning techniques. The input will be in the form of an array of pixels with color value, which then is parsed by the algorithm to produce a corresponding Minecraft skin that most closely matches the input. Applications of this project could include easy generation of content for the game, as well as being an example of computer vision. We are planning to use the DeepFashion dataset to provide labeled images of outfits with rich categorizations. We will have a set of pre-made skins that we will generate in the Minecraft skin creator Minecraftskins, and then categorize each input as one of those pre-made skins, seeking to accurately match the color of the torso, arms, legs, and head. For example, this picture should translate to something like the skin:
![Simple Goal Image](https://github.com/j-lee-88/FITCRAFT/blob/main/goal%20img1.jpg)
![Simple Goal Minecraft Skin](https://github.com/j-lee-88/FITCRAFT/blob/main/goal%20img2.png)

![Mockup of Final Minecraft Skin For RGB T-Shirts](https://imgur.com/a/kca4mBk)

## Team Members
Justin Lee
Cedric Ngo

## Relevant Material
- [OpenCV Haar-Cascade documentation](https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html)
