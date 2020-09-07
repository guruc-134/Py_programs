import numpy as np
def canPartition(List):
    n=len(List)
    S=sum(List)
    if S%2!=0:
        return False
    S=S//2
    rows, cols = (n+1,S+1)
    t = [[False for i in range(cols)] for j in range(rows)]
    for i in range(n+1):
        t[i][0]=True
    print(np.array(t))

    for i in range(1,n+1):
        for j in range(1,S+1):
            if List[i-1]<=j:
                t[i][j]=t[i-1][j] or t[i-1][j-List[i-1]]
            else:
                t[i][j]=t[i-1][j]
    print("\n\n",np.array(t))


canPartition([1,2,3,5])
