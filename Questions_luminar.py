# 1. Temperature conversion
# print("Temperature conversion")
# print("1. Celcius to Fahrnheit")
# print("2. Fahernheit to celcius")
# cho = int(input("Enter the choice = "))
# if cho == 1:
#     a = int(input("Enter the temperature in celcius = "))
#     f = (9/5)*a+32
#     print("Fahernheit =", f)
# elif cho == 2:
#     a = int(input("Enter the temperature in Fahernheit = "))
#     f = (5 / 9) * (a - 32)
#     print("Celcius =", f)
# else:
#     print("Invalid choice")
#
# 2. Remove the index from string

# a = str(input("Enter the string = "))
# print(a)
# b = int(input("Enter the index to remove = "))
# d = len(a)
# if b < d:
#     c = a[:b] + a[b + 1:]
#     print(c)
# else:
#     print("Index doesn't exist")

# 3. enter 2 string, create new string
# string = hello
# string = world
# string = wollo herld
a = str(input("Enter the 1 string = "))
b = str(input("Enter the 2 string = "))
print("1 string is ", a)
print("2 string is ", b)
print("After process")
c = b[:2] + a[2:]
d = a[:2] + b[2:]
print(c, d)
