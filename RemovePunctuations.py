sentence=input("enter a sentence\n")

for c in sentence:
    if ord(c)==63 or ord(c)== 96 or ord(c)== 46 or ord(c)== 33 or ord(c)== 39 or ord(c)== 58 or ord(c)==44 or ord(c)==34 or ord(c)==59 :
        sentence=sentence.replace(c,"")
print('\n\n',sentence)
