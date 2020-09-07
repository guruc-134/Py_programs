
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
t=int(input())
for i in range(t):
    no=int(input())
    edges=[int(x) for x in input().split()]
    d=deque(edges)
    maximum=0
    for i in edges:
        if i>maximum:
            maximum=i
    if edges[0]!=maximum and edges[-1]!=maximum:
        print("No")
        break
    else:
        condition=True
        while(len(d)!=0 and condition):
            current=0
            if d[0]>d[-1]:
                out=d.popleft()
                if out < current:
                    print("No")
                    condition=False
                current=out
            else:
                out=d.popleft()
                if out < current:
                    print("No")
                    condition=False
                current=out
        if  condition:
            print("Yes")
