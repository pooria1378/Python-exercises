class Elevator:
    def __init__(self, top:int, bottom=0):
        self.bottom = bottom
        self.top = top
        self.current = self.bottom
        #print(f'The elevator starts from bottom floor {self.current}. Top floor is {self.top}.')

    def floor_up(self):
        self.current += 1
        print(f'The elevator goes up to floor {self.current}.')

    def floor_down(self):
        self.current -= 1
        print(f'The elevator goes down to floor {self.current}.')

    def go_to_floor(self, to_floor:int):
        print()
        if to_floor in range(self.bottom, self.top+1):
            while self.current != to_floor:
                if self.current < to_floor:
                    self.floor_up()
                else:
                    self.floor_down()
        else:
            print(f'Floor {to_floor} does not exist!')

class Building:
    def __init__(self, number_of_elevators:int, top:int, bottom=0):
        self.elevator_list = []
        self.top = top
        self.bottom = bottom
        print(f'The building has {number_of_elevators} elevators. '
              f'Top floor is {top}. Bottom floor is {bottom}.')
        for i in range(number_of_elevators):
            elevator = Elevator(self.top, self.bottom)
            self.elevator_list.append(elevator)

    def run_elevator(self, elevator_no:int, dest_floor:int):
        #print()
        if elevator_no in range(1, len(self.elevator_list)+1):
            self.elevator_list[elevator_no-1].go_to_floor(dest_floor)
            print(f'Elevator no. {elevator_no} is now at floor {self.elevator_list[elevator_no-1].current}.')
        else:
            print(f'Elevator no. {elevator_no} does not exist!')

    def fire_alarm(self):
        #print()
        for elevator in self.elevator_list:
            elevator.go_to_floor(self.bottom)
        #for i in range(1, len(self.elevator_list)+1):
            #self.run_elevator(i, self.bottom)
            print(f'Fire alarm! '
                  f'Elevator no. {self.elevator_list.index(elevator)+1} is now at floor {elevator.current}!')
                  #f'Elevator no. {i} is now at floor {self.elevator_list[i-1].current}.')


#h = Elevator(7)
#h.go_to_floor(8)
#h.go_to_floor(5)
#h.go_to_floor(0)


karamalmi = Building(3, 7)

karamalmi.run_elevator(1, 5)
karamalmi.run_elevator(2, 6)

karamalmi.fire_alarm()

