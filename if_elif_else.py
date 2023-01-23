# Check the given number is positive , negative or zero
# n = int(input("Enter a number = "))
# if n > 0:
#     print("The given number is positive")
# elif n < 0:
#     print("The given number is negative")
# else:
#     print("The given number is zero")

# Check number divisible by 5 and 7
# Check number is divisible by 5 only
# Check number is divisible by 7 only
# Check number is not divisible by 5 and 7

a = int(input("Enter a number = "))
if a % 7 == 0 and a % 5 == 0:
    print("The number is divisible by 7 and 5")
elif a % 7 == 0:
    print("The number is divisible by 7 only")
elif a % 5 == 0:
    print("The number is divisible by 5 only")
else:
    print(" The number is not divisible by both 5 and 7")
