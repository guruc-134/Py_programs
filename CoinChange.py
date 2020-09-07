# denominations
import numpy as np
den=[1,3,4]
sum=int(input())
t=[[0 for x in range(sum+1)] for y in range(4)]
for i in range(sum+1):
    t[0][i]=2147483647-1
for i in range(1,4):
    for j in range(1,sum+1):
        if j%den[0]==0:
            print("hi")
            t[i][j]= j//den[0]
        else:
            t[i][j]=2147483647-1
for i in range(1,4):
    for j in range(1,sum+1):
        if den[i-1]<j:
            t[i][j]=min(1+t[i][j-den[i-1]],t[i-1][j])
        else:
            t[i][j]=t[i-1][j]
print(np.array(t))
print(t[3][sum])
