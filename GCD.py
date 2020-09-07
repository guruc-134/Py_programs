def GCD(x,y) :
    if y==0 :
        return x
    return GCD(y,x%y)
numbers=input()
list=numbers.split(" ")
x=int(list[0])
y=int(list[1])
print(GCD(x,y))
