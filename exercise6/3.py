def convert(quantity):
    litre=quantity*3.79
    return litre


quantity=float(input("enter Quantity of Gasoline:",))
convert(quantity)
print(convert(quantity))