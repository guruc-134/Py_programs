n=int(input("enter a number to find the fibonacci series\n"))
num1=0
num2=1
if n==0:
    print("enter a number >0")
    exit()
if n==1:
    print(0)
    exit()
print("0 1",end=" ")
i=2
while i<n:
    num3=num1+num2
    num1,num2=num2,num3
    print(num3,end=" ")
    i+=1
