import pytest
from classes.routes import Route 

tr = Route('blue', 5)

# Test route attributes
def test_route_color():
    assert tr.color == 'blue' 

def test_number_busses():
    assert tr.number_of_busses == 5

def test_seats_per_bus():
    assert tr.seats_per_bus == 89

def test_total_seats():
    assert tr.total_seats == 5*89

def test_tickets_sold():
    assert tr.tickets_sold == {}

# test route methods 
def test_sell_ticket():
    ticket = ('12345', 'blue', 'May 5, 2018', 2)
    tr.sell_ticket(ticket)
    assert tr.tickets_sold['12345'] == ticket

def test_refund_ticket():
    ticket_id = '12345'
    tr.refund_ticket('12345')
    assert tr.tickets_sold == {}

def test_get_total_route_seats():
    assert tr.get_total_route_seats() == 5*89

def test_get_number_of_available_tickets():
    ticket = ('12345', 'blue', 'May 5, 2018', 2)
    tr.sell_ticket(ticket)
    assert tr.get_number_of_available_tickets() == 444
