# Big Bus Application

This repository is code for 2nd homework assignment for the course Applied Software Engineering (Spring 2019). The prompt and requirements can be found [here](https://github.com/mpcs51220/hw2/blob/master/big_bus.md) and additional assignment details can be found [here](https://github.com/mpcs51220/hw2/blob/master/requirements.md).

## Repo Organization
There are three files in this repository:

* routes.py - Code for the Route and Seller classes. The Route classes represent a blue, green, or red bus route on a given date, the Seller represents the ticket selling entity.
* control.py - Code for the Control class, which implements the command line interface for dynamic interaction with the Seller class.
* run.py - Initalizes the classes and runs the control method for terminal interaction.

## Running the Code
To run the code, clone this repo and run the command `python run.py` inside the root of the directory. No additional setup is needed. 

Note that there is no database backend built in to this program, so ticket sale information does not persist between runs of the program.
