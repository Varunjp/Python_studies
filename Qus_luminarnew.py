# Find the largest element in a list without using any function?

lst = [5, 16, 9, 4, 8, 7, 5, 25]
a = 0
for i in lst:
    if i > a:
        a = i

print(a)
