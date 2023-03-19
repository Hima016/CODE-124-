class Vehicle:
    def __init__(self,vehicle_id,vehicle_type,vehicle_cost):
        self.__vehicle_id=vehicle_id
        self.__vehicle_type=vehicle_type
        self.__vehicle_cost=vehicle_cost
        self.__premium_amount=None
    def calculate_premium(self):
        if self.__vehicle_type.lower()=="two wheeler":
            self._premimum_amount=0.02*self.__vehicle_cost
        elif self.__vehicle_type.lower()=="four wheeler":
            self.__premimum_amount=0.06*self.__vehicle_cost
        else:
            raise ValueError("Invalid vehicle type")

    def get_vehicle_id(self):
        return self.__vehicle_id
    def set_vehicle_id(self,vehicle_id):
        self.__vehicle_id=vehicle_id

    def get_vehicle_type(self):
        return self.__vehicle_type
    def set_vehicle_type(self,vehicle_type):
        self.__vehicle_type=vehicle_type

    def get_vehicle_cost(self):
        return self.__vehicle_cost   
    def set_vehicle_cost(self,vehicle_cost):
        self.__vehicle_cost=vehicle_cost

    def get_premium_amount(self):
        return self.__premimum_amount



vehicle1 = Vehicle("V001", "Two Wheeler", 50000)
vehicle2 = Vehicle("V002", "Four Wheeler", 100000)

# Set instance variables using setter methods
vehicle1.set_vehicle_id("V003")
vehicle1.set_vehicle_type("Four Wheeler")
vehicle1.set_vehicle_cost(75000)

# Calculate premium for all vehicles
vehicle1.calculate_premium()
vehicle2.calculate_premium()

# Display vehicle details
print("Vehicle ID:", vehicle1.get_vehicle_id())
print("Vehicle Type:", vehicle1.get_vehicle_type())
print("Vehicle Cost:", vehicle1.get_vehicle_cost())
print("Premium Amount:", vehicle1.get_premium_amount())
print()
print("Vehicle ID:", vehicle2.get_vehicle_id())
print("Vehicle Type:", vehicle2.get_vehicle_type())
print("Vehicle Cost:", vehicle2.get_vehicle_cost())
print("Premium Amount:", vehicle2.get_premium_amount())