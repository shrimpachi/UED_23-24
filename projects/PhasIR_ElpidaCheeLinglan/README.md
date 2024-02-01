
# Phase transition temperature measurements with PhasIR: melting point of waxes


## Project Description

PhasIR represents a thermal analysis method focused on determining phase transition temperatures. Unlike similar 
techniques, PhasIR uses an infrared camera for measurements. This system enables rapid and precise estimation of 
multiple samples concurrently. It also offers convenience while accommodating small sample sizes and various
materials' form such as powders, liquids.
In this experiment, the goal is to identify the melting points of two different types of wax.
As determining the melting point hold significant importance for identification purposes, given its unique and specific nature for each material. 


## Application

PhasIR facilitates the visualization and extraction of thermal characteristics for various substances, including both pure
elements and combinations. In this particular study, we have chosen to examine different types of wax to measure their 
melting points. The chosen wax are environmentally friendly alternatives to paraffin wax, which are called candellila and soy wax. 
Both materials have been previously researched, so comparing the observed melting point with the data available in the existing literature is possible.


## Requirements 

### Hardware

For this setup a few hardware components are required:
+ FLIR C5 IR camera
+ VWE hotplate - stirrer
+ Aluminium plate with conical wells
+ 3D printed enclosure
+ Laptop

The experiments are done in a dark room to minimise any reflection on surfaces. This will eventually lead to issues when 
data analysing.

### Software

To be able to analyse the images, the following software is needed:
+ FLIR Thermal Studio
+ Python; with the following libraries:
  + numpy
  + matplotlib
  + scikit-image

**Please note:** FLIR Thermal Studio can only be installed on a Windows OS System. A key is also needed to be able to use
the software. 


## Development

### Hardware System 

The hardware has to be set up as follows:
The aluminium plate and the 3D printed enclosure will be placed on top of the VWE hotplate with the camera attachted to
the pole to have a top view of the aluminium plate. 
The camera can be connected to a laptop that has the FLIR Thermal Studio software.
To set up the camera correctly, the temperature scale needs to be changed accordingly for the specific material as the 
melting points are not the same for different materials. Also, the images needs to be takin in gray scale to have a better 
analysis of the image using the software. This can also be done in the camera settings.
For pictures related to the hardware components please refer to the **Hardware folder**.


### Software system
Using FLIR Thermal Studio, thermal images can be received. In this software, it will show you what is directly shown on the camera.
In this software, a video can be taken of the whole melting procedure to ensure the whole melting process has been recorded of an .avi file type. 
This video file will be used in the python script to do image analysis.

In addition to the software for the camera, a python script is made to perform image analysis.
In this script, the relation between pixel values with the corresponding temperature will be determined.
Using this data, the melting point can be extracted and plots will be shown as how the wax will melt. 

For a detailed code related to the software process, check the **software folder**.

**Note:** At this point, the python script can only read the images and videos as the script has not been finished yet.


## Visuals
 
Check the folder **Measurements**.


## Documentation 
For the detailed instructions on reproducing Phasir use Project Canvas.


## License
This project is licensed under the MIT License - see the **License file** for details.


## Acknowledgments
Sanli Faez ,Mariia Selina : Thank you for your significant contributions and guidance to the project. Your expertise 
enhanced the project's quality.

Lili's Protolab : We appreciate the support from Lili's Protolab for providing recourses, components and assistance enabling
us to maintain and improve this project.

Experiment Desing course participants : Thanks yo the participants of the course Experiment design course for their valuable 
feedback and suggestions. 

Linglan Li, Chee Wong and ELpida Iliopoulou : Special thanks to the PhasIR tema for your efforts in maintaining this projects , 
responding to issues.
