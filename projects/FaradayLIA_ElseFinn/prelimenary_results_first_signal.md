These are the first measurements we made on the phase shifter module of the LIA.
THe measurements are conducted as is described in [[README_ElseFinnRimo.md]]. The results of these measurements are described below.

## The measurements (arduino)
When conducting the measurement we found out that the first and second try of running the python code can result in an error. This has no effect on the result and after running the code for a third time it does function properly. The results are as follows:
+ A phase shift of approxemately 70 degrees
+ A phase shift of approxemately 90 degrees
It is yet unkown to why the 70 degree result occurs. The main hypothesis is that it might be due to the sample frequency of the arduino. We are not capable to sample the frequency accurate enough to get a detailed peak of the sine wave, this is why the measured phase shift can differ greatly. 

We also see that the sine wave shape is impacted by the arduino itself when you connect it to the module. The lower peaks seem to get squashed while the higher peaks seem to stay the same. This should not have an impact on the phase measurement as we only use the high peaks for determining the phase. since all the peaks change identical the phase should not change anyhow.

## The measurements (oscillsocope)
When measuring the phaseshift with the oscilloscope we see way more accurate results. To put it simply, we measure a phase shift of 90 degrees.