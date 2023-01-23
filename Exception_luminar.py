# Abnormal conditions


# a = int(input("Enter the first number = "))
# b = int(input("Enter the second number = "))
# try:  # suspected code
#     div = a / b
#     print(div)
# except:  # Code to handle exceptions
#     print("Division by zero not possible")
# else:  # executes if no exceptions
#     print("Hai")
# finally:  # Executes on all situation
#     print("Use to print in any situation")

try: # suspected code
    a = int(input("Enter the first number = "))
    b = int(input("Enter the second number = "))
    div = a / b
    print(div)
except ValueError:
    print("The entered value is incorrect")
except NameError:
    print("The variable incorrect")
except ZeroDivisionError:  # Code to handle exceptions
    print("Division by zero not possible")
except:
    print("Error")
