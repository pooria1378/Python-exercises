names = set()
ask_name = True
while ask_name:
    your_name = input("Enter a name: ").lower()
    if len(your_name) == 0:
        ask_name = False
    else:
        if your_name in names:
            print("Existing name")
        else:
            print("New name!")
            names.add(your_name)

for name in names:
    print(name)