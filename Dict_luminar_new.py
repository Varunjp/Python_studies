dict1={}
print(dict1)
dict1['Name']='Sasi'
dict1['Age']=46
dict1['Job']='Varkapani'
dict1['Hobby']='Vellamadi'
print(dict1)
dict2={'Peru':'Lalu','Vayyasu':'26','Pani':'Mesthiri'}
print(dict2)
dict1.update(dict2)
print(dict1)
print(dict1.get('Name'))  # get value of a keyword
