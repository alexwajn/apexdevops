class Bicycle:

    def __init__(self, wheel_size):
        self.wheel_size = wheel_size
        self.speed = 0

    def __str__(self):
        return f"Bike wheel size: {self.wheel_size}, current speed: {self.speed}"

    def accel(self, rate):
        self.speed += rate
    
    def getSpeed(self):
        return self.speed

bikes = []
for i in range(6):
    bike = Bicycle(24)
    bikes.append(bike)
    if i in [1,3,5]:
        bike.accel(10)

for bike in bikes:
    print(bike)

