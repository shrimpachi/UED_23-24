*Utrecht Experiment Design 2023*

# Project canvas

### POP

+ **Purpose**:Study the phase transitions  of different types of waxes by integrating PhasIR, a thermal analysis method. 
+ **Outcome(s)**: Define the melting point temperature of waxes with as much as possible accuracy.
 
## PROJECT NAME:Phase transition temperature measurements with PhasIR: melting point of waxes
### TEAM: Chee Wong, Elpida Iliopoulou, Linglan Li


## Introduction to PhasIR

### Project description  

In this project, thermal properties of materials will be researched. Using a setup called PhasIR, we can determine 
phase transitions by using infrared camera.This project will explicitly use soy wax as material of choice to determine its 
melting point.It is a more eco-friendly than its current alternatives, paraffin wax. The goal of this project is to compare 
the results with literature to see how accurate PhasIR is.

### Open Hardware and its purpose

The chosen Open Hardware, referred to as PhasIR, functions as a thermal analysis system. It is used for the purpose of  
investigating phase transitions. It differs from other DTA techniques because it uses an infrared  camera in order to 
visually capture the changes. Furthermore, it allows for the rapid and accurate determination for many samples concurrently. 
The outcomes achieved are comparable with those we get from differential scanning calorimetry (DSC) 
for instance, which is both expensive and time-consuming. Those were the basic drawbacks that lead for a quest of an 
alternative method. In combination with an open software, analysis and extracts the phase transition temperatures.

### Potential users of the hardware and its added value

With the ability to efficiently analyze a large number of samples very quickly, PhasIR appears to be an excellent solution for 
individuals who want to proceed a routine quality control. It can be used in a wide range of applications, including 
sustainable 'green' engineering, pharmaceutical research, materials science, forensics, and polymer engineering, among others.

Some of its advantages are listed below:

1.Provides users with the flexibility to customize. 
2.It can be easily reproducible and adaptable.
3.Affordable method comparing to other DTA techniques.
4.High accuracy in thermal analysis.


### Underlying Physics and Working Principles


+ Heat Transfer and Thermodynamics:

In thermal analysis, principles of heat transfer and thermodynamics are fundamental. 
1. Heat is transferred between the sample and the reference material.
2. Heat capacity is material-specific and influences temperature change during phase transitions. 
3. The first law of thermodynamics states that energy is conserved and can only be transferred or converted.

+ Electromagnetic Radiation and Thermal Energy:

Phasir uses an infrared camera, involving principles of electromagnetic radiation and thermal energy.
1. All objects above absolute zero emit thermal radiation.
2. Planck's law describes the density of electromagnetic radiation emitted by a black body in thermal equilibrium.
3. Wien's Displacement Law relates the temperature of a blackbody to the peak wavelength of its emitted radiation.

- Emissivity:
Emissivity is the efficiency in emitting thermal radiation.
1. Part of Stefan-Boltzmann Law, describing the intensity of thermal radiation emitted by matter.

+ Thermal Conductivity:

Property describing a material's ability to conduct heat.
1. Fourier’s Law gives the rate at which heat is transferred through thermal conductivity.

+ Transitions and Heat Flow:

PhasIR detects changes in heat flow during phase transitions that  involve temperature (T) and pressure (P).
Heat flow associated with a phase transition is calculated using ΔQ = ∫(ΔT) dT.
 
+ Melting Point:

The temperature at which a solid becomes a liquid.
1. Melting points are characteristic properties used for substance identification.
2. PhasIR observes changes in heat flow beyond the melting point, indicating the transition from solid to liquid.


### Working Principles of PhasIR-Get an idea of how it works

PhasIR’s basic working principle is based on  measurements of  temperature differences between a sample and a reference
substance.
+ Sample and Reference: In this setup, the reference material should be well-established and remaining unaffected by any 
phase changes. For our case the black anodized aluminum plate functions as the reference temperature point for the entire 
plate, while the sample's temperature is placed at the central point within the conical wells.
+ Simultaneous Heating or Cooling: To achieve this, we use VWE Hotplate Stirrer along with aluminum well plate systems. 
This arrangement ensures that all samples experience controlled heating or cooling .
+ Measurement of Temperature Difference: Once the temperature ramp is initiated at the desired temperature , a range of
20 degrees in order to find the melting point in between and collect enough data for the plot ,we manually start  the
infrared (IR) camera using Flir Thermal Studio to collect data . As the plate undergoes heating, the camera captures 
and records the temperature of objects within its field of view.
+ Heat Flow and Thermal Events: When in the sample a thermal event happening, it either absorbs or releases heat. 
This heat flow is reflected in the temperature difference between the sample and the reference material. 
Consequently, we obtain graphs illustrating these variations.


## The setup

### Required components 

The components needed are shown in the table below, with  their price.Those were the components used on the open 
Hardware paper we based on. The obtained bill is also confirms the affordability of the set up. A detailed list of the 
components and their prices is given on the Hardware folder.


| Item                    |  Use                                           			|					                                                                                                                                                    
|-------------------------|--------------------------------------------------------------|
| Flir C5 infrared camera | LWIR camera                                                   |                                                                                           
| VWE Hotplate Stirrer    |Heating -cooling plate                                        |                                                                                      
| USB  Cable  type C      | Connect the camera to laptop                                  |                                                                                                          
| Anodized Aluminium Bar  | To make the top plate and the wells                           |  
| Soy wax                 |One of the materials needed for the measurements              | 	
| Candellila wax          | One of the materials needed for the measurements -Calibration | 
| ABS Filament            | Make a confinement to capture the same position               |                                                                       

