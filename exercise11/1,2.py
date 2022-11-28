"""

class Person:
    def __init__(self, name:str, email:str):
        self.name=name
        self.email=email

    def new_email(self, new_domain:str):
        domain=self.email.split('@')[1]
        self.email= self.email.replace(domain, new_domain)




class Parents(Person):
    def __init__(self,name:str, email:str, mobile_number:str):
     super().__init__(name, email)
     self.mobile:mobile_number
class Students(Person):
    def __init__(self,name:str,email:str, student_number:str,group:str):
        super().__init__(name, email)
        self.student_number= student_number
        self.group=group

peter= Students("Peter", "Peter@cool.com", "1234", "A")
print(f"This is a new student {peter.name}. {peter.student_number}")
peter.new_email("metropolia.fi")
print(f'New email: {peter.email}')

"""

"""
class HomeApp:
    def __init__(self, power):
        self.power=power



class WhiteGoods:
    def __init__(self, life_span):
        self.life_span=life_span

class Washingmachine:
    def __init__(self, power, life_span, origin):
        HomeApp.__init__(self, power)
        WhiteGoods.__init__(self, life_span)
        self.origin=origin

bosch=Washingmachine(280,20,"Germany")
print(f'{bosch.power}. {bosch.life_span}. {bosch.origin}')

"""
"""
class Item:
    def __init__(self, name:str, price:float):
        self.name=name
        self.price=price

class BasicCard:
    def __init__(self):
        self.product_list=[]

    def add_product(self, product:Item):
        self.product_list.append(product)

    def calculate_bonus(self):
        bonus=0
        for product in self.product_list:
            bonus += product.price*0.25
            return bonus

class PremiumCard(BasicCard):
    def __init__(self):
        super().__init__()

    def calculate_bonus(self):
        bonus= super().calculate_bonus()
        #for product in super().product_list():
        bonus += bonus*1.05
        return bonus


card1 = BasicCard()
card1.add_product(Item('Red Wine', 90.5))
card1.add_product(Item('Cheddar', 4.5))
bonus = card1.calculate_bonus()
print(f'Bonus {bonus}')

"""

"""

class Publication:
    def __init__(self, name):
        self.name = name

    def print_info(self):
        print(self.name)

class Book(Publication):
    def __init__(self, name, author, page_num):
        super().__init__(name)
        self.author=author
        self.page_num = page_num
    def print_info(self):
        super().print_info()
        print(f'Author: {self.author}, {self.page_num} pages ')

class Magazine(Publication):
    def __init__(self, name, editor):
        super().__init__(name)
        self.editor=editor
    def print_info(self):
        super().print_info()
        print(f'Chief editor: {self.editor}')

Publications=[]
Publications.append(Magazine('Donald Duck', 'Aki something'))
Publications.append(Book('The wild donkey','Candice Ligma', 400))
for x in Publications:
    x.print_info()


"""
class Car:
    def __init__(self, reg_number: str, max_speed: int, currnt_speed=0, distance=0):
        self.name = reg_number
        self.max_speed = max_speed
        self.current_speed = currnt_speed
        self.distance = distance

    def accelerate(self, acceleration):
        self.change = acceleration
        self.current_speed += self.change
        if self.current_speed < 0:
            self.current_speed = 0
        elif self.current_speed > self.max_speed:
            self.current_speed = self.max_speed

    def drive(self, time):
        self.distance += self.current_speed * time



class ElectricCar(Car):

    def __init__(self, reg_number, max_speed, battery_capacity):
        super().__init__(reg_number, max_speed)
        #super().__init__()
        self.battery=battery_capacity

class GasolineCar(Car):
    def __init__(self, reg_number, max_speed, tank_capacity):
        super().__init__(reg_number, max_speed)
        #super().__init__(max_speed)
        self.tank=tank_capacity

car1=ElectricCar('ABC-15', 180, 52.5)
car2=GasolineCar('ACD-123', 165, 32.3)
Speed=int(input('How fast are the cars going? '))
Time=int(input('For how long are the cars driving? '))
car1.accelerate(Speed)
car2.accelerate(Speed)
car1.drive(Time)
car2.drive(Time)
print(f'For car {car1.name}\n'
      f'Max speed={car1.max_speed}\n'
      f'Current speed:{car1.current_speed}\n'
      f'Distance:{car1.distance}\n'
      f'Kw/h usage: {car1.battery*Time}\n'
      f'')

print(f'For car {car2.name}\n'
      f'Max speed={car2.max_speed}\n'
      f'Current speed:{car2.current_speed}\n'
      f'Distance:{car2.distance}\n'
      f'Fuel usage: {(car2.tank*Time):.2f}')
