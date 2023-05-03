
# Robot-Kinematics
This library contains functions that will help you  about robotics kinematics  

## Jacobian Matrix

The Jacobian matrix is a matrix that composes the first-order partial derivatives of a multivariable function. The joints of the robot move with certain velocities then we might want to know with what velocity the endeffector would move. Here is where Jacobian comes to our help.

## Robotic Manipülatör with 2 axis
This function help to calculate Velocity Kinematics of 2 axis robots.

![2axis](https://user-images.githubusercontent.com/36998513/233043637-d5b4c482-9cf0-45e6-b7f7-b90e9c909c93.png)
 

## Homogenous Matrix
A system of linear equations having matrix form AX = O, where O represents a zero column matrix, is called a homogeneous system.In this project, rotation of homogeneous matrices was performed.


![turn](https://user-images.githubusercontent.com/36998513/233045775-6645e372-6bb7-4ec5-8554-61702a7706f5.png)


## Contributing 

All contributions, bug reports, bug fixes, documentation improvements, enhancements, and ideas are welcome.

A detailed overview on how to contribute can be found in the contributing guide.

  
## Installation 

Clone project

```bash
  git clone https://github.com/barisceliker1/Robot-Kinematics
```




  
## Examples

```python

##Jacobian matrix

from jacobian import jacobian

print(jacobian(30,40,2,3))

##Robotic Manipülatör by 2 axis

from axis2 import axis2

axis2(3,5,20,40,30,50)


  
