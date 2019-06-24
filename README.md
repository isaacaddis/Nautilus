# ROV2019

45C Robotics* robot code for the 2019 MATE Competition.

This code was developed by Isaac Addis and Alexander Vasquez.

# Features

In accordance to the team's motto, *Pushing Beyond the Limits*, this year's software for 45C was the most advanced and the most polished up to this time. The codebase features a PyQt GUI simulataneously acting as a multiplexer, serial reader, and vision processing (YOLO Object Objection for Convolutional Neural Networks and OpenCV) output with the *multithreading* module.

## Components

### Graphical User Interface (GUI)

 *Note: PyQt4*

Video signals are combined into the GUI program, transformed into *QImage* modules, then emitted back to the main UI object.

After tracing the codebase's mysterious *Segmentation Faults*, we learned that running individual threads for cv2.VideoCapture() objects was overloading our memory bus, reverting the GUI code to sequentially read and process video frames from each of the three cameras.

### Benthic Species (OpenCV -> YOLO -> cv2.dnn -> GUI)

We found that we had to be extremely selective with the pre-processing steps we applied on the image. Because shapes can be easily transformed from a non-edge preserving cv2.medianBlur() (or even cv2.GaussianBlur()), our processing steps mainly threshold the image (with cv2.THRESH_BINARY_INV -- it's easier to inverse and look for white then look for black in this particular scenario), masking the image, and using cv2.bilateralFilter() for its edge-preserving abilities.

We used [darknet](https://github.com/pjreddie/darknet) to build our YOLO (You Only Look Once) network on 428 manually-labeled images, achieving about 50% of loss after 45 of initial training, and transfer-learning (Freezing weights in layers up to the last layer) with data augmentation, rotating the image in various degrees to improve real-time accuracy.

### LiveMeasure (For crack detection in Task 1)

LiveMeasure was built by Alex V. and undistorts the images from our fisheye cameras to be used for measurement. This relies on calibrating your camera onto a flat checkerboard and referring to the OpenCV documentation.

## Future Improvements

- Using ssh with OpenSSH (between development computers and the main computer) to program directly on the computer efficiently while other's are working with the control box or robot.
- Using a pure HTML5-based method of serving the GUI multiplexer. We tried using Flask but found that OpenCV worked too irregularly
- Optimizing vision processing code
- Incorporating machine learning into noise reduction, accuracy improvement
