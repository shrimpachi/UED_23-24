*Utrecht Experiment Design 2022*

# Project canvas

### POP

+ **Purpose**: to make the project requirements, boundaries, and goals as concrete as possible  
+ **Outcome(s)**: list your project steps, the best possible outcome, and the minimum desired outcome  
+ **Process**: self-reflection and discussion with your mentors

PROJECT NAME: Sap Flow Meter

TEAM: Rimo, Linglan

## Project description  
Trunk sap flow serves as an important indicator of a tree's water consumption capacity and is critical for targeted irrigation and fruit yield calculations.

In this project, we will build a low-cost and transportable sap flow meter based on guidance from online resources. This sap flow meter uses the heat ratio method (HRM) to measure the flow of sap in the tree. 

After the measurements, we will collect the data and process the data to get a graph of sap velocity versus days. By understanding this, people can plant orchards with efficient irrigation systems while saving water.

### Open Hardware and its purpose
1. Measurement probes:
* 12 AWG piercing needles, QTY 3
* Glue syringes, QTY 2. (Make sure the tip is smaller than 1.8mm in diameter)
* Thermal paste
* Gorilla Glue
* Assembled flex probe PCB (henceforth called PCBA)
* Q-tip

The measurement probes will be inserted into a tree, and send digitally encoded temperature back to a datalogger module.

2. Datalogger: Data collection.

3. Base station: It will maintain a local database of time-stamped sap flow measurements.

### Potential users of the hardware and its added value
It can be used to plan orchard irrigation and reduce water waste.
### Underlying physics and working principles
This sap flow meter  utilizes the Heat Ratio Method (HRM) for measuring the rate that sap is flowing in a tree. 

HRM is a thermometric method of measuring sap flow in xylem tissue which uses a short pulse of heat as a tracer. By measuring the ratio of heat transported to two symmetrically placed temperature sensors, the magnitude and direction of water flux can be calculated.

The Heat Ratio Method (HRM) sensor is a modified heat pulse technique. HRM consists of three needles: two measurement needles located equidistant above and below a central line heater. It is a pulsed technique using a short two to six second pulse of heat and a 100 second measurement window. 

### Required components and planned alteration to the reported recipe
https://agsci-labs.oregonstate.edu/openslab/2018/06/12/2018-6-4-build-guide/
### Chosen method of interfacing with a computer
Once sap flow has been measured, it is transmitted back to the Feather M0 via an I2C line. Once data is at the Feather, it is stored in a CSV file on its SD card. Then we can remove the SD card from the sap flow wing and read it on a computer. There will be files that describes the system behavior with timestamps. 

### Planned measurements
After setting up the equipment, we will insert the measuring probes into the tree trunks for measurement. Once it has been measured, we can read data from the SD card for analysis and graphing.

## Mid-course review of your project state (fill this mid-course)
*Note what progress you have made and what adjustments you need to make to finish your project in time.*


## Final review of the project accomplishments (fill at the end of the course)

+ list the achievements of your project  
+ write down your plans for improving your project or making it more widely accessible 

