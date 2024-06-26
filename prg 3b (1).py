# Write a Python program to find the string similarity between two given strings 
def compare(s,p):
    count=0
    n=min(len(s),len(p))
    for i in range(n):
        if s[i]==p[i]:
            count+=1
    return count
s1 = input("Enter String 1 \n")
s2 = input("Enter String 2 \n")
mx=max(len(s1),len(s2))
count=compare(s1,s2)
similarity=count/mx*100
print ("Total number letter matched is",count)
print("simirality between two string is",similarity)
