a = int(int(input("Enter the lower limit = ")))
b = int(int(input("Enter the upper limit = ")))
c = []
for i in range(a, b):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        c.append(i)
print("Prime number between the given limit", list(c))
