#Tom Banis
#cars
#Get and print information about a car using classes


class Vehicle():
    def __init__(self, type):
        self.type = type

class Automobile(Vehicle):
    def __init__(self, type, year, make, model, doors, roof):
        super().__init__(type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

vtype = input("Enter the type of the vehicle: ")
vyear = input("Enter the year of the vehicle: ")
vmake = input("Enter the make of the vehicle: ")
vmodel = input("Enter the model of the vehicle: ")
vdoors = input("Enter the number of doors on the vehicle (2 or 4): ")
vroof = input("Enter the type of roof (solid or sun): ")

vehicle = Automobile(vtype, vyear, vmake, vmodel, vdoors, vroof)

print("Vehicle type: {}".format(vehicle.type))
print("Year: {}".format(vehicle.year))
print("Make: {}".format(vehicle.make))
print("Model: {}".format(vehicle.model))
print("Number of doors: {}".format(vehicle.doors))
print("Type of roof: {}".format(vehicle.roof))
