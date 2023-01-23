# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return n*fact(n-1)
# n = int(input("Enter the number = "))
# factorial=fact(n)
# print(factorial)

# Sum of first n natural number using recusion
def sum(n):
    if n == 1:
        return 1
    else:
        return n+sum(n-1)
n = int(input("Enter the number = "))
Total=sum(n)
print("Sum of natural number", Total)
