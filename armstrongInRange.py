
def printArmstrong(num):
    temp = num
    dig=[int(x) for x in str(temp)]
    k=len(dig)
    sum=0
    while temp > 0:
       digit = temp % 10
       sum += digit **k
       temp //= 10
    if num == sum:
        print(num)

s,e=tuple([int(x) for x in input("enter the range for getting armstrong numbers\n").split()])
print(s,e)
for i in range(s,e+1):
    printArmstrong(i)
