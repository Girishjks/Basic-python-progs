# Write a Python program that accepts a sentence and find the number of words, digits, uppercase letters and lowercase letters.
word = input("Enter a word : ")
digi = ucase = lcase = wordcnt = 0
wordcont=word.split()
for x in word:
    if x>='0' and x<='9':
        digi += 1
    if x>='A'and x<='Z':
        ucase += 1
    if x>='a' and x<='z':
        lcase += 1
print("This word has\n")
print("words: ", len(wordcont),"\n" "digits",digi, )
print("upper case letters",ucase, "\n" "lower case letters ",lcase)
