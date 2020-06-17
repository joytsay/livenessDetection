# Liveness Detection

* This code trains and implements liveness detection with video input

* Modified original model to Resnet50 to achieve better accuracy (Thanks Jason Chu!)

<p align="center">
  <img src="https://github.com/joytsay/livenessDetection/blob/master/dataset/ezgif-1-085534fa4973.gif?raw=true" width="600">
</p>
<br>
<br>

* Install steps:

Use Anaconda3

pip install imutils

pip install keras

pip install --upgrade h5py

pip install opencv-python

* Train & Deploy steps:

use ./gather.bat to get train image snapshots from video in ./videos folder. (images will be stored in ./dataset/fake & real)

run ./trainLiveness.bat to train images from ./dataset

run ./runLiveness.bat to see implementaion of Liveness Detection via video input (-c 0.5 is the threshold of "Fake" and "Liveness")

# The following link is the original pyimagesearch liveness-detection-with-opencv example code:
https://www.pyimagesearch.com/2019/03/11/liveness-detection-with-opencv

### Find this project useful ? :heart:
* Support it by clicking the :star: button on the upper right of this page. :v:

### Credits
* The example has been taken from pyimagesearch liveness-detection-with-opencv example and modified model to Resnet50

### License
Copyright (C) 2020 Adrian Rosebrock, PyImageSearch, https://www.pyimagesearch.com/2019/03/11/liveness-detection-with-opencv/, accessed on March 11, 2019

### Contributing to livenessDetection
Just make pull request. Thank you!
