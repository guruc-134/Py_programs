def GCD(x,y) :
    if y==0 :
        return x
    return GCD(y,x%y)

def findLCM(x,y) :
    if x%y==0 :
        return x
    else :
        return (x*y)/GCD(x,y)

numbers=input()
x,y=tuple([int(x) for x in input("enter two numbers to find their lcm").split()])
lcm=0
if x>y :
    lcm=findLCM(x,y)
else :
    lcm=findLCM(y,x)
print(int(lcm))
