class Engine:
    def __init__(self,horsepower):
        self.horsepower=horsepower
    def get_engine_info(self):
        return f"{self.horsepower} HP Engine"
        
class Vehicle:
    total_vehicles=0
    # status="available"
    def __init__(self,brand,model,engine):
        self.brand=brand
        self.model=model
        self.engine=engine
        Vehicle.total_vehicles=Vehicle.total_vehicles+1
        self._rental_price=0
        self.status="available"
        
    def get_details(self):
        return f"{self.brand} | {self.model} | {self.engine.horsepower}"
        
    @staticmethod
    def get_vehicle_type():
        return "Generic Vehicle"
    
    @classmethod
    def get_total_vehicles(cls):
        return cls.total_vehicles
        
    @property
    def rental_price(self):
        return self._rental_price
    
    @rental_price.setter
    def rental_price(self,value):
        if value>=0:
            self._rental_price=value
        else:
            raise ValueError("price value cannot be negative")
            
class Car(Vehicle):
    def __init__(self,brand,model,engine,seats):
        super().__init__(brand,model,engine)
        self.seats=seats
    def get_details(self):
        base_details= super().get_details()
        return f"{base_details} | Seats: {self.seats}"

class Bike(Vehicle):
    def __init__(self, brand, model, engine,wheels,type_):
        super().__init__(brand, model, engine)
        self.wheels=wheels
        self.type_=type_

class Rental_Agency:
    def __init__(self,):
        self.list_vehicles=[]

    def rent_vehicle(self,vehicle):
        if vehicle.status == "available":
            vehicle.status="rented"
        else:
            print(f"{vehicle} is not available")

    def return_vehicle(self,vehicle):
        vehicle.status="available"

    def avaiable_vehicle(self):
        for i in self.list_vehicles:
            if i.status=="available":
                print(i.get_details())

    def add_vehicle(self, vehicle):
        self.list_vehicles.append(vehicle)
        print(f"{vehicle.brand} added to fleet") 

engine1 = Engine(120)
engine2 = Engine(80)

car1 = Car("Honda", "City", engine1, 5)
bike1 = Bike("Yamaha", "R15", engine2, 2, "Sport")

agency = Rental_Agency()
agency.add_vehicle(car1)
agency.add_vehicle(bike1)

agency.avaiable_vehicle()   
                            

agency.rent_vehicle(car1)
agency.avaiable_vehicle()

agency.return_vehicle(car1)
agency.avaiable_vehicle()   