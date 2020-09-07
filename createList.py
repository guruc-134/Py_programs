# DAY--2 Assignment
"""
create a empty list and append elements
"""
def createList():
    n=int(input("enter the number of elements\n"))
    print("enter %d elements"%(n))
    count=0
    return [int(x) for x in input().split()]

newlist=createList()
print(newlist)
