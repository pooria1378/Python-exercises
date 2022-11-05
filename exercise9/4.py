import random
class Car:
    def __init__(self, regNum, maxSpeed):
            self.regNum = regNum
            self.maxSpeed = maxSpeed
            self.currentSpeed = 0
            self.travDis = 0
    def acceleration(self, acceleration):
            self.currentSpeed = min(max(self.currentSpeed + acceleration, 0), self.maxSpeed)
    def drive(self, time):
        self.travDis += self.currentSpeed * time

tesla =Car("ABC-123", 142)
print()
print(f'Registration number of {tesla.regNum}, maximum speed is{tesla.maxSpeed} km/h'
      f'Current speed is {tesla.currentSpeed} km/h, travel distance is {tesla.travDis}')
car_list = []
for i in range(10):
    car_list.append(Car("ABC-" + str(i + 1), random.randint(100, 200)))
travMax = 0
while travMax < 10000:
    for raceCar in car_list:
        raceCar.acceleration(random.randint(-10, 15))
        raceCar.drive(1)
        travMax = max(raceCar.travDis, travMax)
for raceCar in car_list:
    print(f"{raceCar.regNum:6s} : {raceCar.maxSpeed} km/h, {raceCar.travDis} km")
print(f"the winner was able to travel {travMax}")