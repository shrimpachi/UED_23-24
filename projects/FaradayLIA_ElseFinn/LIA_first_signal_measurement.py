
# The code to read the serial monitor of the arduino
import serial.tools.list_ports
import time
import matplotlib.pyplot as plot
import math
import numpy as np

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

portsList = []

#get the list of ports
for onePort in ports:
    portsList.append(str(onePort))
    print(str(onePort))

#select which port to use
val = input("Select Port: COM")

for x in range(0,len(portsList)):
    if portsList[x].startswith("COM" + str(val)):
        portVar = "COM" + str(val)
        print(portVar)

serialInst.baudrate = 250000 #this should be the same as the baudrate that is selected/used in the arduino code
serialInst.port = portVar
serialInst.open()



#write the serial monitor of arduino to the commandline
time.sleep(2)
wave1_amp = []
wave2_amp = []
measure_time = []

for i in range(25):
    if serialInst.in_waiting:
        packet = serialInst.readline()
        input = packet.decode('utf').rstrip('\n')
        data = input.split(", ")
        measure_time.append(int(data[0]))
        wave1_amp.append(int(data[1]))
        wave2_amp.append(int(data[2]))

pi = 3.141
#getting the max value of first wave and the time index it is max
wave1_max = max(wave1_amp)
time1 = measure_time[wave1_amp.index(wave1_max)]

# getting the value of the second wave for the same time wave 1 achieved max
wave2_max = max(wave2_amp)
time2 = measure_time[wave2_amp.index(wave2_max)]

# calculating the amplitude difference of the wave for a given time
time_diff = time2-time1
phase_diff = time_diff*360/10000
while phase_diff > 200:
    phase_diff = phase_diff - 360
message1 = "The phase shift: "
print(message1 + str(phase_diff))

# calculating the phase difference between them

plot.plot(measure_time, wave1_amp)
plot.plot (measure_time , wave2_amp)
plot.show()