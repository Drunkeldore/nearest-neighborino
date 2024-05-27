class DeliveryTruck:
    def __init__(self, miles, packages, currentLocation, initalTime, currentTime):
        self.miles = miles
        self.packages = packages
        self.currentLocation = currentLocation
        self.initalTime = initalTime
        self.currentTime = initalTime

    def status(self):
        print(f"Current Miles: {miles}")
        print(f"Current Packages Aboard: {packages}")
        print(f"Current Address: {currentLocation}")
        print(f"Current Time: {CurrentTime}")