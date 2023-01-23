# Find the sum of multiples of 3 under 30
a = 0
for i in range(0, 31, 3):
    print(i, end=' ')
    a += i
print("Sum of total =", a)
