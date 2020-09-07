import math
def checkPrime(i):
    count=0
    if i==1:
        return False
    for c in range(2,int(math.sqrt(i/1))+1):
        if i%c==0:
            count+=1
    return (count==0)
l,h=tuple([int(x) for x in input("enter the range to get primmes in that range\n").split()])
print("the prime numbers in range %d and %d are "%(l,h))

for i in range(l,h+1):
    if checkPrime(i):
        print(i)
