def Factorial(n):
    if n==0:
        return 1
    else:
        return n*Factorial(n-1)


n=int(input("enter a number \n"))
print(Factorial(n))
