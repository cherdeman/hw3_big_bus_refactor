# Big Bus Application

This repository is code for 3nd homework assignment for the course Applied Software Engineering (Spring 2019). This builds on homework assignment 2 (details [here](https://github.com/mpcs51220/hw2/blob/master/big_bus.md) and [here](https://github.com/mpcs51220/hw2/blob/master/requirements.md)) by refactoring the existing code and adding tests through a TDD process. See details [here](https://github.com/mpcs51220/hw3).

## Repo Organization
The repo is now organized into `classes` and `tests` subdirectories, while the `run.py` script is located in the repository root.

* `run.py` - Initalizes the classes and runs the control method for terminal interaction.
* `requirements.txt` - Lists package dependencies, in this case only `pytest`.

#### classes
Each class is now located in its own module:

* `routes.py` - Code for the Route class. The Route classes represent a blue, green, or red bus route on a given date. 
* `seller.py` - Code for the Seller class. The Seller represents the ticket selling entity.
* `control.py` - Code for the Control class, which implements the command line interface for dynamic interaction with the Seller class.

#### tests
Each class module has its own set of tests:

* `test_routes.py` - Test suite for the Route class.
* `test_seller.py` - Test suite for the Seller class.
* `test_control.py` - Test suite for the Control class.

## Running the Code
This repository was developed in Python 3.6. The only package dependency is the `pytest` testing framework. This can be installed from the requirements document by running `pip -r install requirements.txt` or simply `pip install pytest`.

To run the program, run the command `python run.py` inside the root of the directory. No additional setup is needed. 

Note that there is no database backend built in to this program, so ticket sale information does not persist between runs of the program.
