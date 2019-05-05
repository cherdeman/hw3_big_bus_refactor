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

ts = Seller(date_dict)

# test attributes
def test_available_dates():
	ts.routes_by_date == date_dict

def test_weekend_multiplier():
	ts.test_weekend_multiplier == 1.2


# test methods
def test_check_input_date():
	ts.check_input_date('05/04/2019') == True
