num=int(input("enter a number to find its multiplication table\n"))
s,e=tuple([int(x) for x in input("enter the interval for table\n").split()])
print("------------------table----------------\n")
for i in range(s,e+1):
    print(" %d X  %d  =  %d"%(num,i,num*i))
