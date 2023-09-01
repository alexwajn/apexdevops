
class Car:
    wheels = 4
    axle_number = 2
    number_doors = 5
    speed = 0
    is_engine_running = False
    
    def __init__(self, brand, model, year, color, type, fuel):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.type = type
        self.fuel = fuel

    def accelerate(self, rate):
        self.speed = self.speed + rate
        
    def brake(self, rate):
        self.speed = self.speed - rate        

    def start_engine(self):
        self.is_engine_running = True

    def stop_engine(self):
        self.is_engine_running = False
        
    def horn(self):
        print("Honk honk!")
    


    









