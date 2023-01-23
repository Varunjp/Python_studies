# def fun(*num):
#     print(type(num))
#     for i in num:
#        print(i)
#
# fun(10)
# fun(10,20,30)
# fun(10,20,30,40)

# Find the sum of element passing through the argument?

# def fun(*num):
#     print(type(num))
#     a = 0
#     for i in num:
#         a = a + i
#     print(a)
#
#
# # fun(10)
# # fun(10,20,30)
# fun(10, 20, 30, 40)


def fun(**karg):
    print(type(karg))
    for key, value in karg.items():
        print(key, "is", value)


fun(name="Anu", Age="20", cls="Bio")
