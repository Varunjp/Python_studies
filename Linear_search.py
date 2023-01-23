# linear search
def linearsearch(lst1, key):
    n = len(lst1)
    for i in range(0, n):
        if lst1[i] == key:
            return i
    return -1


lst = input("Enter the list (with space) = ").split()
key = int(input("Enter the key = "))
for i in range(0, len(lst)):
    lst[i] = int(lst[i])
print(lst)
res = linearsearch(lst, key)
if res == -1:
    print("Not found")
else:
    print("Item found in index ", res)
