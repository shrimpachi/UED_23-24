# Homework to finish before Thursday September 23rd

+ Make sure you have a working python installation.  
    - Get the latest version of Python 3 installed and running.
    - The preferred IDE is [PyCharm](https://www.jetbrains.com/pycharm/) (community edition)
    - other IDEs such as IDLE will suffice, be aware thad on some OS, Spyder run inside Anaconda might raise conflicts for PyQt apps.
    - Installing pip is highly recommended.

## Simple GUI with Matplotlib, camphew

+ Make sure you have Matplotlib and Numpy packages installed 
+ In order to follow along on Thursday you'll need to be familiar with some python basics.  
    - Look through the [some_python_basics.py](./some_python_basics.py) file to see if you understand it.  
    - Run the file (or bits of it) in an interactive python console to play around with it and increase your understanding where required.
 
 ## Advanced instrumentation programming, labphew
 
 NOTE: The following steps may requiring tinkering with your python packages. 
 If you do not have prior experience with object oriented programming in python, your time is better spent on 
 practicing with single script python codes of the camphew.
 
+ Create a [github](https://github.com/) account.
    - And fork the [labphew repository](https://github.com/SanliFaez/labphew) to your own account
+ Install Git on your pc.  
    - Optionally you can also install a git client. (Github Desktop might be useful but I don’t have any experience with it)
+ Clone your own labphew repository to your pc.
+ It is strongly recommended to create a virtual environment.  
    - If you have conda you could create one like this from a (anaconda) command prompt `conda create --name my_env python=3.10`    And activate it with `conda activate my_env`
    - (Note, you can pick any name instead of my_env and note that python versions 3.6 and 3.10 should works, but 3.9 will not).
    - as alternative to anaconda, you can use `virtualenv` or the environments in PyCharm.
+ From within the repository directory, install your local copy of labphew in editable mode: `pip install -e .` (make sure to include the dot at the end)
+ Test it with: `labphew start blink -d`  
  If a window shows, everything is good. If you run into issues contact Aron Opheij on Teams before Thursday!
+ Install [Digilent Waveforms](https://digilent.com/reference/software/waveforms/waveforms-3/start) (if you don't want to fill in the form you can also install the latest [previous version](https://digilent.com/reference/software/waveforms/waveforms-3/previous-versions))
+ Test if labphew can use it: `labphew start ad2-sim -d`

