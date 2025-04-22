from abc import ABC, abstractmethod
class Car(ABC):
    def __init__(self, model, brand, engine_number):
        self.model = model
        self.brand = brand
        self.__engine_number = engine_number
        
    @abstractmethod
    def start(self):
        pass
        
    
    def get_engine_number(self): 
        return self.__engine_number
    
    
class ElectricCar(Car):
    def __init__(self, model, brand, engine_number, battery_capacity):
        super().__init__(model, brand, engine_number)
        self.battery_capacity = battery_capacity
        
    def show_capacity(self):
        print(f"Battery capacity: {self.battery_capacity} kWh")
        
    def start(self):
        print("Starting with Electric Engine")
        
        
class PetrolCar(Car):
    def start(self):
        print("Starting with Pertrol Engine")
        
        
class HybridCar(Car):
    def start(self):
        print("Starting with Hybrid Engine")
        
    
def car_start(car_obj):
    car_obj.start()
        
    
        
petrol_car = PetrolCar("Model X", "Tesla", "12345ABC")  
electric_car = ElectricCar("Model Y", "Tesla", "54321XYZ", 100)  
hybrid_car = HybridCar("Model Z", "Tesla", "98765LMN")


car_start(petrol_car)
car_start(electric_car)
car_start(hybrid_car)
        
        
e_car = ElectricCar("Model 3", "Tesla", "67890XYZ", 75)
print(e_car.model, e_car.brand, e_car.battery_capacity)
print(e_car.get_engine_number())
e_car.show_capacity() 


print(e_car.model, e_car.brand, e_car.battery_capacity)
        
# my_car = Car("Model S", "Tesla", "12345ABC")
c1 = PetrolCar("Model S", "Tesla", "12345ABC")
c2 = ElectricCar("Model 3", "Tesla", "67890XYZ", 75)

print(f"Car Model: {c1.model}, brand: {c1.brand}")
print(c1.model)
print(c2.brand)

print(c1.get_engine_number())

c1.start()
c2.start()
