import pytest
from classes.control import Control 
from classes.seller import Seller 
from classes.routes import Route

from datetime import datetime, timedelta

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

# test attributes
def test_seller():
	tc.seller == ts