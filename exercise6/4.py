def sum_1(list_1):
    return sum(list_1)



list_1=[]
amount=int(input("enter the amount of list:"))
for i in range(1,amount+1):
    num=int(input("enter list of number:"))
    list_1.append(num)
sum_1(list_1)
print(sum(list_1))