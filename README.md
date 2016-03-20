# Gate Peaces

Seperate pieces of code for the gate system.
These are parts of the gate system to be put together. 


## Directories

What do those directories in this project mean?

* bin - This directory is for entry points of this tool, like the command to run it all.
* lib - Where the actual project code goes.
* tests - Where the unit tests go.
* example - Example code for referencing.


## Operation

This is how you can run the program.
```sh
./run.sh
```

```sh
PYTHONPATH=. bin/gate
```
## Required versions
Raspbian jessie based version 8.x
Python version > 3.2

## Required libraries

Run the following command to install all necessary libraries for this tool.

```sh
sudo apt-get install python3-setuptools
sudo apt-get install python3-smbus
pip3 install -U pytest
```


## Development

Run this command to execute all available tests and see if everything works as intended.

```sh
py.test
```

#items installed

sudo pip3 install wiringpi2

