# Map
# lst = ['2', '5', '6', '4']
# res = map(int, lst)
# print(list(res))

# def sq(a):
#     return a * a
#
#
# lst = [1, 2, 3, 4, 5, 6]
# res = map(sq, lst)
# print(list(res))

# Lambda function

# lst = [1, 2, 3, 4, 5, 6]
# lst1 = [1, 2, 3, 4, 5, 8]
# res = map(lambda x, y: x + y, lst, lst1)
# print(list(res))

lst = ['sat', 'bat', 'hat']
res = map(list, lst)
print(list(res))
