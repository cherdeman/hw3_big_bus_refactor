import pytest
import unittest
from unittest.mock import patch
import unittest.mock
from datetime import datetime, timedelta

from classes.control import Control 
from classes.seller import Seller 
from classes.routes import Route



#initialize test control
now = datetime(2019, 5, 4, 18, 39, 53, 898306)
date_dict = {}

for i in range(10):
    date = now + timedelta(days = i)
    date = date.strftime("%m/%d/%Y")
    date_dict[date] = {}
    date_dict[date]['blue'] = Route('blue', 5)

ts = Seller(date_dict, 1.2, 0.9, 10)

tc = Control(ts)

# helper function
def option_tester(command):
    print("hey")
    tc.active = False

# test attributes
def test_seller():
    tc.seller == ts

def test_options():
    tc.options == {1: "Sell tickets",
                   2: "Provide a refund",
                   3: "Generate a report",
                   4: "Exit"}

def test_active():
    tc.active

# test methods
@patch('builtins.input', lambda _ : '1')
def test_get_option_correct():
    tc.get_option() == 1

@patch('builtins.input', lambda _ : '0')
def test_get_option_incorrect1():
    tc.get_option() is None

@patch('builtins.input', lambda _ : 'asdf')
def test_get_option_incorrect2():
    tc.get_option() is None

def test_set_active():
    tc.active = True
    tc.set_active()
    not tc.active

@patch('builtins.input', lambda _ : '4')
def test_control_exit():
    tc.control()
    not tc.active

@patch('builtins.input', lambda _ : '1')
@patch.object(Seller, 'sell_ticket', new=option_tester)
def test_control_1():
    tc.active = True
    tc.control()
    not tc.active

@patch('builtins.input', lambda _ : '2')
@patch.object(Seller, 'refund', new=option_tester)
def test_control_2():
    tc.active = True
    tc.control()
    not tc.active

@patch('builtins.input', lambda _ : '3')
@patch.object(Seller, 'report', new=option_tester)
def test_control_2():
    tc.active = True
    tc.control()
    not tc.active




