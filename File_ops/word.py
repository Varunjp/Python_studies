# fi = open('new', 'r')
# a = fi.read()
# # print(a)
# for i in a.split():
#     print(i)

# Count the word and add in dictionary
fi = open('new', 'r')
a = fi.read()
count = {}
for i in a.split():
    if i not in count:
        count[i] = 1
    else:
        count[i] += 1
print(count)
for j, k in count.items():
    print(j, k)
