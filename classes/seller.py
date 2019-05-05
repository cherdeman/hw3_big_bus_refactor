# This module defines the seller class

from uuid import uuid4
from datetime import datetime, timedelta
from classes.routes import Route

class Seller():
    """Class representing the ticket seller"""
    def __init__(self, date_route_dict, weekend_multiplier, group_discount_rate, base_price): 
        self.routes_by_date = date_route_dict
        self.weekend_multiplier = weekend_multiplier
        self.group_discount_rate = group_discount_rate
        self.base_ticket_price = base_price
        self.price = None
        self.route = None
        self.tickets_requested = None
        self.date = None

    # Ticket selling method and helpers
    def sell_ticket(self):
        """Sell tickets for a given date and route"""
        # Get date input
        self.get_date()
        # Check date validity
        if not self.check_input_date():
            return

        # vary price based on weekday/weekend
        self.price = self.get_price()

        # choose route
        bus = self.get_route()
        if bus is None:
            return

        tickets_requested = input("How many tickets would you like to buy? ")
        tickets_requested = int(tickets_requested)
        if not self.check_seat_availability(bus, tickets_requested):
            return

        if not self.check_ticket_limit(tickets_requested):
            return

        price = self.check_group_discount(price, tickets_requested)

        confirmation = input(f"Would you like to purchase {tickets_requested} ticket(s) for route {route} on {date} for ${price:,.2f}? (y/n) ")
        
        self.confirm_order(confirmation, route, price, tickets_requested)

    def get_date(self):
        self.date = input("Enter the date for which you'd like to buy ticket(s) in the form mm/dd/yyyy (e.g. 05/10/2019): ")

    def check_input_date(self):
        valid_date = False
        if self.date in self.routes_by_date.keys():
            valid_date = True
        else:
            print(f"{self.date} is not an available date")

        return valid_date

    def get_price(self):
        if datetime.strptime(self.date, "%m/%d/%Y").weekday() < 5:
            price = self.base_ticket_price
        else: 
            price = self.base_ticket_price * self.weekend_multiplier        
        
        return price

    def get_route(self):
        bus = None
        color = input("Enter the route (blue, green, or red): ")
        self.route = color
        if self.route in self.routes_by_date[self.date].keys():
            bus = self.routes_by_date[self.date][self.route]
        else:
            print(f"{route} is not a valid route".format())

        return bus

    def check_seat_availability(self, bus, tickets_requested):
        available_tickets = False
        if tickets_requested <= bus.get_number_of_available_tickets():
            available_tickets = True
        else:
            print(f"There are fewer than {tickets_requested} tickets available for route {bus.color}".format())

        return available_tickets

    def check_ticket_limit(self, tickets_requested):
        under_ticket_limit = False
        if tickets_requested < 5:
            under_ticket_limit = True
        else:
            print("The maximum number of tickets you can purchase is 4.")

        return under_ticket_limit

    def check_group_discount(self, price, tickets_requested):
        if tickets_requested == 4:
            price *= self.group_discount_rate
            print(f"You qualify for a group discount rate, your price per ticket is ${price}")

        return price

    def confirm_order(self, confirmation, route, price, tickets_requested):
        confirmed = True
        if confirmation == "y":
            for ticket_number in range(tickets_requested):
                ticket_id = str(uuid4())
                ticket = (ticket_id, route, date, price)
                bus.sell_ticket(ticket)
                print(f"You purchased ticket {ticket[0]} for route {ticket[1]} on {ticket[2]} for ${ticket[3]:,.2f}".format())
        else:
            confirmed = False
            print("Ok, NVM")

        return confirmed   

    # Refund method and helpers
    def refund(self): 
        """Refund a ticket"""
        date = input("Enter the date for which you'd like to be refunded in the form Month/day/Year (e.g. April/23/2019): ")
        if date == datetime.now().strftime("%B/%d/%Y"):
            print("No refunds for tickets for today.")
            return
        if date not in self.avail.keys():
            print("Not a valid date for a refund.")
            return
        
        route = input("Enter the route (blue, green, or red): ")
        if route not in ["blue", "red", "green"]:
            print("Not a valid route")
            return
        
        _id = input("Enter the ticket id: ")
        if _id not in self.avail[date][route].tix:
            print(f"There is no ticket sold with id {_id} on route {route} and {date}".format())
            return

        x = input(f"Are you sure you want a refund for ticket {_id} on route {route} on date {date}? (y/n) ".format())
        if x == "y":
            bus = self.avail[date][route]
            bus.refund(_id)
            print("Your ticket has been refunded")

    def report(self):
        """Print a report for any valid date"""
        date = input("Enter the date for which you'd like a report in the form Month/day/Year (e.g. April/23/2019): ")
        if date == datetime.now().strftime("%B/%d/%Y"):
            print("You'd like a report for today. Route information is also required.")
            route = input("Enter the route you want a report on (blue, green, or red): ")
            if route not in ["blue", "red", "green"]:
                print("Not a valid route")
                return
            else:
                print(f"{len(self.avail[date][route].tix)} tickets have been sold on route {route} for today.".format())
                return

        if date not in self.avail.keys():
            print("A report cannot be generated for {}".format(date))
            return

        print(f"Report for date {date}".format())
        for route, obj in self.avail[date].items():
            n = len(self.avail[date][route].tix)
            print(f"{n} tickets of {self.avail[date][route].tseats} have been sold on the {route} route".format())
