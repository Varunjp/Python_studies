# Check prime or not
a = int(input("Enter a number = "))
flag = 0
for i in range(2, int((a/2)+1)):
    if a % i == 0:
        flag = 1
        break
if flag == 1:
    print("The number is not prime")
else:
    print("The given number is prime")
