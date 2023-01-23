# Find the largest among the list
import functools

lst = [2, 6, 7, 9, 2, 4]
res = functools.reduce(max, lst)
print(res)
