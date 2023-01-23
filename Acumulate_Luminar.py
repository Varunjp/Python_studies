# Accumulate
import itertools

lst = [1, 2, 3, 4]
res = itertools.accumulate(lst, lambda x, y: x + y)
print(list(res))
