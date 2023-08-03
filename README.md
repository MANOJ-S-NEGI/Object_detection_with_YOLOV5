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

  
