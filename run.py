from datetime import datetime, timedelta
from routes import Route, Seller
from control import Control

# Route dictionary: key = route color, val = num buses on route
rdict = {'blue': 2, 'green': 4, 'red': 5}

# Initialize date dict and get current date
ddict = {}
now = datetime.today()

# Associate appropriate route info with each date for next 10 days
for i in range(10):
    d = now+timedelta(days = i)
    d = d.strftime("%B/%d/%Y")
    ddict[d] = {}
    for color, num in rdict.items():
        ddict[d][color] = Route(color, num)

# Initialize seller
s = Seller(ddict)

def main():
	c = Control(s)
	c.control()

if __name__ == '__main__':
	main()