---
layout: default
title:  Proposal
---
## Summary
The project our team has chosen to undertake is converting images of humans in outfits into Minecraft skins, based on a multi-class classification algorithm trained with machine learning techniques. The input will be in the form of an array of pixels with color value, which then is parsed by the algorithm to produce a corresponding Minecraft skin that most closely matches the input. Applications of this project could include easy generation of content for the game, as well as being an example of computer vision.  We are planning to use the DeepFashion dataset to provide labeled images of outfits with rich categorizations.  We will have a set of pre-made skins that we will generate in the Minecraft skin creator Minecraftskins, and then categorize each input as one of those pre-made skins, seeking to accurately match the color of the torso, arms, legs, and head. For an example image: https://imgur.com/a/X9Tq330, the output might be the following: https://imgur.com/a/44mmluH.

## AI/ML Algorithms
Some of the AI/ML algorithms that we anticipate using for this project are deep learning for images, and other libraries and functions in the computer vision and multi-class classification fields.

## Evaluation Plan
The quantitative metrics we will use to evaluate our model's performance are AUC score measured against a validation set that we will seed manually by choosing the optimal Minecraft skin for a number of test data.  Our baseline will be established with early testing of simple models, and may vary depending on our chosen set of outputs.  In addition, our testing and training examples will have to be cleaned.

For qualitative analysis, visualization of the internal workings of our model will be based primarily upon deep-dives into the documentation of the libraries we employ.  We will reserve a certain number of images most clearly linked to a certain Minecraft skin as our sanity cases.  Our moonshot or stretch goal would be to be able to pass complex outfits into the model and receive accurate Minecraft skins, such as those involving complex textures or color variations.  

## Status Report Goals
By the date of the status report, our team is looking to have developed a model that can accurately match the color of an input's shirt to a corresponding Minecraft skin.  

## Weekly Meeting time
Our team will plan to meet on each Wednesday at 3:00 PM.

Appointment time: 1/27/20, 3:45 PM
