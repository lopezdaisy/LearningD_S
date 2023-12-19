class vehicle:
    def general_usage(self):
        print("General use: Transportation")

class car(vehicle):
    def __init__(self) -> None:
        super().__init__()
        print("I am a car") 
        self.wheels = 4
        self.has_root = True

    def specific_usage(self):
        print("Specific use: Commute to work \n vacation with family") 

class Motocycle(vehicle):
    def __init__(self) -> None:
        super().__init__()
        print('I am a Motocycle')
        self.wheels = 2
        self.has_roof = False

    def specific_use(self):
        print("Specific use: road trip \n racing")

# Instantiate objects
car_object = car()
motorcycle_object = Motocycle()

# Accessing methods
car_object.general_usage()
car_object.specific_usage()

motorcycle_object.general_usage()
motorcycle_object.specific_use()        
        


