n = int(input("Enter the number = "))
s = 0
a = n
while n > 0:
    d = n % 10
    s = s+d*d*d
    n = n // 10
print(s)
if s == a:
    print("The number is armstrong number")
else:
    print("The number is not armstrong number")
