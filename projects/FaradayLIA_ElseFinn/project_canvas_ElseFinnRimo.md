# Project canvas
PROJECT NAME: Measurement Of the Faraday Effect using a Lock-In Amplifier (FaradayLIA)
TEAM: E.M Okkinga, F.M.A Smits

## Project description  
A lock-in amplifier is a device that measures small signals that can barely be distiguished from noise. The goal of this project is to create a lock-in amplifier using affordable and easy to get materials that can be used for DIY projects at home but can also serve an educational purpose for engineering and physics faculties to understand the underlying working principles of lock-in amplifiers. 
With this lock-in amplifier small signals like small intensities of LED lights can be measured even when there is a lot of background noise (e.g. amient light). This created lock-in amplifier is therefore an ideal instrument to demonstrate and prove the faraday effect, where the polarization of light changes slightly when traveling though a magnetic field.

### Open Hardware and its purpose
To make this device accessible for any potential user, the setup will consist of affordable and easy to get equipment and will be made up of components that can be explored and altered individually. The computer interface will use an easy and globally used open source programming language and software to make sure that users can easily make personal alterations to meet their experiment goals. This also ensures that the setup is accesible for anyone with an internet connection in need of such a device.

### Potential users of the hardware and its added value
The target group of this project are researchers with limited funding and/or resources that need a lock-in amplifier for measurements. A lock-in amplifier can be very expensive but the applications are limitless, this low-cost lock-in amplifier can be the solution. 
Another important target group are engineering and physics faculties, where this low-cost lock-in amplifier can be used for educational purposes. This device could become an affordable alternative for experiments and to understand the underlying working principle behind the lock-in amplifier.

### Underlying physics and working principles
Small signals (DC) are measured by modulating a frequency over the signal (Input). Using a reference signal (Ref) with exactly the same frequency, the frequencies of the noise can be filtered out. This is done by multiplying the Input and Reference signals and integrating over a time longer that the period of the signal (Low-pass filter). This isolates the frequency of the input signal with the same frequency as the reference signal and all other frequencies are filtered out. The output is the in-phase RMS value of the input signal.
By shifting the reference signal by exactly 90 degrees, the out-of-phase RMS value of the input signal can be measured at the same time. This allows to measure both the value and the phase compared to the reference signal.
Because the lock-in amplifier is in fact a filter with a very narrow bandwidth, this device is especially good for measuring signals with lots of noise, since all the noise is filtered out. 

Using the lock-in amplifier, the Faraday effect can be demonstrated. The Faraday effect is the effect that polarized light rotates when traveing though a magnetic field. Using two polarizing filters,rotated 90 degrees to each other, and a magnet in a medium like oil (where the rotation is relavely large), it can be shown that light still comes trhough the second polarizing filter,which is only possible if the light is rotated slightly. A fotodiode will give a certain amount of current dependent on the intensity of light. This current can be measured with the lock-in amplifier by oscillating the magnetic field. By varying the magnitude of the magnetic field and measuring the intensity of the rotated light, a correlation between B and the rotation angle can be measured.

### Required components and planned alteration to the reported recipe
+ For the lock-in amplifier:
+ Breadboard (with 5 inputs)
+ cables
+ Resistors
+ capacitors
+ 5 opamps UA741
+ phase shifter: OPA177
+ 2 Modulator/deodulator: AD630
+ Opamp power supply (+/-15V)

+ Arduino

+ For the experiment:
+ 2 polarizing filters
+ Glass with oil
+ Coil for in oil
+ Laser
+ Fotodiode
+ Resistor
+ Power supply for coil


### Chosen method of interfacing with a computer
For interfacing with a computer an arduino will be used. This was chosen because the arduino is easy to use, affordable to get and is operated by an open source software and globlaly known language (Python).

### Planned measurements
To test how good the lock-in amplifier works, measurements will be done by producing an oscillating signal and measure the output using both the low-cost lock-in amplifier and a commercial lock-in amplifier to verify. The frequency and amplitude of this input signal is varied to measure the region of frequency and amplitude the lock-in amplifier can operate. 
To demonstrate the Faraday effect, the intensity of the light after the second polarization filter is measured using a photodiode and the lock-in amplifier. The intensity as a function of the magnitude of the magnetic field is measured.

## Mid-course review of your project state (fill this mid-course)
*Note what progress you have made and what adjustments you need to make to finish your project in time.*


## Final review of the project accomplishments (fill at the end of the course)
+ list the achievements of your project  
+ write down your plans for improving your project or making it more widely accessible 

