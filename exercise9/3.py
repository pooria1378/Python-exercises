class Car:

    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.traveled_distance = 2000

    def accerelate(self, speed):
        self.current_speed = min(max(self.current_speed + speed, 0), self.maximum_speed)

    def drive(self, number_of_hours):
        self.traveled_distance += (self.current_speed * number_of_hours)

car = Car("ABC-123", 142)
car.accerelate(60)
car.drive(1.5)
print(f"Car's traveled distance is {car.traveled_distance} km.")