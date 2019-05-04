import pytest
from classes.routes import Route 

test_route = Route('blue', 5)

# Test route attributes
def test_route_color():
	test_route.color == 'blue' 

def test_number_busses():
	test_route.number_of_busses == 5
