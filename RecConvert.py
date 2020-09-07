l=list()
def binary(n):
    if n==0:
        return
    binary(n//2)
    print(n%2,end="")



number=int(input("enter a number\n"))
binary(number)
