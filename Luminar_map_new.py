a = [2, 3, 4, 5]
b = map(lambda x: x * x, a)
print(list(b))

# filter

a = [2, 4, 5, 6, 7, 9, 15, 18, 25, 45]
b = filter(lambda x: x % 5 == 0, a)
print(list(b))
c = filter(lambda x: x % 5 != 0, a)
print(list(c))