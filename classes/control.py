# Module for the controller class

class Control():
    """Class to provide CLI for interaction with the system"""
    def __init__(self, seller):
        self.seller = seller
        self.options = {1: ("Sell tickets", lambda: self.seller.sell_ticket()),
                        2: ("Provide a refund", lambda: self.seller.refund_ticket()),
                        3: ("Generate a report", lambda: self.seller.report()),
                        4: ("Exit", lambda: self.set_active())}
        self.active = True

    def control(self):
        """Method to provide control functionality"""
        while self.active:
            print()
            print("What would you like to do?")
            for i in range(1, len(self.options) + 1):
                option_name = self.options[i][0]
                print(f"{i}) {option_name}")

            option = self.get_option()

            if option in self.options.keys():
                action_tuple = self.options[option]
                action_tuple[1]()
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
        if self.active:
            self.active = False

