#program to find the nth fibonacci number
def findFib(n) :
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
        return num1%10
    if n==1 :
        return num2%10
    while count<=n :
        num3=(num1+num2)
        num1=num2%10
        num2=num3%10
        count+=1
        sum+=num3%10
    return sum

numbers=input()
list=numbers.split(" ")
x=int(list[0])
y=int(list[1])
number1=findFib(x-1)
number2=findFib(y)
number=number2-number1
if number<0:
    number+=10
    number%=10
print(number%10)
