# open and read file
# fo = open("new", 'r')
# # print(fo.read())
# # print(fo.readlines())
# for i in fo.readlines():
#     print(i.strip())
# fo.close()
# print(fo.name)  # retrieve name
# print(fo.mode)  # Check the mode of operation
# print(fo.closed)  # Check if file is closed or not

# Find the number of file
# fo = open("new", 'r')
# print("Number of lines in file is", len(fo.readlines()))
# fo.close()

# Write new line in file
# f1 = open("new", 'r+')
# f1.write("How's the day going on?")
# print(f1.tell())  # returns file pointer position
# f1.seek(0)  # change the file pointer position
# print(f1.read())
# f1.close()

# Write using writelines
# f1 = open("new", 'r+')
# seq = ["First line\n", "Second line\n", "Third line\n"]
# f1.writelines(seq)
# f1.seek(0)
# print(f1.readlines())
# f1.close()

# Copy the content a file to another file?
# f1 = open("new", "r")
# a = f1.read()
# f2 = open("new2", 'r+')
# f2.writelines(a)
# f2.seek(0)
# print(f2.read())
# f1.close()
# f2.close()

# Editing file in different location
# f1 = open(r"C:\Users\varun\Desktop\New Text Document.txt", 'w')
# f1.write("Hi python")
# f1.close()

f1 = open("new",'r')
a = f1.readlines()
print(a)
a.reverse()
print(a)
for i in a:
    print(i.strip())
