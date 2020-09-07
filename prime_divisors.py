#divisors of number

n=int(input("enter the number"))
i=2
count=0
while i<=n/2:
    if n%i==0:
        count+=1
        break
    i+=1
print(n)
if count==0:
    print("the number %d is prime"%(n))

        
