from datetime import datetime, timedelta
from routes import Route, Seller
from control import Control


rdict = {'blue': 2, 'green': 4, 'red': 5}
ddict = {}
now = datetime.today()

for i in range(10):
    d = now+timedelta(days = i)
    d = d.strftime("%B/%d/%Y")
    ddict[d] = {}
    for color, num in rdict.items():
        ddict[d][color] = Route(color, num)

s = Seller(ddict)

def main():
	c = Control(s)
	c.control()

if __name__ == '__main__':
	main()