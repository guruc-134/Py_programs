
""" idea use tuples to create the numbers and then do sorted(Revrse=true)"""
def split(word):
    return [int(char) for char in word]
no=int(input())
if no==0:
    print("0")
    exit()
str=input().split()
numbers=list()
for i in range(no):
    tup=tuple(split(str[i]))
    print(tup)
    numbers.append(tup)
print(numbers)
lengths=list()
for i in range(no):
    lengths.append(len(numbers[i]))
maxLen=max(lengths)
print(maxLen)
print(lengths)
for i in range(no):
    if len[lengths[i]]<maxLen:
        num

numbers.sort(reverse=True)
print(numbers)
