# ROV2019

45C Robotics' robot code for the 2019 MATE Competition. 

# Components

We will be adding more components as the season progresses, but for now, these are the components we are adding to this year's system:


### ESC Control



### PID

The MPU6050 module is being used as a gyro and accelerometer to generate the acceleration and raw position values necessary for calculating actual error, and using the error, the kP, kI, kD constant values.

Note: The constants in the file must be tuned, and in their current state they are *untuned*. Perhaps we may eliminate kI and kD if we deem them unnecessary. 
