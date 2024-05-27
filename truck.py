# Nick Porter
# Student ID: 011452649


class DeliveryTruck:
    def __init__(self, miles, packages, currentLocation, initalTime):
        """Create Delivery Truck object with inital miles, package list, current location, and initalTime(Time of Departure)"""
        self.miles = miles
        self.packages = packages
        self.currentLocation = currentLocation
        self.initalTime = initalTime
        self.currentTime = initalTime

    def status(self):
        return (f"Current Miles: {self.miles}\n"
        f"Current Packages Aboard: {self.packages}\n"
        f"Current Address: {self.currentLocation}\n"
        f"Current Time: {self.currentTime}")
   