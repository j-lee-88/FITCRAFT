---
layout: default
title:  Proposal
---
## Summary
The project our team has chosen to undertake is converting images of humans in outfits into Minecraft skins, based on a multi-class classification algorithm trained with machine learning techniques. The input will be in the form of an array of pixels with color value, which then is parsed by the algorithm to produce a corresponding Minecraft skin that most closely matches the input. Applications of this project could include easy generation of content for the game, as well as being an example of computer vision.  


## AI/ML Algorithms
Some of the AI/ML algorithms that we anticipate using for this project are deep learning for images, and other libraries and functions in the computer vision and multi-class classification fields.


## Evaluation Plan
The quantitative metrics we will use to evaluate our model's performance are AUC score measured against a validation set that we will seed manually by choosing the optimal Minecraft skin for a number of test data.  Our baseline will be established with early testing of simple models, and may vary depending on our chosen set of outputs.  In addition, our testing and training examples will have to be cleaned.

For qualitative analysis, visualization of the internal workings of our model will be based primarily upon deep-dives into the documentation of the libraries we employ.  We will reserve a certain number of images most clearly linked to a certain Minecraft skin as our sanity cases.  Our moonshot or stretch goal would be to be able to pass complex outfits into the model and receive accurate Minecraft skins, such as those involving complex textures or color variations.  


Appointment time: 1/27/20, 3:45 PM
