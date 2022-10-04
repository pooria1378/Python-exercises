month_of_seasons = ("March", "April", "May", "June", "July", "August", "September", "October", "November", "December", "January", "February")
number_of_month = int(input("Enter the number of your favorite month: "))
if (number_of_month-1) == 0 or (number_of_month-1) == 1 or (number_of_month-1) == 2:
    print(f"Month number {number_of_month} belongs to the Spring.")
elif (number_of_month-1) == 3 or (number_of_month-1) == 4 or (number_of_month-1) == 5:
    print(f"Month number {number_of_month} belongs to the Summer.")
elif (number_of_month-1) == 6 or (number_of_month-1) == 7 or (number_of_month-1) == 8:
    print(f"month number{number_of_month} belongs to the Autumn.")
elif (number_of_month-1) == 9 or (number_of_month-1) == 10 or (number_of_month-1) == 11:
    print(f"month number{number_of_month} belongs to the Winter.")
else:
    print("We have just 12 months which starts from 1.")