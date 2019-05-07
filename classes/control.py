# Module for the controller class

class Control():
    """Class to provide CLI for interaction with the system"""
    def __init__(self, seller):
        self.seller = seller
        self.options = {1: "Sell tickets",
                        2: "Provide a refund",
                        3: "Generate a report",
                        4: "Exit"}
        self.active = True

    def control(self):
        """Method to provide control functionality"""
        while self.active:
            print()
            print("What would you like to do?")
            for i in range(1, len(self.options) + 1):
                print(f"{i}) {self.options[i]}".format())

            option = input("Please enter the number of the option you'd like to select: ")
            print()
            if option.isdigit():
                option = int(option)
            if option == 1:
                self.seller.sell_ticket()
            elif option == 2:
                self.seller.refund()
            elif option == 3:
                self.seller.report()
            elif option == 4:
                print("Bye")
                self.active = False
            else: 
                print("That is not valid input.")

    def get_option(self):
        option = input("Please enter the number of the option you'd like to select: ")
        try:
            option = int(option)
        except Error as e:
            print(e)

