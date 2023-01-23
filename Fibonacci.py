# Fibon = 0 1 1 2 3 5 8 13
n = int(input("Enter the limit = "))
f = 0
s = 1
print(f, end=" ")
print(s, end=" ")
for i in range(2, n):
    t = f+s
    print(t, end=" ")
    f = s
    s = t
