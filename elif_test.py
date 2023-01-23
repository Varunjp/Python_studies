# a = int(input("Enter the number"))
# b = int(input("Enter the number"))
# c = int(input("Enter the number"))
# if a>b>c:
#     print("a is greater")
# elif b>a>c:
#     print("b is greater")
# elif c>a>b:
#     print("c is greater")
# else:
#     print("a=b=c")

a = int(input("enter the mark"))
b = int(input("enter the mark"))
c = int(input("enter the mark"))
d = (a+b+c)/300 * 100
if(d>=90):
    print("Distinction")
elif(d>=80 and d<90):
    print("1st class")
elif(d>=70 and d<80):
    print("second class")
else:
    print("Fail")