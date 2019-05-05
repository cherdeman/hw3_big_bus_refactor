import pytest
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
def test_check_input_date():
    ts.check_input_date('05/04/2019') == True

def test_get_price_weekend():
    ts.get_price('05/04/2019') == 12

def test_get_price_weekday():
    ts.get_price('05/09/2019') == 10

def test_get_route():
    ts.get_route('05/04/2019', 'blue').color == 'blue'

def test_check_ticket_limit_4():
    ts.check_ticket_limit(4) == True

def test_check_ticket_limit_5():
    ts.check_ticket_limit(5) == False

def test_check_seat_availability():
    bus = ts.get_route('05/04/2019', 'blue')
    ts.check_seat_availability(bus, 500) == False

def test_check_group_discount():
    ts.check_group_discount(4) == True
