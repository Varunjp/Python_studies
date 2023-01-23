# lst = ["apple", "orange", "banana", "kiwi", "cherry"]
# Newlst = []
# for i in lst:
#     if 'a' in i:
#         Newlst.append(i)
# print(Newlst)

# List Comphrehension
# lst = ["apple", "orange", "banana", "kiwi", "cherry"]
# newlst = [x.upper() for x in lst if x != "apple"]
# print(newlst)

# Create new given list
# lst1=[0,1,2,3,4]
# lst = [x for x in range(5)]
# print(lst)

# Replace element in list (If want to write if else then start with if condtion)
# lst = ["apple", "orange", "banana", "kiwi", "cherry"]
# newlst = [x if x!="banana" else "strawberry" for x in lst ]
# print(newlst)

# How to remove duplicate elements in a list
lst = [2, 3, 4, 2, 5, 6, 2, 3, 5]
newlst=[]
for i in lst:
    if i not in newlst:
        newlst.append(i)
print(newlst)
