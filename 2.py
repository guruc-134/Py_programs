import math
def my_function(x):
  return list(dict.fromkeys(x))
def primeFactors(n,k):
    n=int(input())
    lst=list()
    while n % 2 == 0:
        lst.append(2)
        n = n / 2
    for i in range(3,int(math.sqrt(n))+1,2):
        while n % i== 0:
            lst.append(i)
            n = n / i
    if n > 2:
        lst.append(n)
    count=0
    mylist = my_function(lst)
    #if len(mylist)==k:
    #    return 1
    return mylist

n=int(input())
j=0
while j<n:
    str=input().split()
    print(str)
    l=int(str[0])
    h=int(str[1])
    k=int(str[2])
    i=l
    count=0
    while i<h:
        count=primeFactors(i,k)
        if len(count)==k:
            count+=1
    print(count)
    j+=1
