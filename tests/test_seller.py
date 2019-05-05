import pytest
import unittest
from unittest.mock import patch
from datetime import datetime, timedelta

from classes.routes import Route 
from classes.seller import Seller


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

@patch('builtins.input', lambda _ : 'asdgfhas')
def test_get_date_bad_formation():
    ts.get_date()
    ts.date is None

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
    ts.get_route()
    ts.bus.color == 'blue'

@patch('builtins.input', lambda _ : '4')
def test_ticket_request():
    ts.ticket_request()
    ts.tickets_requested == 4

def test_check_ticket_limit_4():
    ts.tickets_requested = 4
    ts.check_ticket_limit() == True

def test_check_ticket_limit_5():
    ts.tickets_requested = 5
    ts.check_ticket_limit() == False

def test_check_seat_availability():
    ts.date = '05/04/2019'
    ts.route = 'blue'
    ts.bus = ts.routes_by_date[ts.date][ts.route]
    ts.check_seat_availability() == False

def test_check_group_discount():
    ts.tickets_requested = 4
    ts.price = 10
    ts.check_group_discount() == 9

@patch('builtins.input', lambda _ : 'y')
def test_confirm_ticket_sale():
    ts.date = '05/10/2019'
    ts.get_route()
    ts.confirm_order() == True

@patch('builtins.input', lambda _ : 'blue')
def test_report_today_correct():
    ts.date == '05/04/2019'
    ts.print_report_today() == True

def test_report_future_date_none():
    ts.date == None
    ts.print_report_other_day() == False

def test_report_future_date_correct():
    ts.date == '05/06/2019'
    ts.print_report_other_day() == True

@patch('builtins.input', lambda _ : '05/05/2019')
def test_report_future_date():
    ts.report() == True

@patch('builtins.input', lambda _ : '05/05/2019')
def test_report_future_date():
    ts.report() == True


