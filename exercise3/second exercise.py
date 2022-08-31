cabin_class = input("Please enter your cabin class: ")

if cabin_class.lower() == "lux":
    print("upper-deck cabin with a balcony. ")
elif cabin_class.lower() == "a":
    print("above the car deck, equipped with a window. ")
elif cabin_class.upper() == "B":
    print("windowless cabin above the car deck. ")
elif cabin_class.upper() == "C":
    print("windowless cabin below the car deck. ")
else:
    print("Invalid cabin class")