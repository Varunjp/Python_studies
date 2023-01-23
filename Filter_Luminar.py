# Filter
# def even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
#
#
# lst = [1, 2, 3, 4, 5, 6, 7]
# res = filter(even, lst)
# print(list(res))

a = list(input("Enter the list with space = ").split())
b = map(int, a)
b = list(b)


def check(b):
    if b % 2 == 0:
        c = b
        return c
    else:
        d = b
        return d


re = filter(check, b)
print(list(re))
