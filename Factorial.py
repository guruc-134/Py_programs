def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
num=int(input("enter a number to find the factorial\n"))
print(factorial(num))
