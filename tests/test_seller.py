import pytest
from datetime import datetime, timedelta
from classes.routes import Route 
from classes.seller import Seller
import unittest
from unittest.mock import patch


#initialize test seller
now = datetime(2019, 5, 4, 18, 39, 53, 898306)
date_dict = {}

for i in range(10):
    date = now + timedelta(days = i)
    date = date.strftime("%m/%d/%Y")
    date_dict[date] = {}
    date_dict[date]['blue'] = Route('blue', 5)

ts = Seller(date_dict, 1.2, 0.9, 10)

# test attributes
def test_available_dates():
    ts.routes_by_date == date_dict

def test_weekend_multiplier():
    ts.weekend_multiplier == 1.2

def test_group_discount_rate():
    ts.group_discount_rate == 0.9

def test_base_ticket_price():
    ts.base_ticket_price == 10

# test methods
@patch('builtins.input', lambda _ : '05/10/2019')
def test_get_date():
    ts.get_date()
    ts.date == '05/10/2019'

def test_check_input_date():
    ts.date = '05/04/2019'
    ts.check_input_date() == True

def test_get_price_weekend():
    ts.date = '05/04/2019'
    ts.get_price() == 12

def test_get_price_weekday():
    ts.date = '05/09/2019'
    ts.get_price() == 10

@patch('builtins.input', lambda _ : 'blue')
def test_get_route():
    ts.date = '05/10/2019'
    bus = ts.get_route()
    bus.color == 'blue'

@patch('builtins.input', lambda _ : '4')
def test_tickets_requested():
    ts.tickets_requested()
    ts.tickets_requested == 4

def test_check_ticket_limit_4():
    ts.check_ticket_limit(4) == True

def test_check_ticket_limit_5():
    ts.check_ticket_limit(5) == False

def test_check_seat_availability():
    ts.date = '05/04/2019'
    ts.route = 'blue'
    bus = ts.routes_by_date[ts.date][ts.route]
    ts.check_seat_availability(bus, 500) == False

def test_check_group_discount():
    ts.check_group_discount(10, 4) == 9

def test_confirm_ticket_sale():
    pass