*More details on Hardware folder*

**NOTE** :
Be aware of the type that the data are being collected when purchasing an infrared camera. In order to perform scientific 
measurements and extract precised results it is important to get a camera the saves the data in an uncompressed form. 
Flir C5 gives pictures in .jpg form that is a compressed type of file .

### Constructing the Phasir setup:

+ Place the long stick onto the circular reception at the rear of the Hotplate stirrer.
+ Secure the enclosure onto the stick, ensuring it fits  onto the heating plate.
+ Affix the smaller stick to the camera using the special screw provided.
+ Utilize the receiver part to connect the camera to the long stick, ensuring it captures the entire image of the 
aluminum plate.(Estimated height: approximately 30 cm, with deviations to be adjusted to meet the objective.)
+ Place the aluminum plate inside the enclosure to ensure stability.

![steps to construct phasir.png](..%2F..%2F..%2F..%2FMASTER%2F1st%20SEMESTER%2FExperiment%20Disign%2Fpictures%2Fsteps%20to%20construct%20phasir.png)
 
**Note:**
Exercise caution when 3D printing the enclosure, taking into consideration the melting point of its materials that is made of.

*Flir C5 Infrared Camera Operation:*

+ Activate the Flir C5 IR camera.
+ Adjust the settings as follows:
- Set the image mode to thermal.
- Configure the color setting to Black - Hot.
- Set the temperature scale within a range of 20 degrees, depending on the material being analyzed.Keep in mind when setting 
the temperature range it might not stick to the exact values we aim to.
+ Connecting the Camera:
Link the camera to a laptop by employing a Type C USB cable.

**Important Notice:**
Ensure the exclusive use of a Type C USB cable.

+ Software Application:
Download Flir Thermal Studio for capturing videos and images.

### Check the proper functioning of the components

The initial step involves verifying the proper functioning of each component.

*Heating Plate*
It is important to assess the temperature fluctuations of the heating plate, taking them into account during data collection,
if there are any. To conduct this evaluation, a thermocouple is used to measure temperature values at specific points on 
the reference material with and without water . In the latter case, we use water to check what is the temperature deviations 
when a sample is placed on the wells. This step is critical because the accuracy or deviation of the temperature values 
on the aluminum plate is used for determining the melting point,and consequently giving the results .
 
To conduct the verification process, here is  briefly presented the *functioning of the Hotplate* stirrer's heating plate:

+ Activate the Hotplate by pressing the on/off button located in the right corner of the machine.
+ Adjust the target temperature by using the arrows on the left side; this will represent the maximum temperature the
system aims to achieve.
+ Initiate the heating process by utilizing the on/off button adjacent to the arrows.

Here is the procedure for checking temperature deviation:
+ Power on the heating plate and set the temperature to a specific value, we used, T = 40.
+ Allow the system to reach the desired temperature (indicated by a beep sound when ready).
+ Use the thermocouple to measure the temperature in two cases :
1.  Without a sample
2. With a water sample
Check the temperature in the four corners and at the center of the aluminum plate (as shown in the picture below) , for the temperatures both inside and
outside of the well.


To check the full results we got to compare / understand the results  of temperature deviation of the plate use the folder **measurements**.

## Planned measurements


Calibration of a thermal analysis system, like the PhasIR system, is crucial to ensure accurate and reliable measurements

*NOTE*: Flir is auto calibrated camera that does calibration when needed .
(We just need to press the calibration button before starting the video capturing in the Flir Thermal Studio environment) .

How calibration is performed:
+ Choose reference materials with precisely known thermal properties, often with well-defined melting points. 
+ Ensure the thermal analysis system is set up in a stable environment.All measurements occur in a dark room to decrease any 
reflections in our set-up that may affect our measurements.

1. Cut the sample in similar pieces and place them inside the conical wells. Put the aluminum plate in the enclosure and we 
are ready to start the process.
2. Since we are using candellila wax, as our reference material for calibration with known melting point at 72.5 °C.
We set the temperature of the heating plate at *78°C* (can differ from case to case depending on the range we want to measure.)
Warm up the system in a range of 20 degrees,he range was used is 60-80 degrees, for the camera to capture the  to find the melting point of candelilla wax.
3. Allow it to reach a consistent operating temperature before you stop the measurement.
4. Verify sample temperature accuracy based on literature and adjust the system settings if needed.(*more details will be provided*)
 

Then , we are ready to perform our main measurement on soy wax melting point following the same process with candellila wax.


## Chosen method of interfacing with a computer

The PhasIR hardware system is used along with an open-source Python-based software, designed to facilitate analysis of the 
output video from the IR camera in the setup. This package simplifies data exploration by enabling users to extract and 
analyze results directly from a Jupyter Notebook. The open-source package can be broadly categorized into two main
sections: image analysis and thermal analysis.



**Image Analysis**


**Thermal Analysis**




## Mid-course review of your project state 
**26/10/23**

So far, the form of setup was completed so that we could perform control on our components to verify if  they work
properly. Temperature deviation of the aluminum plate and calibration of the sample temperature have already been done. 
In that stage we are working on the python script to extract and analyse our data . We manages to extract the frames of 
the video that was captured.(26/10)




## Final review of the project accomplishments (fill at the end of the course)

+ list the achievements of your project  
+ write down your plans for improving your project or making it more widely accessible 

