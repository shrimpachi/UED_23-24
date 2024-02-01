*Utrecht Experiment Design 2023*

# Project canvas

### POP

+ **Purpose**: to make the project requirements, boundaries, and goals as concrete as possible  
+ **Outcome(s)**: list your project steps, the best possible outcome, and the minimum desired outcome  
+ **Process**: self-reflection and discussion with your mentors

PROJECT NAME: OSMS

TEAM: Elena Gerasimos

## Project description  
Spectrophotometry deals with the measurement of the interaction of light with materials. Spectrophotometric systems are widely used in studies across many fields. Many of these applications require highly precise and reliable data which often leads to the implementation of complex and expensive spectrophotometric systems. In this work we describe the construction and performance of the portable, low-cost, customizable and fast (registers the whole wavelength range at once, allowing to obtain a full absorbance spectrum every second) open-source miniature spectrophotometer (OSMS). The data acquired can be displayed on a computer interface. All design and software files are open-source and are intended for the device to be easily replicable and further customizable to suit specific applications. The assembled device can measure absorption in the wavelength range from 450 nm to 750 nm with a resolution of 15 nm and is housed in a 90 x 85 x 58 mm casing.

### Open Hardware and its purpose
The open hardware used in this project is the Open Source Miniature Spectophotometer (OSMS). 

### Potential users of the hardware and its added value
There have been several projects that have focused on building a
portable and compact spectrophotometer that could be used on-the-go,
however, most of these projects have been aimed at creating very
low-cost devices, usually to be used for educational purposes,  not for
acquiring scientifically significant data, which requires reproducible
and accurate measurements. Our OSMS is designed to offer much more
accurate measurements, while remaining affordable and highly portable.
Also, although the device is generally designed for liquid samples,
solid samples can also be measured if attached to a quartz holder.
### Underlying physics and working principles
Spectrophotometry is a method to measure how much a substance absorbs light by measuring the intensity of light as a beam of light passes through sample solution. The basic principle is that each compound absorbs or transmits light over a certain range of wavelength. This measurement can also be used to measure the amount of a known substance. Spectrophotometry is one of the most useful methods of quantitative analysis in various fields such as chemistry, physics, biochemistry, material and chemical engineering and clinical applications.

A spectrometer is an instrument that detects the characteristics of light scattered,
emitted, or absorbed by atoms and molecules. Radiation from an appropriate source is directed toward a sample. In most spectrometers, light transmitted, emitted, or scattered by the sample is collected by
mirrors or lenses and strikes a dispersing element that separates radiation into different frequencies. The intensity of light at each frequency is then analysed by a suitable
detector. With the spectrophotometer, the amount of a known chemical substance (concentrations) can also be determined by measuring the intensity of light detected. Depending on the range of wavelength of light source, it can be classified into two different types: UV-visible spectrophotometer and IR spectrophotometer. In this project we will use a spectophotometer in the visible range of the spectrum (400-750nm).

In visible spectrophotometry, the absorption or the transmission of a certain substance can be determined by the observed colour. For instance, if a solution sample absorbs red light (700 nm), it appears green because green is the complementary colour of red. Visible spectrophotometers, in practice, use a prism to narrow down a certain range of wavelength (to filter out other wavelengths) so that the particular beam of light is passed through a solution sample.

Absorption spectrophotometry is based on the ability of a substance to absorb radiation. Measurement of the degree of absorption at various discrete wavelengths yields a pattern of absorbance relative to wavelength — an absorption spectrum — characteristic of the light-absorbing substance. Such absorption spectra may be used to identify or characterize unknown compounds. In addition, the amount of absorbance of monochromatic light is often proportional to the amount of absorbing substance, thus yielding a method for quantitative estimation of the substance. Absorption spectra  show the change in absorbance of a sample as a function of the wavelength of incident light. For this purpose it is convinient to intoduce to concept of absorbance A:

$A=-log_{10}(\frac{I}{I_{o}})$
where $I_{o}$ is the original intensity of the light beam and I is the intensity of light that reaches the detector. Therefore, absorbance is a direct measure of how much light is absorbed by our sample.
The absorbance is linearly proportional to the molar concentration of the sample; which enables the concentration of the sample to be calculated from the absorption spectrum using the Beer-Lambert Law:
$$A=εLC$$
where ε is the molar absorptivity, L is the distance covered by the light inside the the sample and C is the concetration of the absorber.

### Required components and planned alteration to the reported recipe
++ Arduino Microcontroller

++ C12880MA Spectrometer

++ LED Nichia Optisolis

++ Resistor 1 k

++ Resistor 2.2 k

++ Resistor 4.7 k

++ Switch

++ 9 V battery

++ 3D printed container

++ 3D printed lid
### Chosen method of interfacing with a computer
For interfacing with a computer an arduino will be used. This was chosen
because of the arduino's ease of use, affordability, availability and
because it is operated by an open source software and globally known
language (Python).
### Planned measurements
We plan to measure different kinds of liquid organic materials. We will focus on everyday consumer products such as milk, olive oil and alcochol products.

## Mid-course review of your project state (fill this mid-course)
*Note what progress you have made and what adjustments you need to make to finish your project in time.*


## Final review of the project accomplishments (fill at the end of the course)

+ list the achievements of your project  
+ write down your plans for improving your project or making it more widely accessible 


