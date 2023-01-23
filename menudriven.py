def add(x, y):
    print("addition", x + y)


def sub(x, y):
    print("Subtraction", x - y)


def mul(x, y):
    print("Multiplication", x * y)


def div(x, y):
    print("Division", x // y)


while True:
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Break from the program")
    choice = int(input("Enter the choice = "))
    if choice == 1:
        a = int(input("enter the number = "))
        b = int(input("enter the number = "))
        print("Addition", add(a, b))
    elif choice == 2:
        a = int(input("enter the number = "))
        b = int(input("enter the number = "))
        print("Subtraction", sub(a, b))
    elif choice == 3:
        a = int(input("enter the number = "))
        b = int(input("enter the number = "))
        print("Multiplication", mul(a, b))
    elif choice == 4:
        a = int(input("enter the number = "))
        b = int(input("enter the number = "))
        print("Division", div(a, b))
    elif choice == 5:
        break
    else:
        print("Invalid input")
