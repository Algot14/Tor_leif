# Installation

Download and install V-REP from [here](http://www.coppeliarobotics.com/downloads.html)

Pre-requisites:
 * Python3
 * `virtualenv`


Following [this tutorial](http://nbviewer.jupyter.org/github/poppy-project/poppy-humanoid/blob/master/software/samples/notebooks/Controlling%20a%20Poppy%20humanoid%20in%20V-REP%20using%20pypot.ipynb) for pypot and V-REP.

Installation:

```
virtualenv -p python3 venv3
source venv3/bin/activate
pip install pypot
pip install poppy-humanoid
```

Test that it is installed correctly:

```
python
from pypot.vrep import from_vrep
from pypot.creatures import PoppyHumanoid
```



## OLD

```
virtualenv -p python3 venv3
source venv3/bin/activate
pip install poppy-ergo-jr --upgrade
pip install poppy-torso
poppy-services --snap --vrep --no-browser poppy-torso   # V-REP should be started
```

Follow the instruction for the Hello world example [here](https://docs.poppy-project.org/en/programming/python.html)
