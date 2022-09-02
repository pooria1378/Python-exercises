import random
number =random.randint(1, 10)
while True:
    guess = int(input('guess the number :'))
    if guess > number:
        print("too high")
    elif guess < number:
        print("too low")
    else:
        print("correct")
        break
