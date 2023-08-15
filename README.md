# OBJECT DETECTION BEGINNER TUTORIAL MODULE

<div>
    <h3> Module Description </h3>
        <p>This module is for the beginner who is trying the object detection model for the first time to grasp the sense of object detection.
        In this Module, we will work with Hand sign Images with 6 poses for detection.</p>
         <h4> What we Going to cover in this module </h4>
                <ul>
                      <li>How to create the training dataset and do annotation of an object (label creation)</li>
                      <li>How set custom dataset to work with YOLOv5    [<a href> https://github.com/ultralytics/yolov5.git</a> ]</li>
                      <li>Training the Dataset </li>
                      <li>Testing the dataset in real-time </li>
                </ul>
</div>


# Setting Annotations


<div>
    <ul>
        <li>Step :1 </li>
        Download the hand sign dataset from Kaggle [<a href> https://www.kaggle.com/datasets/gti-upm/leapgestrecog </a>] or can also create your own dataset using your hand gesture images
        <li>step:2</li>
        use the annotation tool to label the object [tool is attached in this git repo download it]
    </ul>
</div>

![annotation steps](https://github.com/MANOJ-S-NEGI/Object_detection_with_YOLOV5/assets/99602627/b01e4496-64bb-469e-b818-e09dafc29567)



<div>
    <ul>
        <li>Step :3 </li>
        separate the generated .txt file into a single folder name label 
        <li>step:4</li>
        Do the same with other every image 
    </ul>
</div>

```
Note: * Label name generated automatically is the same as the image name
      * 30 images are sufficient for each gesture 
```

# Training the Dataset:

* clone YOLOv5 repository
  ```
  git clone https://github.com/ultralytics/yolov5.git
  ```
* install dependencies inside YOLO5s
    ```
    !pip install -r requirements.txt
    
    import torch
    print('Setup complete: Using torch  veersion: (torch.__version__)
    ```
* create data.yaml file
    ```
    train: path/train/images
    val: path/test/images
    
    nc: 6    # number of classes
    names: ['Hello', 'IloveYou', 'No', 'Please', 'Thanks', 'Yes']
    ```
  
* This is the model configuration we will use
    ```
      %cat /content/yolov5/models/yolov5s.yaml
    ```
    OUTPUT:
  
    ![output](https://github.com/MANOJ-S-NEGI/Object_detection_with_YOLOV5/assets/99602627/86014df8-b643-4405-a65b-30507aa719ae)




* Customize iPython writefile
  ```
    from IPython.core.magic import register_line_cell_magic
    @register_line_cell_magic
      
    def writetemplate(line, cell):
       with open(line, 'w') as f:
       f.write(cell.format(**globals()))
  ```
    ```
    %%writetemplate /content/yolov5/models/custom_yolov5s.yaml


     parameters
    nc: 6  # number of classes
    depth_multiple: 0.33  # model depth multiple
    width_multiple: 0.50  # layer channel multiple
    
    # anchors
    anchors:
      - [10,13, 16,30, 33,23]  # P3/8
      - [30,61, 62,45, 59,119]  # P4/16
      - [116,90, 156,198, 373,326]  # P5/32
    
    # YOLOv5 backbone
    backbone:
      # [from, number, module, args]
      [[-1, 1, Focus, [64, 3]],  # 0-P1/2
       [-1, 1, Conv, [128, 3, 2]],  # 1-P2/4
       [-1, 3, BottleneckCSP, [128]],
       [-1, 1, Conv, [256, 3, 2]],  # 3-P3/8
       [-1, 9, BottleneckCSP, [256]],
       [-1, 1, Conv, [512, 3, 2]],  # 5-P4/16
       [-1, 9, BottleneckCSP, [512]],
       [-1, 1, Conv, [1024, 3, 2]],  # 7-P5/32
       [-1, 1, SPP, [1024, [5, 9, 13]]],
       [-1, 3, BottleneckCSP, [1024, False]],  # 9
      ]
    
    # YOLOv5 head
    head:
      [[-1, 1, Conv, [512, 1, 1]],
       [-1, 1, nn.Upsample, [None, 2, 'nearest']],
       [[-1, 6], 1, Concat, [1]],  # cat backbone P4
       [-1, 3, BottleneckCSP, [512, False]],  # 13
    
       [-1, 1, Conv, [256, 1, 1]],
       [-1, 1, nn.Upsample, [None, 2, 'nearest']],
       [[-1, 4], 1, Concat, [1]],  # cat backbone P3
       [-1, 3, BottleneckCSP, [256, False]],  # 17 (P3/8-small)
    
       [-1, 1, Conv, [256, 3, 2]],
       [[-1, 14], 1, Concat, [1]],  # cat head P4
       [-1, 3, BottleneckCSP, [512, False]],  # 20 (P4/16-medium)
    
       [-1, 1, Conv, [512, 3, 2]],
       [[-1, 10], 1, Concat, [1]],  # cat head P5
       [-1, 3, BottleneckCSP, [1024, False]],  # 23 (P5/32-large)
    
       [[17, 20, 23], 1, Detect, [nc, anchors]],  # Detect(P3, P4, P5)
      ]
    ```
    * NOTE: [only need to change the parameter nc = 6]
 
# Train Custom YOLOv5 Detector
number of arguments:

* img: define the input image size
* batch: determine batch size
* epochs: define the number of training epochs. (Note: often, 3000+ are common here!)
* data: set the path to our yaml file
* cfg: specify our model configuration 8 weights: specify a custom path to weights. (Note: you can download weights from the Ultralytics Google Drive folder)
* name: result names
* nosave: only save the final checkpoint
* cache: cache images for faster training

      ```
      %%time
      %cd /content/yolov5/
      !python train.py --img 416 --batch 16 --epochs 300 --data '/content/drive/MyDrive/cnn_data/data/data.yaml' --cfg ./models/custom_yolov5s.yaml --weights 'yolov5s.pt' --name yolov5s_results  --cache
      ```
# Evaluate Custom YOLOv5 Detector Performance
    ```
    from utils. plots import plot_results 
    Image(filename='/yolov5s_results/results.png', width=1000)  # view results.png
    ```
* Note from Glenn: Partially completed results.txt files can be plotted from utils.utils import plot_results; plot_results().
    
![results](https://github.com/MANOJ-S-NEGI/Object_detection_with_YOLOV5/assets/99602627/c3dbf6d6-bb46-4227-9bfa-e471a30c6429)

# Check the predictions
 create run.py and paste the below code
```
import os

os.system("python detect.py --weights best.pt --img 416 --conf 0.5 --source 0")

Note:[source 0 is the webcam while weight best.pt is in the same folder with the result]
```

### copy the best.pt and run.py and paste them into the YOLOV5 folder and then execute run.py


________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
# PYTHON MODULE GUIDE:

  ```
  pip install requirement.txt
  ```
```
run main.py
```
all setup will be done eventually error will encounter as path need to setup

* open signLanguage folder > components > Data_Training.py
```
yolov5_command = [
    "python", "PATH/yolov5/train.py",
    "--data", "PATH/data.yaml",
    "--cfg", "PATH/yolov5/models/custom_yolov5s.yaml",
]
```

* Open
```
signLanguage folder > constant > init.py and modify the TRAINING_DATA_PATH and VALIDATION_DATA_PATH
```
* run main.py Training will start


### Check the predictions
* copy the best.pt and run.py and paste them into the YOLOV5 folder and then execute run.py


