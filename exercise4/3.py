number = input("enter a number: ")
maximum = float(number)
minimum = float(number)
while number != "":
    number = float(number)
    if number < minimum:
        minimum = number
    if number > maximum:
        maximum = number
    number = input("enter a number: ")
print(f"maximum: {maximum} \nminimum: {minimum}")
