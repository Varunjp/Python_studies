import functools

lst = [1, 2, 3, 4]
result = functools.reduce(lambda x, y: x + y, lst)
print(result)

# Different method

from functools import reduce
import operator

lst = [1, 2, 3, 4]
result = reduce(operator.add, lst)
print(result)
result1 = reduce(operator.sub, lst)
print(result1)

# content = dir(operator)
# print(content)
