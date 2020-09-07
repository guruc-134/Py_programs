#program to find the nth fibonacci number
def findFib(n) :
    if n<0 :
        return "enter a valid number"
    num1=0
    num2=1
    count=2
    if n==0 :
        return num1
    if n==1 :
        return num2
    while count<=n :
        num3=num1%10+num2%10
        num1=num2%10
        num2=num3%10
        count+=1
    return num3

n=int(input())
number=findFib(n)
if number >=10 :
    number=number%10
print(number)
