import random

def randomRoll():
        return random.randint(1,num)

def main(num):
    num1=None
    while num != num1:
        num1=randomRoll()
        print(num1)
num=int(input("enter number of side:"))
main(num)