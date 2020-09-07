import numpy as np
def numSubseq(List,target):
    cols,rows=sum(List),len(List)
    t=[[False for x in range(cols+1)] for j in range(rows+1)]
    for i in range(rows+1):
        t[i][0]=True
    #print(np.array(t))
    List.sort()
    count=0
    for i in range(1,rows+1):
        for j in range(1,cols+1):
            if List[0]+List[i-1]<=target:
                count+=1
            if List[i-1]<=j:
                t[i][j]=t[i-1][j] or t[i-1][j-List[i-1]]
            else:
                t[i][j]=t[i-1][j]
    print(np.array(t))
    print(count)



numSubseq([3,6,7,5],9)
