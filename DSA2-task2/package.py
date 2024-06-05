# Nick Porter
# Student ID: 011452649


class Package:
    """Creates Package Object that takes id, address, city, state, zip, deadline, weight, status, deliveryTime, and departure Time as arguments"""
    # Created package class to create objects for each package
    def __init__(self, id, address,city, state, zip, deadline, weight, status):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.status = status
        # deliveryTime and departure Time will be updated later
        self.deliveryTime = None
        self.deparTime = None

    #method for updating status of package based on time comparison
    def status_update(self, time):
        if (time > self.deparTime) and (time < self.deliveryTime):
            self.status = "In route"
        elif (time > self.deliveryTime):
            self.status = f"Delivered, {self.deliveryTime}"
        else:
            self.status = "At the Hub"

    #Method for checking cotent of package testing purposes.
    def package_content(self):
        return(self.id, self.address, self.city, self.state, self.zip, self.deadline, self.weight, self.status)

