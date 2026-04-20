class Vehicle:
    spots=10
    def __init__(self,number):
        self.number = number
        
class Car(Vehicle):
    rate=20

class Bike(Vehicle):
    rate=10

class ParkingLot:
    def __init__(self):
        self.parking_spots=[]

    def park_vehicle(self, vehicle):
        if len(self.parking_spots) < Vehicle.spots:
            if vehicle.number in self.parking_spots:
                print("Vehicle already parked.")
            else:
                self.parking_spots.append(vehicle.number)
                print(f"Vehicle {vehicle.number} parked successfully.")
                print(f"Total parked: {len(self.parking_spots)}, Available spots: {Vehicle.spots - len(self.parking_spots)}")
        else:
            print("Parking is full.")
    
    def unpark_vehicle(self, vehicle, time):
        if vehicle.number in self.parking_spots:
            self.parking_spots.remove(vehicle.number)
            print(f"Vehicle {vehicle.number} unparked successfully.")
            print(f"The total fare of parking is: {vehicle.rate * time}")
            print(f"Total parked: {len(self.parking_spots)}, Available spots: {Vehicle.spots - len(self.parking_spots)}")   
        else:
            print("Vehicle not found in parking lot.")

parking_lot = ParkingLot()
car1= Car("KA-01-1234")
car2= Car("KA-01-5678")
bike1= Bike("KA-01-4321")
parking_lot.park_vehicle(car1)
parking_lot.park_vehicle(car2)
parking_lot.park_vehicle(bike1)
parking_lot.unpark_vehicle(car1,2)


