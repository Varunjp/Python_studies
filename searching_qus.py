# check if the entered key exist in given list
lst = [4,2,6,5,8,7,4,3,9]
a = int(input("Enter the value = "))
for i in lst:
    if i == a:
        flag=1
        break
    else:
        flag=0
if flag == 1:
    print("Value found")
else:
    print("Not found")
