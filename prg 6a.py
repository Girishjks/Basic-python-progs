# Write a python program to accept a file name from the user and perform the following operations 
# 1. Display the first N line of the file 
# 2. Find the frequency of occurrence of the word accepted from the user in the file 
fname = input("Enter the filename : ")
infile = open(fname, "r")
line = int(input("Enter the first N line "))
for x in range(line):
    a = infile.readline()
    print(x+1, ":", a)
infile.seek(0)
word = input("Enter a word : ")
cnt = 0
for line in infile:
    r = line.split()
    cnt += r.count(word)
print("The word", word, "appears", cnt, "times in the file")
