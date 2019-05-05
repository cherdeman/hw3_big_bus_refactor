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
        self.bus = None

    # Ticket selling method and helpers
    def sell_ticket(self):
        """Sell tickets for a given date and route"""
        # Get date input
        self.get_date()
        # Check date validity
        if not self.check_input_date():
            self.reset()
            return

        # vary price based on weekday/weekend
        self.get_price()

        # choose route
        self.get_route()
        if self.bus is None:
            self.reset()
            return

        self.ticket_request()
        if not self.check_seat_availability():
            self.reset()
            return

        if not self.check_ticket_limit():
            self.reset()
            return

        self.check_group_discount()
        self.confirm_order()
        self.reset()

    def get_date(self):
        date = input("Enter the date in the form mm/dd/yyyy (e.g. 05/10/2019): ")
        try:
            datetime.strptime(date, "%m/%d/%Y")
            self.date = date
        except ValueError:
            print("Incorrect data format, should be mm/dd/yyyy")
            return

    def check_input_date(self):
        valid_date = False
        if self.date in self.routes_by_date.keys():
            valid_date = True
        else:
            print(f"{self.date} is not an available date")

        return valid_date

    def get_price(self):
        if datetime.strptime(self.date, "%m/%d/%Y").weekday() < 5:
            self.price = self.base_ticket_price
        else: 
            self.price = self.base_ticket_price * self.weekend_multiplier        

    def get_route(self):
        color = input("Enter the route (blue, green, or red): ")
        self.route = color
        if self.route in self.routes_by_date[self.date].keys():
            self.bus = self.routes_by_date[self.date][self.route]
        else:
            print(f"{self.route} is not a valid route")

        #return bus

    def ticket_request(self):
        num_tickets = input("How many tickets would you like to buy? ")
        self.tickets_requested = int(num_tickets)

    def check_seat_availability(self):
        available_tickets = False
        if self.tickets_requested <= self.bus.get_number_of_available_tickets():
            available_tickets = True
        else:
            print(f"There are fewer than {self.tickets_requested} tickets available for route {bus.color}")

        return available_tickets

    def check_ticket_limit(self):
        under_ticket_limit = False
        if self.tickets_requested < 5:
            under_ticket_limit = True
        else:
            print("The maximum number of tickets you can purchase is 4.")

        return under_ticket_limit

    def check_group_discount(self):
        if self.tickets_requested == 4:
            self.price *= self.group_discount_rate
            print(f"You qualify for a group discount rate, your price per ticket is ${self.price}")

    def confirm_order(self):
        confirmed = True
        confirmation = input(f"Would you like to purchase {self.tickets_requested} ticket(s) for route {self.route} on {self.date} for ${self.price*self.tickets_requested:,.2f} total? (y/n) ")
        if confirmation == "y":
            for ticket_number in range(self.tickets_requested):
                ticket_id = str(uuid4())
                ticket = (ticket_id, self.route, self.date, self.price)
                self.bus.sell_ticket(ticket)
                print(f"You purchased ticket {ticket[0]} for route {ticket[1]} on {ticket[2]} for ${ticket[3]:,.2f}".format())
        else:
            confirmed = False
            print("Ok, NVM")

        return confirmed 

    def reset(self):
        self.price = None
        self.route = None
        self.tickets_requested = None
        self.date = None
        self.bus = None 

    # Refund method and helpers
    def refund(self): 
        """Refund a ticket"""
        self.get_date()

        if date == datetime.now().strftime("%m/%d/%Y"):
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

        x = input(f"Are you sure you want a refund for ticket {_id} on route {route} on date {date}? (y/n) ")
        if x == "y":
            bus = self.avail[date][route]
            bus.refund(_id)
            print("Your ticket has been refunded")

    def report(self):
        """Print a report for any valid date"""
        reported = False
        self.get_date()
        if not self.check_input_date():
            print("Cannot generate report.")
            self.reset()
            return reported

        reported = self.print_report_today()
        if not reported:
            reported = self.print_report_other_day()

        self.reset()
        return reported       

    def print_report_today(self):
        reported = False
        if self.date == datetime.now().strftime("%m/%d/%Y"):
            self.get_route()
            if self.bus is not None:
                print(f"{len(self.bus.tickets_sold)} tickets have been sold on route {self.route} for today.")
                reported = True

        return reported

    def print_report_other_day(self):
        reported = False
        print(f"Report for date {self.date}")
        for route in self.routes_by_date[self.date].keys():
            try:
                num_tickets_sold = len(self.routes_by_date[self.date][route].tickets_sold)
                print(f"{num_tickets_sold} tickets of {self.routes_by_date[self.date][route].total_seats} have been sold on the {route} route")
                reported = True
            except KeyError:
                print("Invalid request.")
                reported = False

        return reported

