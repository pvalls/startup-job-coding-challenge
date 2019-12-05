# Coding Challenge - Sunlight Hours
>  Solution proposal submitted by Pol Valls Rué.

This is a coding challenge I completed as part of the selection  process for a <i>software developer / backend engineer</i> position at a well-known barcelona based technology startup.

I recommend it as preparation for future applications as well as a programming learning and problem solving exercise.

The provided implementation of the solution was developed with the PyCharm CE IDE in Python 3.7.5.

## Running the project
#### Requirements
- Python 3 interpreter. Optionally I would recommend using an IDE such as Pycharm and a virtual environment such as Conda.
- Python environemnt with modules:
	- math
	- json
	- time 
	
#### Run the project

Run the main program interface (provided solution) executing the provided run_tests.py file. Use the IDE Run option or in the terminal type:

```
$ python run_tests.py

```


## Problem statement
A new feature has been requested for our room listings in future Barcelona: We want to display the sunlight hours that a given apartment receives in a day.​ To ensure our announced sunlight hours will be always true, we decided to display the sunlight hours during the Winter Solstice. Hence you can do all your calculations assuming December 22nd sunlight hours, i.e sunlight hours will be between 08:14 and 17:25.
    
In this amazing version of future Barcelona, one can safely assume:

- Buildings are distributed in neighbourhoods.
- In those neighbourhoods, the buildings are always aligned east to west.
- The sun rises in the east and travels at a constant radial speed until setting.
- The only shadows created in a neighbourhood are artefacts of the buildings in it.
- We consider an apartment receives sunlight when either its eastern or western exterior
wall is fully covered in sunlight and/or when the sun is directly overhead.
- There is only one apartment per floor; in a building with N floors they are numbered from 0 to N-1.

<b>API</b><br>
Your program should have two APIs defined:

- <b>init</b>​ method that takes a String containing a JSON describing the city, with this format:<br>
[{ neighborhood: < name-string >, apartments_height: < number >, buildings: [{name: < name-string >, apartments_count: < number >, distance: < number >}]}]

Assume the building list is ordered from east to west.


- <b>getSunlightHours</b>​ method which takes a neighbourhood name, building name, and
apartment number. It returns the sunlight hours as a string like “hh:mm:ss - hh:mm:ss” in 24hr format.

Assume i​nit ​is only going to be called once, however, getSunlightHours ​will be called very frequently.

Please provide a working solution, and justify any limitations. Don’t be afraid to go above and beyond!

## Proposed solution

#### Function tree
```
|--createCity.py
|--run_tests.py
|--main.py
           /functions
           |--apartmentExists.py
           |--getBuilding.py
           |--getNeighborhood.py
           |--computeAngleTrigonometry.py
           |--computeSunlightHours.py

```

#### Solution overview

<b><i>run_tests.py</b></i>:
The code in <i>run_tests.py</i> obtains a city object from <i>createCity.py</i>, converts it to <i>json</i> and runs <i>main.py</i> several times for testing purposes.

<b><i>main.py</b></i>:
The core solution.

- It lets you modify the default sunlight hours (if you want to use some hours other than the December 22nd 08:14 and 17:25)
- It has the two required API's. 
	- The <b><i>init​</b></i> method takes a JSON describing the city and coverts it back and stores it into a python global variable <i>city</i>. 
	- The <b><i>getSunlightHours​</b></i> method. This method computes the sunlight hours a given apartment will have when taking into account the shadow artifacts from other buildings. It is capable of obtaining this result by placing the indicated apartment and the other apartments in a 2D coordinate system, compute the greatest angle during sunrise/sunset at which there is a higher apartment blocking sunlight and finally using the default sunrise and sunset time as well as the shadow angles found to compute the resulting sunlight hours.

*For further details and a more in-depth explanation, see comments on the source code.






     