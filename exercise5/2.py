numbers = []
user_input = input("enter your numbers(minimum 5 numbers) or to quit pressing enter: ")
while user_input != "":
    numbers.append(int(user_input))
    user_input = input("enter your next number or to quit pressing enter: ")
numbers.sort(reverse=True)
for i in range(5):
    print(numbers[i])
