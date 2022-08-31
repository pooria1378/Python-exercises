year = int(input("enter your year: "))
if year % 400 == 0 or year % 100 != 0 and year % 4 ==0:
    print("given year is leap year")
else:
    print("given year is not leap year")