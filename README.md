### 1. Introduction

The traffic signs recognition is able to detect and classify different traffic signs using OpenCV. The source code that was used for this program can be found here: https://github.com/hoanglehaithanh/Traffic-Sign-Detection. Compared to the program created by Thanh Hoang Le Hai, the number of traffic signs was increased from 8 to 28, and right now it is possible to detect input not only from a video file but also from the camera and directly from the screen. 

The detection phase uses Image Processing techniques that create contours on each video frame and find all ellipses or circles among those contours. They are marked as candidates for traffic signs. A white square will highlight the object detected.

Detection strategy:
1. Increase the contrast and dynamic range of the video frame
2. Remove unnecessary colors like green with HSV Color range
3. Use Laplacian of Gaussian to display border of objects
4. Make contours by Binarization.
5. Detect ellipse-like and circle-like contours

In the next phase - classification phase, a list of images are created by cropping from the original frame-based on candidates' coordinate. A pre-trained SVM model will classify these images to find out which type of traffic sign they are. A green square will highlight the object detected as a traffic sign.

The traffic signs that are currently supported can be seen in the pictures below (the name of each traffic sign corresponds to their class in SVM* and to their specific folder in the dataset folder):

[![all-signs-detected.png](https://i.postimg.cc/HsTgQbj0/all-signs-detected.png)](https://postimg.cc/pyc4vhfy)
[![all-signs-detected2.png](https://i.postimg.cc/L8ZN5bRx/all-signs-detected2.png)](https://postimg.cc/YvM1y8vF)

The 0 class is for images that are detected but marked as non-traffic signs. Currently, only the **biggest** sign in the current frame is cropped and classified. Due to the initial implementation, the SVM Model is trained each time the ```main.py``` called, before the detection phase. However, the model is saved into a file ```data_svm.dat```, so a future reload function implementation to avoid the retraining phase would be possible. 

If a traffic sign is detected, it will be tracked until it disappears or there is another bigger sign in the frame. The tracking method is [Dense Optical Flow](https://docs.opencv.org/trunk/d7/d8b/tutorial_py_lucas_kanade.html).

### 2. Dependencies:

The program is dependent on other libraries. It works only with Python3 and OpenCV3. Additionally, some other dependencies such as Imutils are used for image processing while the mss and PIL libraries are used for the Screen Recording program. 

- Python 3.5
- [OpenCV3](https://opencv.org/) (use ```pip3 install opencv-python==3.4.0.14```)
- Imutils (use```pip3 install imutils``` to install)
- mss (use```pip3 install -U --user mss``` to install)
- PIL (use ```sudo apt install python3-pil```)
- SCIKIT-Image (use ```sudo apt-get install python3-skimage```)
-	MatplotLib (use ```pip3 install -U matplotlib```)

### 3. System file structure
##### a. There are 3 python files as 3 modules:
- [main.py](main.py) : Is the start point of the program.
- [classification.py](classification.py) : Is the SVM Model to classify traffic signs
- [common.py](common.py) : Is a script containing functions for defining SVM Model


Other files:
- [data_svm.dat](data_svm.dat) : Saved SVM model after training.
- [MVI_1049.avi](MVI_1049.avi) : Currently and original video used by the creator of this program
- [MVI_1049(first).avi](MVI_1049(first).avi) : Video containing many traffic signs (speed increased)
- [Youtube:Traffic signs - English vocabulary](https://www.youtube.com/watch?v=s36wuoemF7U) : Original video speed compared to ```MVI_1049(first).avi```
- [Youtube:Driving in the Netherlands](https://www.youtube.com/watch?v=1mgGIiQeffw) : Other video to be used for the detection
- [output.avi](output.avi) : Output video generated from the detection using ```MVI_1049.avi```
- [output2.avi](output2.avi) : Output video from video ```MVI_1049(first).avi``` used to generated the result .gif

##### b. [Dataset](dataset)
The [Dataset](dataset) folder contains images for training SVM models. There are 28 folders contains cropped images of traffic signs. Each folder is named like the class of the traffic signs it contains. The special dataset 0 folder contains non-traffic-sign cropped images which can be recognized as traffic signs in the detection phase. 

[![0.png](https://i.postimg.cc/zvrkcnQ8/0.png)](https://postimg.cc/r0fWdtcP)

The new dataset was created by applying the detection phase on many videos with various parameters to mark all traffic signs and then manually separating them into their right classes.

Each time the program is run, the dataset can be updated by checking all generated cropped images of detected traffic signs, then find all misclassified traffic signs.

Additionally in this folder, another folder called ```Complete Belgian Dataset``` exist which contains the majority of traffic signs that can be found in Belgium. If somebody wants to add different traffic signs than the one already implemented make sure to check this folder. 

If a new sign will be added then create a new folder in the ```Dataset``` folder, keeping the same numbering order in the name of the folders. Add your new files into that folder. Then change the following things: 

1. In the script ```main.py``` after line 43 add your traffic sign detection text like this ``` "New Sign", ```. Keep ``` "OTHER" ``` as your last detection text, do not remove it to add your new traffic sign, add it before.

2. In the script ```classification.py``` change the ```CLASS_NUMBER``` (line 10) to your ```last folder value + 1``` (or the total number of folders you have).  

In order to convert images from .ppm to .png (as the program only allows .png and the dataset has .ppm files) use the following command in the terminal:

```
mogrify -format png *.* 
```

##### c. [CompressedImage2Other](CompressedImage2Other)
This folder contains three Python scripts. The script called [CompressedImage2Other](CompressedImage2Other) takes care of converting the ROS Compressed Images to OpenCV Images using CVBridge. It currently supports only one topic thus only one camera stream but work is done in expanding it to multiple camera streams. It works with Python3. The code zqs inspired from the following: http://wiki.ros.org/rospy_tutorials/Tutorials/WritingImagePublisherSubscriber. The other python scripts take care of the conversion to video. Due to some errors with the libraries, these programs do not currently work (they were taken from this library: https://github.com/mli0603/CompressedImage2Video). Due to different priorities, this was not achieved at the moment.  

##### d. [ScreenRecord](ScreenRecord)
This folder contains the script that was used in the traffic sign recognition program to capture the screen. It is fully working on its own using Python3.

### 4. Input supported
#### Several inputs are supported by this program
- a video in format .avi : ```vidcap = cv2.VideoCapture(args.file_name)```
- camera stream : ```vidcap = cv2.VideoCapture(0)```
- Screen recording : ```screenshot = mss().grab(mon)```

Please read the comments in the document ```main.py``` in order to make the switch between the different inputs (line 261 to 262 and line 291 to 311). 

### 5. Installation
#### There are two ways of running the program:
Use default arguments:
```sh
$python3 main.py
```
Use custom arguments: 
```sh
$python3 main.py
optional arguments:
  -h, --help            show this help message and exit
  --file_name FILE_NAME
                        Video to be analyzed
  --min_size_components MIN_SIZE_COMPONENTS
                        Min size component to be reserved
  --similitary_contour_with_circle SIMILITARY_CONTOUR_WITH_CIRCLE
                        Similarly to a circle
```
### 6. Result

Click on the picture:

![](images/demo2.gif)

### 7. Disadvantages
- The image processing is static, meaning that parameters must be updated for each video with different lighting conditions.
- The accuracy of the detection phase is okay, sometimes it misses traffic signs or detects other objects like traffic signs(this happens almost never). 
- The screen Recorder frames are around 15 fps. 

### 8. License and Versions

[MIT License](LICENSE)
© 2018 Hoàng Lê Hải Thanh (Thanh Hoang Le Hai) aka GhostBB (original version)

The Current Version was modified from the original by Mihai-Dragoș Ungureanu. 
