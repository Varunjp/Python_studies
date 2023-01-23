# Positive , negative and zero
# n = int(input("Enter a number = "))
# if n >= 0:
#     if n > 0:
#         print("Positive")
#     else:
#         print("Zero")
# else:
#     print("Negative")

# Largest among 3 numbers

# a = int(input(" Enter first number = "))
# b = int(input("Enter second number = "))
# c = int(input("Enter third number = "))
# if a > b:
#     if a > c:
#         print("The largest among given number is", a)
#     else:
#         print("The largest among given number is", c)
# elif b > a:
#     if b > c:
#         print("The largest among given number is", b)
#     else:
#         print("The largest among given number is", c)
# else:
#     print("The given number is equal")

# Take 3 mark of subject of a student out of 100 and find the percentage
# above 80% - Dis
# 60-70 First
# 50-59 Second
# 45- Passed

sub1 = int(input("Enter mark of subject1 = "))
sub2 = int(input("Enter mark of subject2 = "))
sub3 = int(input("Enter mark of subject3 = "))
per = ((sub1 + sub2 + sub3)/300) * 100
print("Total percentage = ", per)
if per >= 80:
    print("Grade is distinction")
elif 60 <= per <= 79:
    print("Grade is First class")
elif 50 <= per <= 59:
    print("Grade is second class")
elif 45 <= per <= 49:
    print("Grade is Passed")
else:
    print("Failed")
