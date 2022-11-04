class Car:
    def __init__(self, regNum, maxSpeed):
            self.regNum = regNum
            self.maxSpeed = maxSpeed
            self.currentSpeed = 0
            self.travDis = 0
    def acceleration(self, acceleration):
            self.currentSpeed = min(max(self.currentSpeed + acceleration, 0), self.maxSpeed)

tesla =Car("ABC-123", 142)
print()
print(f'Registration number of {tesla.regNum}, maximum speed is{tesla.maxSpeed} km/h'
      f'Current speed is {tesla.currentSpeed} km/h, travel distance is {tesla.travDis}')