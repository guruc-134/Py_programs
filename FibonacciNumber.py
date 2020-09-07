#program to find the nth fibonacci number
def findFib(n) :
    if n<0 :
        return "enter a valid number"
    li=list()
    if n==0 :
        return 0
    if n==1 :
        return 1
    count=2
    while count<=n :
        list[i].append((list[i-1]+list[i-2])%10)
        count+=1
    return list[n]

n=int(input())
print(findFib(n))
