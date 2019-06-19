
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
  
      3.1 This process is making *Training images* and *Annotation data set* with VOC format.
      
      Place your background images under the following directory, the name of image file should include the squence number from "000001".
  
      `(you workdirectory)/ssd_pytorch/VOCdevkit/VOC2019/xx_data_creator/00_background`

      3.2 Place your icon images under the following directory, the name of image file direcly is used as label names (classificaton label) and you should not use *capital letters* for label names.
      For example, "icona.PNG" --> the label name is "icona".

      `(you workdirectory)/ssd_pytorch/VOCdevkit/VOC2019/xx_data_creator/01_icon`
      
      3.3 Create the following items
      
        * Training images (located in (**)/VOCdevkit/VOC2019/JPEGImages), 
        * Annotation xmls (located in (**)//VOCdevkit/VOC2019/Annotations),
        * trainval.txt  (training index list, located in (**)/VOCdevkit/VOC2019/ImageSets/Main),
        * test.txt  (test index list, located in (**)/VOCdevkit/VOC2019/ImageSets/Main)
      
      data_creation.py will place the icons randomly on the background images so that training images are acquired. At the same time it makes the annotation xmls, trainval.txt  and test.txt as well. 
      
      `$cd (you workdirectory)/ssd_pytorch/VOCdevkit/VOC2019/xx_data_creator` 
      
      `$python3 data_creation.py`
      
      
  4. Traning precedure    
      
      Move to root directory (you workdirectory)/ssd_pytorch), and start jupyter notebook.

      `$jupyter notebook`

      Then, click *training.ipynb*
      
      Please RUN each cell for the following section, (there are same *Headlines*)
        * Step.1) IMPORT PYTORCH
        * Step.2) Setting up for Training SSD network
        * Step.3) Training SSD network
      
    After training, you will recieved the network weights file (VOC.pth, located in (WD)/ssd_pytorch/weights)

  
  5. Operation precedure
      
      Use jupyter notebook, and then click *detection.ipynb* located in (WD)/ssd_pytorch/demo, 
      
      Please RUN each cell for the following section, (there are same *Headlines*)
        * Step.1) IMPORT PYTORCH
        * Step.2) Loading SSD network wight
        * Step.3) Set image file to test
        * Step.4) Processing SSD for icon detetion

      