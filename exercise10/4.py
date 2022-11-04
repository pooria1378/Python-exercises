import random

class Car:
    def __init__(self, reg_number:str, max_speed:int, cur_speed=0, trv_distance=0):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.cur_speed = cur_speed
        self.trv_distance = trv_distance

    def accelerate(self, change_speed:int):
        self.cur_speed += change_speed
        if self.cur_speed > self.max_speed:
            self.cur_speed = self.max_speed
        elif self.cur_speed < 0:
            self.cur_speed = 0
        return self.cur_speed

    def drive(self, drive_hour:float):
        self.trv_distance += self.cur_speed * drive_hour
        return self.trv_distance

class Race:
    def __init__(self, name:str, distance:int, car_list:list):
        self.name = name
        self.distance = distance
        self.car_list = car_list
        print(f'{self.name}, distance {self.distance} km, participating cars:')
        for car in self.car_list:
            print(f'{car.reg_number}, max speed {car.max_speed} km/h.')

    def hour_passes(self):
        for car in self.car_list:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)

    def print_status(self):
        for car in self.car_list:
            print(f'{car.reg_number}, current speed {car.cur_speed} km/h, travelled distance {car.trv_distance} km.')

    def race_finished(self):
        max_distance = 0
        for car in self.car_list:
            max_distance = max(max_distance, car.trv_distance)
        if max_distance >= self.distance:
            return True


car_list = []
for i in range(10):
    car_list.append(Car(f"ABC-{i+1}", random.randint(100, 200)))

race = Race('Grand Demolition Derby', 8000, car_list)
print()

hour = 0
while race.race_finished() is not True:
    hour +=1
    race.hour_passes()
    if hour % 10 == 0:
        print(f'After {hour} hours:')
        race.print_status()
        print()
print(f'The race finished after {hour} hours:')
race.print_status()