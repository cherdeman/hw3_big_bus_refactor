import pytest
from classes.routes import Route 

tr = Route('blue', 5)

# Test route attributes
def test_route_color():
    tr.color == 'blue' 

def test_number_busses():
    tr.number_of_busses == 5

def test_seats_per_bus():
    tr.seats_per_bus == 89

def test_total_seats():
    tr.total_seats == 5*89

def test_tickets_sold():
    tr.tickets_sold == {}

# test route methods 
def test_sell_ticket():
    ticket = ('12345', 'blue', 'May 5, 2018', 2)
    tr.sell_ticket(ticket)
    tr.tickets_sold['12345'] == ticket

def test_refund_ticket():
    ticket_id = '12345'
    tr.refund_ticket('12345')
    tr.tickets_solid == {}
