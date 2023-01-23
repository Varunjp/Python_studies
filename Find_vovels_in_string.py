str = input("Enter the string ")  # I love python
v = 0
s = 0
c = 0
lst1=[]
lst2=[]
for i in str:
    if i in 'aeiouAEIOU':
        lst1.append(i)
        v += 1
    elif i == ' ':
        s += 1
    else:
        lst2.append(i)
        c += 1
print('Vowels in given string is', lst1)
print('Number of vowels in the string is', v)
print('Space in given string is', s)
print('Consonants  in given string is', lst2)
print('Number of Consonants is', c)
