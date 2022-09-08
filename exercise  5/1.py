from random import randint
dices = int(input("how many dices do you want to roll: "))
sum_of_rolls = 0
for i in range(dices):
    sum_of_rolls += randint(1,6)
print(f"sum of the numbers are {sum_of_rolls}")

