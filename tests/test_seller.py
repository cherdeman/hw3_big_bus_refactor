import pytest
import unittest
from unittest.mock import patch
from datetime import datetime, timedelta

from classes.routes import Route 
from classes.seller import Seller

# Reference for overriding input function: https://stackoverflow.com/questions/18161330/using-unittest-mock-to-patch-input-in-python-3

#initialize test seller
now = datetime(2019, 5, 4, 18, 39, 53, 898306)
date_dict = {}

for i in range(10):
    date = now + timedelta(days = i)
    date = date.strftime("%m/%d/%Y")
    date_dict[date] = {}
    date_dict[date]['blue'] = Route('blue', 5)

ts = Seller(date_dict, 1.2, 0.9, 10)

def today(command):
    print("hey")
    ts.date = '05/05/2019'
    return True

# test attributes
def test_available_dates():
    assert ts.routes_by_date == date_dict

def test_weekend_multiplier():
    assert ts.weekend_multiplier == 1.2

def test_group_discount_rate():
    assert ts.group_discount_rate == 0.9

def test_base_ticket_price():
    assert ts.base_ticket_price == 10

# test methods
@patch('builtins.input', lambda _ : '05/10/2019')
def test_get_date():
    ts.get_date()
    assert ts.date == '05/10/2019'

@patch('builtins.input', lambda _ : 'asdgfhas')
def test_get_date_bad_formation():
    ts.reset()
    ts.get_date()
    assert ts.date is None

def test_check_input_date():
    ts.date = '05/04/2019'
    assert ts.check_input_date()

def test_get_price_weekend():
    ts.date = '05/04/2019'
    ts.get_price()
    assert ts.price == 12

def test_get_price_weekday():
    ts.date = '05/09/2019'
    ts.get_price()
    assert ts.price == 10

@patch('builtins.input', lambda _ : 'blue')
def test_get_route():
    ts.date = '05/10/2019'
    ts.get_route()
    assert ts.bus.color == 'blue'

@patch('builtins.input', lambda _ : '4')
def test_ticket_request():
    ts.ticket_request()
    assert ts.tickets_requested == 4

def test_check_ticket_limit_4():
    ts.tickets_requested = 4
    assert ts.check_ticket_limit()

def test_check_ticket_limit_5():
    ts.tickets_requested = 5
    assert not ts.check_ticket_limit()

def test_check_seat_availability():
    ts.date = '05/04/2019'
    ts.route = 'blue'
    ts.bus = ts.routes_by_date[ts.date][ts.route]
    assert ts.check_seat_availability()

def test_check_group_discount():
    ts.tickets_requested = 4
    ts.price = 10
    ts.check_group_discount() 
    assert ts.price == 9

@patch('builtins.input', lambda _ : 'y')
def test_confirm_ticket_sale():
    ts.date = '05/10/2019'
    ts.get_route()
    assert ts.confirm_order()

@patch('builtins.input', lambda _ : 'n')
def test_confirm_ticket_sale_reject():
    ts.date = '05/10/2019'
    ts.get_route()
    assert not ts.confirm_order()

@patch.object(Seller, 'check_today', new=today)
@patch('builtins.input', lambda _ : 'blue')
def test_print_report_today_correct():
    assert ts.print_report_today()

def test_print_report_today_incorrect():
    ts.date = '05/05/2019'
    assert not ts.print_report_today()

def test_report_future_date_none():
    ts.reset()
    assert not ts.print_report_other_day()

def test_report_future_date_correct():
    ts.date = '05/06/2019'
    assert ts.print_report_other_day()

@patch('builtins.input', lambda _ : '05/05/2019')
def test_report_future_date():
    assert ts.report()

@patch('builtins.input', lambda _ : '05/05/2019')
def test_report_future_date():
    assert ts.report()

def test_reset():
    ts.price = 1
    ts.route = 'blue'
    ts.tickets_requested = 5
    ts.date = '05/05/05'
    ts.bus = Route('blue', 5)
    ts.reset()

    assert ts.price is None
    assert ts.route is None
    assert ts.tickets_requested is None
    assert ts.date is None
    assert ts.bus is None


