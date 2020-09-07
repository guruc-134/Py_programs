# we will be getting an integer indicating the number of kms a car can travell
#before running out of fuel
"""
in the second line we will have an array/list of numbers indicating the refilling
gas stations
in the answerline we need to indicate the minimum number of refils required to move
from  a to b distance between which will be indicated in the second line

l
0 1 2 3 4 5 6 7 ...n n+1
0--a
n+1----b
1,2--n are the gas stations
 o/p
 min num of refils
 """
a=int(input())
l=int(input())
n1=int(input())
if n1==0:
    print("0")
    exit()
gasStations=input()
gs=gasStations.split()
num=len(gs)

lst=list()
lst.append(0)
for i in range(num):
    lst.append(int(gs[int(i)]))
lst.append(a)
#print(lst)
n=len(lst)-2
currentRefil=0
no_refils=0
b=True
for j in range(1,n+1) :
    lastRefil=currentRefil
    while currentRefil<=n  and lst[currentRefil+1]-lst[lastRefil]<=l:
        currentRefil+=1
    if currentRefil==lastRefil:
        b=False
        break
    if currentRefil<=n :
    #    print("refill at :",lst[currentRefil])
        no_refils+=1
if b==False and currentRefil is not n+1:
    print("-1")#impossible
else:
    print(no_refils)
