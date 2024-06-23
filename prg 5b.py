# Develop a python program that could search the text in a file for phone numbers (+919900889977) and email addresses (sample@gmail.com) 
import re 
phone_pat=re.compile(r'\+\d{12}$') 
email_pat=re.compile(r'[0-9a-zA-Z._]+@gmail.com') 
f=open("C://Users//deepa//OneDrive//Desktop//ex.txt",'r') 
for line in f: 
    matches=phone_pat.findall(line) 
    for match in matches: 
        print(match) 
    matches=email_pat.findall(line)
    for match in matches: 
        print(match)
