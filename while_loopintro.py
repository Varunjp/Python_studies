# i = 1
# while i <= 10:
#     print(i, end=" ")
#     i += 1
# Print all the even numbers upto 10 and display it's sum
# i = 2
# sum = 0
# while i <= 10:
#     sum += i
#     print(i)
#     i += 2
# print("Sum of even numbers =", sum)
#
# Calculate the sum of digit in a number
# n = int(input("Enter a number = "))
# s = 0
# while n > 0:
#     d = n % 10
#     s += d
#     n = n // 10
# print("Sum of digit", s)
# Reverse number
n = int(input("Enter a number = "))
rev = 0
while n > 0:
    s = n % 10
    if s == 0:
        print(s, end='')
    rev = rev * 10 + s
    n = n // 10
print(rev)
# palindrome or not
# n = int(input("Enter a number = "))
# rev = 0
# a = n
# while n > 0:
#     s = n % 10
#     rev = rev * 10 + s
#     n = n // 10
# print("Reverse of digit", rev)
# if a == rev:
#     print("The given number is palindrome")
# else:
#     print("The given number is not palindrome")
