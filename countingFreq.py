inp=input("enter a line/word to count the frequency of a character\n")
ch=input("enter the character\n")
count=[c for c in inp if ch is c]
print(len(count))

