# Meeting 26-10-23
Attending: Finn, Rimo, Else (online)

## Planning:
Finn: Use python to read data from the arduino (thursday 26-10 + monday 30-10)
Start with measurement setup (thursday (2-11?)
Rimo: Calculate from data the phase shift between two signals (thursday 26-10 + monday 30-10)
Start with measurement setup (thursday 2-11?)
Else: Documentation DEADLINE if necessary help with python script to calculate the phase shift (27-10 + 30-10)
Finish lock-in amplifier (Thursday 2-11?)

## Materials:
Lasers: Finn will contact
Magnet: Else will contact Rene Barthel
Lock-in amplifier: Else will contact Dante

Else will send the necessary equations to calculate which resistors and capacitors should be used to get a phase shift of 90 degrees dependent on the frequency.

# Meeting 26-10-23
Attending: Gerhard Blab, Finn, Rimo, Else (online)

## Things to consider according to Blab when choosing a modulation frequency:
Take into account the readout frequency of the arduino
Take into account the external frequencies (50Hz, 140-143 Hz ventilation)
When modulating the B-field:
How will the B-field be changed? With an electromagnet there is a certain time constant which means that there is a limit on how fast the B-field can change. The time scale is dependent on how fast we can change B
The changes in the B-field might not be instantaneous —> investigate how instantaneous these changes are
When choosing a low frequency take into account a longer integration time and this longer measurement times

## Make an estimation on what to expect:
How high should the B-field be? Take into account possible (safety) precautions
How high should the intensity of the laser be? —> High enouth to measure but not too high for the electronic components
What modulation frequency should be used?
What is the expectation of signal amplitude?
What polarisation orientation would be best? Parallel —> signal will decrease, perpendicular —> signal will increase
What is going to happen with the effect when we change from a constant B-field to a time dependent B-field?
DO SOME CALCULATIONS:
Is the input signal an exact sine-wave? What will happen with the multiplication if it is not?
How does B change when current is changed? —> Kirchoff for a coil
The rotation is directly dependent on B
Magnetic field will look like it is filtered

Arduino: Blab can help with the arduino programming
PulseIn function
Interupt function
What range do we measure voltage
ADC 16 bit instead of arduino (10 bit) —> Higher resolution?

## Measurement setup:
Light pass filter to only measure the laser?
Show how powerfull the LIA is by measuring both in dark and light and see how much of the background light noise you can filter out
What type of connections will we use? —> BNC (no bananas!) AND PROPERLY GROUND THE DEVICE, otherwise you will create an attena 
What wavelenght and material will be used to maximize the verdet constant and thus the rotation, do we want a verdet constant that is relatively constant in wavelenght?
