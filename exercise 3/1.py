fish_length = int(input("Insert the length of the fish in (CM): "))
if fish_length < 42:
    small = 42 - fish_length
    print(f"release the fish in the lake and it is {small} cm below the limit size")
else:
    print("it's yours!")