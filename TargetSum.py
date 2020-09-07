import numpy as np
def countSubsets(arr,s):
    n=len(arr)
    print(arr)
    t = [[0 for x in range(s+1)] for x in range(n+1)]
    for i in range(n+1):
        t[i][0]=1

    for i in range(1,n+1):
        for j in range(1,s+1):
            if arr[i-1]<=j:
                t[i][j]=t[i-1][j]+t[i-1][j-arr[i-1]]
            else:
                try:
                    t[i][j]=t[i-1][j]
                except:
                    print(j,s)
    return t[n][s]

def findTargetSumWays(List, S: int) -> int:
    Sum=sum(List)
    newValue=(Sum+S)//2
    print(newValue)
    return countSubsets(List,newValue)

nums=[0,0,0,0,0,1]
S=1
print(findTargetSumWays(nums,S))
