def fib(n):
    if n==0:
        return 0
    if n==1 :
        return 1
    else :
        return fib(n-1)+fib(n-2)

n=int(input("enter a n value to get fib series\n"))
for i in range (0,n+1):
     print(fib(i),end=" ")
