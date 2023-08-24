# Liveness Detection

* This code trains and implements liveness detection with video input

* Modified original model to Resnet50 to achieve better accuracy (Thanks Jason Chu)

<p align="center">
  <img src="dataset\ezgif-1-085534fa4973.gif?raw=true" width="600">
</p>
<br>
<br>

## Setup Environment:
```
conda create -n liveness python=3.8
conda activate liveness
pip install -r requirements.txt
```

## Train & Deploy steps:
All Tested on Windows 10 conda environment
Please install miniconda or Anaconda first
### Cmd Line

```
# data pre-process
python gather_examples.py -i ./videos/fake.mp4 -o ./dataset/fake -d ./face_detector -c 0.9 -s 1 -f 0
python gather_examples.py -i ./videos/real.mp4 -o ./dataset/real -d ./face_detector -c 0.9 -s 1 -f 0
python gather_examples.py -i ./videos/mask.mp4 -o ./dataset/mask -d ./face_detector -c 0.9 -s 1 -f 0

# train model
python train_liveness.py -d ./dataset -m liveness.model -l le.pickle

# run liveness model on test video
python liveness_demo.py -m liveness.model -l le.pickle -d ./face_detector -c 0.5
press "q" to quit

# run liveness model on web cam
python webcam.py

```

### Auto run bat files
run 01_XXX.bat files (01~05) sequentially:
```
01_install.bat
02_gather.bat
03_trainLiveness.bat
04_runLiveness.bat
05_webcam.bat
```


## Refernce
 The following link is the original pyimagesearch liveness-detection-with-opencv example code:
https://www.pyimagesearch.com/2019/03/11/liveness-detection-with-opencv

### Find this project useful ? :heart:
* Support it by clicking the :star: button on the upper right of this page. :v:

### Credits
* The example has been taken from pyimagesearch liveness-detection-with-opencv example and modified model to Resnet50

### License
Copyright (C) 2020 Adrian Rosebrock, PyImageSearch, https://www.pyimagesearch.com/2019/03/11/liveness-detection-with-opencv/, accessed on March 11, 2019

### Contributing to livenessDetection
Just make pull request. Thank you!
