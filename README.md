# ROV2019

45C Robotics' robot code for the 2019 MATE Competition. 

# Components

We will be adding more components as the season progresses, but for now, these are the components we are adding to this year's system:


### ESC Control

Tx and Rx communication was used between the Arduino Uno and the Arduino Mega. The Arduino Mega recieved data from the Arduino uno. Joystick values were mapped to motor outputs. 


### PID

The MPU6050 module is being used as a gyro and accelerometer to generate the acceleration and raw position values necessary for calculating actual error, and using the error, the kP, kI, kD constant values.

Note: The constants in the file must be tuned, and in their current state they are *untuned*. Perhaps we may eliminate kI and kD if we deem them unnecessary. 

#### Vision

[https://github.com/opencv/opencv/wiki/OE-4.-OpenCV-4](OpenCV4) has been released. 

Images should be processed using the pipeline created in the  **imagePreProcess** class, which erodes/dilates and blurs input video. 

##### Conventions

Variable names should be declared using *mixed camel case* nomenclature (e.g. waitForInstructions), and function names should be lower case, with underscores in between each consecutive word.

Proper Object Orientation principles should be maintained whenever possible; including for one-use scripts (e.g. installation and instruction programs)


