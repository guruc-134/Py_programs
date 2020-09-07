
n=int(input())
numbers=input()
#print(numbers)
numbers.strip()
numbers=numbers.split(" ")
list=[None]*n
count=0
for num in numbers :
    if(num !=' ') :
        list[count]=int(numbers[count])
        count+=1
#print(list)
max1=list[0]
index1=0
i=0
#finding max
for no in list :
    if no > max1 :
        max1=no
        index1=i
    i+=1
    #finding second max
max2=-2.2250738585072014e-308
i=0
for no in list :
    if no > max2 and (no <=max1 and i!=index1) :
        max2=no
    i+=1
print(max1*max2)
