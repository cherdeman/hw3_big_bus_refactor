import pytest
from classes.routes import Route 

test_route = Route('blue', 5)

# Test route attributes
def test_route_color():
	test_route.route_color == 'blue' 
