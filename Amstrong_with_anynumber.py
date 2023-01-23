n = int(input("Enter the number = "))
a = n
s = 0
l = len(str(n))
print(l)
while n > 0:
    d = n % 10
    s = s + d ** l
    n = n // 10
if a == s:
    print("Armstrong")
else:
    print("Not armstrong")
