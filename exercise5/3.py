
user_input = int(input("enter your number: "))
if user_input>1:
    is_prime = True
    for i in range(2,user_input):
        if user_input % i == 0:
            is_prime = False
    if is_prime == True:
        print("it's prime number")
    else:
        print('not prime number')
else:
    print("invalid input.")