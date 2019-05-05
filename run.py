from datetime import datetime, timedelta
from classes.routes import Route
from classes.seller import Seller
from classes.control import Control


def main():
    # Route dictionary: key = route color, val = num buses on route
    rdict = {'blue': 2, 'green': 4, 'red': 5}

    # Initialize date dict and get current date
    date_dict = {}
    now = datetime.today()

    date_dict = {}



	# Associate appropriate route info with each date for next 10 days
    for i in range(10):
        date = now + timedelta(days = i)
        date = date.strftime("%m/%d/%Y")
        date_dict[date] = {}
        for color, num in rdict.items():
            date_dict[date][color] = Route(color, num)

	# Initialize seller
    s = Seller(date_dict, 1.2, 0.9, 10)
    c = Control(s)
    c.control()

if __name__ == '__main__':
    main()