
# ssd_pytorch
====

## Overview

Icon detection software in car multimedia systems using ssd and pytorch


## Description
ssd_pytorch consist of 3 parts

1) Data creation for own data-set aligned with VOC format
2) Training process (training.ipynb)
3) Operation process (./demo/detection.ipynb)


## Requirement

OS: Ubuntu 16.04 LTS

* Python related

  Python 3.5.2
  opencv-python 4.0.0
  numpy 1.16.2
  matplotlib 3.0.3
  Pillow 6.0.0
 

* Deep learning related (How to install)

  jupyter notebook 4.4.0
  `$pip3 install jupyter`

  pytorch (please follow the same version)
  `$pip3 install torch==0.4.1`
  `$pip3 install torchvision==0.2.1`


## Usage

   1. Clone the code
      
      This repository include *pascal-voc-writer*, 
      https://github.com/AndrewCarterUK/pascal-voc-writer

      `$git clone https://github.com/kobokobo/ssd_pytorch.git`

      `$git submodule update --init --recursive`

      `$git checkout feature/car_navigation`


  2. Download base network VGG16 and place it to under *weights* directory
  
      `$wget https://s3.amazonaws.com/amdegroot-models/vgg16_reducedfc.pth`
      `$mv ./vgg16_reducedfc.pth  (you workdirectory)/ssd_pytorch/weights`


  3. Data prepartion for VOC format
      this process 

      place your background under 
  
      `(you workdirectory)/ssd_pytorch/VOCdevkit/VOC2019/xx_data_creator/00_background`


