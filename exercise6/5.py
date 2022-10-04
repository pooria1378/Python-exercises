def odd(num):
    if num % 2 == 0:
        return num
 #   for i in list_1:
        #numlist=int(list_1[i])
           # if (numlist % 2 == 0):
               # list_2.append(numlist)
   # return list_2




list_3=[]
list_1=[]
amount=int(input("enter number on list:",))
print("enter list of number:")
for i in range(1,amount+1):
    num=int(input())
    list_1.append(num)
    odd(num)
    num2=odd(num)
    if num2 != None:
        list_3.append(num2)
#odd(list_1)
print("the First list is:",list_1)
print("the Second list is: ",list_3)