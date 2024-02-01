#Project status:
+Lock-in amplifier is 2/3th ready, only the multiplier is still missing.
+Measuring the phase shift of the reference signal is accomplished


#Project description

This project describes a setup for making your own low budget lock-in amplifier and use this to demonstrate the Faraday effect of light in a magnetic field.

To get a better understanding of what a lock-in amplifier is and how to use it, I encourage you to read [[project_canvas_ElseFinnRimo.md]]

#How to build a lock-in amplifier
A lock-in amplifier is a device that measures DC voltages of very low amplitudes and/or signals that are buried in noise. With relatively simple electronic components it is possible to build your own lock-in amplifier. This short description is for a lock-in amplifier tuned to measure signals of 100Hz, it is relatively straight forward to adjust the lock-in amplifier for different frequencies, see [[project_canvas_ElseFinnRimo.md]].

##Materials:
+ Breadboard to build your lock-in amplifier on.
+ Jumper cables for the breadboard.
+ Function generator to modulate an AC signal.
+ Arduino to measure the DC output of the lock-in amplifier (also possible to use e.g. a multimeter, in this case I would also advice to use a oscilloscope to measure the AC signals.)
+ Cables to connect the function generator to the lock-in amplifier and the lock-in amplifier to a multimeter.
+ +15 and -15V DC power supply for the OpAmp power supply and neccesary cables to connect the power supply to the lock-in amplifier.
+ Computer to read in the arduino (if using an arduino).

+ Resistors (6x 15k and 2x 2.2k for a 100Hz signal).
+ Resistors (6x 15k and 2x 2.2k for a 100Hz signal)
+ Capacitors (5x 1 uF and 1x 0.1 uF for a 100Hz signal).
+ Opamps (6x).
+ OPA177 or OPA77 for the phase shift.
+ AD360JNZ (2x) for multiplying the signal and reference signal.

Build the lock-in amplifier as shown in figure 1. Be advised to measure each of the six parts to see if they are working before building the next part. NOTE: this lock-in amplifier was build for a frequency of 100Hz, for different frequencies the resistors and capacitors should be changes as described in Lock-in_amplifier.md.

+ The first part (High pass filter) should eliminate the DC component of a signal as shown in figure 2.
[High pass filter](./Images/highpassfilter)
+ The second and fifth part (Multiplier) should multiply the input signal and reference signal and when they have the same frequency give a signal as shown in figure 3 (for in-phase signals).
+ The third and sixth part (Low pass filter) should filter all higher frequencies and give a DC output as shown in figure 4. 
[Low pass filter](./Images/lowpassfilter)
+ The fourth part (phase shifter) should shift the phase of the reference signal by 90 degrees, as shown in figure 5. 
[Phase shifter](./Images/phaseshift)

The DC output of the in-phase (Vx) and out-of-phase (Vy) signal is equal to 0,637A with A the amplitude of the input signal.

#Measurements using the lock-in amplifier:
##Materials:
Self-made lock-in amplifier.
Arduino
Jumper cables to connect arduino to the lock-in amplifier
Function generator + cables to connect to the lock-in amplifier
Python 3.11 (should also work for 3.7).
python library: pyserial, install by using “pip install pyserial”
If not using an arduino: Multimeter + cables to measure output

Now that the lock-in amplifier is build, some measurements can be done.  The input should be a modulated signal with known frequency and a reference signal with the same frequency (e.g. from a function generator).
The output of the lock-in amplifier in measured using an arduino. This could also be done by any other device that can measure DC voltages, e.g. a multimeter.  The output of the lock-in amplifier will give an in-phase DC signal and out-of-phase DC signal which together will give the amplitude of the input. 

##How to measure the phase shift
The first important measurement is that of the phase shift in part four (figure 1). This phase shift should equal 90 degrees in order to get an accurate measurement of the out-of-phase signal. 
[Setup schematic](./Images/Setup_schematic)
[Setup picture](./Images/Setup_foto)
To measure the phase shift, follow the next steps:
Connect the lock-in amplifier, as shown in figure 5, to the arduino and the function generator.
A0 to the input
A5 to the output of the OpAmp
GND to the ground
For the function generator, generate a signal with amplitude of 500mV and a frequency of 100Hz.
Open the python code LIA_first_signal_measurement.py and run the code.
The program will ask: from the printed list select the arduino port (com1, com2… what is being displayed) For linux check which port the arduino is connected to, for instance in the arduino IDE
Now the arduino will measure the input signal from the function generator and the phase shifted signal after the phase shifter. It will compare both signals and give the phase shift between them.

###Frequently Occuring Problems (FOP)
Pyhton gives the error: 'utf-8' codec can't decode byte 0x8a in position 8: invalid start byte —> Run the code again, it will very likely work the second time
Python gives another error —> Run the code again, it will also likely work the second time
Python still gives an error after the second attempt —> Kindely ask your laptop and the arduino to work, give them a pat on the head and try again, hopefully it will work now

If you are not sure the input signal is correct, or something is going wrong in the circuit, you can use an oscilloscope to check the input, output of the phase shift and output of the OpAmp. Since the OpAmp works as a buffer, it is not supposed to change the signal.
Make sure the probe (from the function generator) does not amplify the signal (check for a yellow button on the probe)

##How to use the lock-in amplifier to measure a signal [Preliminary, not tested yet because the lock-in amplifier is not ready]

Now that the phase shift is confirmed to be 90 degrees, the lock-in amplifier can be used to measure a signal. The first step is to connect the lock-in amplifier to the arduino, function generator, power supply and input voltage as shown in figure 6. 
The outputs Vx and Vy can be measured using the arduino and combined will give the RMS value of the input signal by:

A_RMS =  1.11sqrt{X^2 + Y^2} 

