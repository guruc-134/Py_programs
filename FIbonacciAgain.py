
#program to find the nth fibonacci number
def findFib(n,y) :
    # fibonacci numbers have repeating last digit after every 60 numbers so we
    #can find the corresponding number
    #in the range of numbers from 1-60
    if n<=0 :
        return 0
    n=n%60
    num1=0
    num2=1
    count=2
    sum=1
    if n==0 :
        return num1%y
    if n==1 :
        return num2%y
    while count<=n :
        num3=(num1+num2)
        num1=num2%y
        num2=num3%y
        count+=1
    return num3%y

numbers=input()
list=numbers.split(" ")
x=int(list[0])
y=int(list[1])
number=findFib(x,y)
print(number%y)
