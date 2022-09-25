import random
def roll():
    return random.randint(1,6)
x=roll()
while x != 6:
    print(x)
    x=roll()
print(x)