# Liveness Detection

* This code trains and implements via video from the [pyimagesearch liveness detection blog](https://www.pyimagesearch.com/2019/03/11/liveness-detection-with-opencv)

* We modified the blog's original shallow CNN model to Resnet50 that can achieve better accuracy

<p align="center">
  <img src="https://github.com/joytsay/livenessDetection/blob/master/dataset/ezgif-1-085534fa4973.gif?raw=true" width="600">
</p>
<br>
<br>

## Get this code:
```
git clone https://github.com/joytsay/livenessDetection.git
cd livenessDetection
```

## Pre-Trained Model and Train/Test Videos:
Download from [here](https://drive.google.com/drive/folders/1Uj49JwLSAY4Q4v6UVMNF0u9hobGrJoWC?usp=sharing) and put in root folder (`/livenessDetection`)

## Setup Environment:
### Tested on Windows 10 [mini-conda](https://docs.conda.io/en/latest/miniconda.html) environment via

[Miniconda3-latest-Windows-x86_64.exe](https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe)

### Tested on MacOS M2 [mini-forge](https://github.com/conda-forge/miniforge) environment via
`brew install miniforge`

## Install Code:
### Option 1: Auto run bat files
run 01_XXX.bat files (01~05) sequentially:
```
01_install.bat
02_gather.bat
03_trainLiveness.bat
04_runLiveness.bat
05_webcam.bat
```
### Option 2: Cmd Line
```
conda create -n liveness python=3.8
conda activate liveness
pip install -r requirements.txt
```

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
python webcam.py -m liveness.model -l le.pickle -d ./face_detector -c 0.5

```



## Reference
 The following link is the original pyimagesearch [liveness-detection-with-opencv example code](https://www.pyimagesearch.com/2019/03/11/liveness-detection-with-opencv)

### Find this project useful ? :heart:
* Support it by clicking the :star: button on the upper right of this page. :v:

### Credits
* The example has been taken from pyimagesearch liveness-detection-with-opencv example and modified model to Resnet50

### License
Copyright (C) 2020 Adrian Rosebrock, [PyImageSearch](https://www.pyimagesearch.com/2019/03/11/liveness-detection-with-opencv/), accessed on March 11, 2019

### Contributing to livenessDetection
Just make pull request. Thank you!
