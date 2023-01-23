# Factorial of a number
a = int(input("Enter the number = "))
fact = 1
for i in range(1, a+1):
    fact = fact * i
print("Factorial of", a, "=", fact)

# Sum of first 100 natural numbers
# b = int(input("Enter the limit = "))
# a = 0
# for i in range(0, b+1):
#     a = a + i
# print("Sum of natural number till", b, "=", a)
