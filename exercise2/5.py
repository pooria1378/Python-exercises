talents = float(input("please insert your mass in talents : "))
pounds = float(input("please insert your mass in pounds : "))
lots = float(input("please insert your mass in lots : "))
all_in_grams = talents * 8512 + pounds * 425.6 + lots * 13.3
kilograms = int(all_in_grams / 1000)
grams = all_in_grams % 1000
print(f"The weight in modern units:\n{kilograms} kilograms and {grams} grams.")
