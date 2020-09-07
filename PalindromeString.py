str=input("enter a string to check if its a palindrome\n")
lst=list(str)
lst.reverse()
rev=""
for x in lst:
    rev+=x
if rev == str:
    print("palindrome")
else:
    print("not palindrome")
