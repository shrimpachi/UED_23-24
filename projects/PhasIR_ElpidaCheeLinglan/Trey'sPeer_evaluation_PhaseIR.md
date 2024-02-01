# Reproducibility report

## Experiment/team: 
Phase IR by Ελπιδα, Chee, and Linglan

## Reviewers: 
Trey Grijalva #4588053

------

## Report 

### Documentation:

1. Could you understand the purpose of the experiment? Explain.
Yes, the name is already pretty self-explanatory, but they clearly outlined that the purpose of their 
experiment is to determine the phase transition temp of a substance -- in this case, wax -- with an IR cam. 
My one critique is the last sentence of the Description section should be their Application section.

2. Were the safety instructions clear?
There don't appear to be any safety instructions, but it's not a dangerous experiment, 
considering wax melts at around 65℃. I don't recall seeing a particular requirement for a section on this.

3. Was the starting point and the expected duration of the measurements clear in the documentation?
No, but this wasn't an outlined expectation, so I won't be deducting anything from the score for this.

4. Does the documentation contain all necessary information to successfully reproduce the measurement? If not, what was missing?  
No, it doesn't include any references to the visuals, just pictures in folders not connected to the README.
References would be really helpful to explain the setup process.

5. Did you get stuck at some point? What extra help did you need to proceed? 
I'm not sure which 3d printed enclosure I'm supposed to use, there are 5 of various sizes and colors. based 
on the title of some of the pics, I think I'm supposed to use 2 at a time, but I can't tell based on the 
final setup pic.

6. Are you encouraged to reproduce previous measurements? How easily could you navigate through the project documentation?  
Beyond the fact that it's documented in a gitLab repo, I'm not explicitly called to reproduction, but this 
isn't mentioned in the project template either, so I won't deduct any points for this.

7. What can be improved in the documentation?
The visuals should be referenced in a step-by-step guide contained in the README. The biggest thing missing 
is the steps to actually run the hotplate and record the phase change. I don't know what temperature I'm 
supposed to set the hotplate to so I can collect data.

8. Something I liked about the documentation?
The 'BOM' (bill of materials) is pretty solid. We didn't make a nice table to price out all of the 
equipment and supplies we used, so I'm going to steal this idea.

On the scale of 1-5 (1: top quality, 5: disappointing) how do you assess the documentation? Please justify your grade based on the questions above.

#### Documentation grade:
3

### Measurements:

1. Can you operate the setup with the provided instructions?
After analyzing the JPEGs I set it up and I believe I could run it, but I don't have access to a dark room to really do the setup justice. There are just too many windows and lights in the rooms and labs I have access to. The reflections seen by the camera are quite impressive, as it sees an IR reflection of me on the hotplate like it's a mirror, but visual spectrum doesn't reflect off of the dirty surface well at all. But the biggest thing preventing me from actually measuring anything is not knowing exactly what temp range I need to target over what time period.

2. How close were the results you obtain to the previously reported results?
N/A

3. Is the analysis procedure easy to understand? Summarize it briefly in your own words.
The analysis seems to be straighforward, I feed the recorded FLIR video script to the python script in the Software folder and it spits out results.
The problem is, the python script is empty: 0 Bytes.

4. Is the setup robust and safe to operate?
I wouldn't say it's extremely robust, but it does seem pretty safe.

5. Did you encounter any issues? Could you troubleshoot those issues without contacting the owners?  
Yes, I ran into the aforementioned issues and couldn't resolve them alone.

6. What part of the measurement procedure did you appreciate most?
I always love messing with a thermal camera.

On the scale of 1-5 (1: top quality, 5: disappointing) how do you assess the measurements reproducibility? Please justify your grade based on the questions above.

#### Reproducibility grade:
5

### Interactions:

1. If you had to perform work on this part of the project, would you have selected the same goal or aimed at something else? Please, explain.  
Yes I would have selected the same goal, because I'm not really sure what else I could select. We were supposed to reproduce an Open Source Project, so I thought we were supposed to do our best to pursue a reasonable reproduction with what we had.

2. Which instructions did you need from the owners on top of the written files?
In the spirit of true reproducibility I did not contact the owners. If I did contact them I would ask them 
what temperature I should target for data collection and for the python script they used for analysis. 

3. Does the experiment accomplish its stated purpose?
Not quite.

4. What do you recommend to the project owners to improve their complete package?  
Create a comprehensive README with the visuals, add the python script, and apparently you need some safety instructions.

______

### Response to reviewers

_This part must be filled by the project owners based on the peer feedback_

1. Which major adjustments did you make based on this feedback?  
2. Do you agree with the graded assessment of the reviewer?  

On the scale of 1-5 (1: really helpful, 5: disappointing) how do you assess the peer evaluation? Please explain.
