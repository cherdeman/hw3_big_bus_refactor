# This module defines the route class

from uuid import uuid4
from datetime import datetime, timedelta

class Route():
    # Class representing bus routes
    def __init__(self, color, bnum):
        self.color = color
        self.bnum = bnum
        self.seats = 89
        self.tseats = self.seats * self.bnum
        self.tix = {}

    def sell(self, ticket):
        # add ticket to ticket list
        self.tix[str(ticket[0])] = ticket

    def refund(self, tid):
        # remove ticket from ticket list
        del(self.tix[tid])

class Seller():
    """Class representing the ticket seller"""
    def __init__(self, rdict): 
        self.avail = rdict
        self.price = 2

    def sell(self):
        """Sell tickets for a given date and route"""
        # Get date input
        date = input("Enter the date for which you'd like to buy ticket(s) in the form Month/day/Year (e.g. April/23/2019): ")
        # Check date validity
        if date in self.avail.keys():
            # vary price based on weekday/weekend
            if datetime.strptime(date, "%B/%d/%Y").weekday() < 5:
                p = self.price
            else:
                p = self.price * 1.2

            # choose route
            route = input("Enter the route (blue, green, or red): ")
            if route in self.avail[date].keys():
                bus = self.avail[date][route]
                # Check for ticket availability
                n = input("How many tickets would you like to buy? ")
                n = int(n)
                if bus.tseats - len(bus.tix) > n:
                    # Check ticket num limit
                    if n > 4:
                        print("The maximum number of tickets you can purchase is 4.")
                        return
                    else:
                        p = p * n
                        # 10% discount for purchasing 4
                        if n == 4:
                            p = p*0.9
                    x = input(f"Would you like to purchase {n} ticket(s) for route {route} on {date} for ${p:,.2f}? (y/n) ")
                    # If confirmed, generate tickets
                    if x == "y":
                        for i in range(n):
                            t = (uuid4(), route, date, p/n)
                            bus.sell(t)
                            print(f"You purchased ticket {t[0]} for route {t[1]} on {t[2]} for ${t[3]:,.2f}".format())
                    else:
                        print("Ok, NVM")
                        return
                else:
                    print(f"There are fewer than {n} tickets available for route {route} on {date}".format())
                    return
            else:
                print(f"{route} is not a valid route".format())
                return
        else:
            print(f"{date} is not an available date".format())
            return


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



