# This module defines the route class

class Route():
    # Class representing a bus route on a single day
    def __init__(self, route_color, number_of_busses):
        self.color = route_color
        self.number_of_busses = number_of_busses
        self.seats_per_bus = 89
        self.total_seats = self.get_total_route_seats()
        self.tickets_sold = {}

    def get_total_route_seats(self):
        return self.seats_per_bus * self.number_of_busses

    def sell_ticket(self, ticket):
        # add ticket to ticket list
        ticket_id = str(ticket[0])
        self.tickets_sold[ticket_id] = ticket

    def refund_ticket(self, ticket_id):
        # remove ticket from ticket list
        del(self.tickets_sold[ticket_id])


