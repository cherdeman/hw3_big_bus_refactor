# Module for the controller class

class Control():
    """Class to provide CLI for interaction with the system"""
    def __init__(self, seller):
        self.seller = seller
        self.options = {1: ("Sell tickets", lambda: self.seller.sell_ticket()),
                        2: ("Provide a refund", lambda: self.seller.refund()),
                        3: ("Generate a report", lambda: self.seller.report()),
                        4: ("Exit", lambda: self.set_active())}
        self.active = True

    def control(self):
        """Method to provide control functionality"""
        while self.active:
            print()
            print("What would you like to do?")
            for i in range(1, len(self.options) + 1):
                print(f"{i}) {self.options[i][0]}")

            option = self.get_option()

            if option in self.options.keys():
                action_tuple = self.options[option]
                action_tuple[1]()
            # if option == 1:
            #     self.seller.sell_ticket()
            # elif option == 2:
            #     self.seller.refund()
            # elif option == 3:
            #     self.seller.report()
            # elif option == 4:
            #     print("Bye")
            #     self.active = False
            else: 
                print("That is not valid input.")

    def get_option(self):
        option = input("Please enter the number of the option you'd like to select: ")
        try:
            option = int(option)
        except ValueError:
            option = None

        return option

    def set_active(self):
        if self.active is True:
            self.active = False
        else:
            self.active = True

