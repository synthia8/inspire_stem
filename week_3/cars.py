# this is a class that describes cars

class car:
    def __init__(self,model,make,year_of_production,fuel_capacity,colour):
        self.model = model
        self.make = make
        self.year_of_production = year_of_production
        self.fuel_capacity = fuel_capacity
        self.colour = colour

    def print_make(self,make):
        print("the car is of{0} make".format(self.make))

    def set_make(self,make):
        self.make = make

    def get_make(self):
        return self.make
    

    
friends_car = car("impala","chrevolet","1969","2500cc","lilac")

friends_car.print_make("impala")

friends_car.set_make("ford")
print(friends_car.get_make)

friends_car.set_colour("pink")
print(friends_car.get_colour)