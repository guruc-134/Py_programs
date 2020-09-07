lst=[int(x) for x in input("enter the list of  numbers \n").split()]
key=int(input("enter a key to check divisibility of the numbers in the list"))
for i in lst:
    if(i%key==0):
        print(i)
