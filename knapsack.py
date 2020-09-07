def value(weights,S):
    size=len(weights)
    t=[[0 for i in range(S+1)] for j in range(size+1)]
    for i in range(S+1):
        t[0][i]=0
    for i in range(size+1):
        t[i][0]=0
    for i in range(1,size+1):
        for j in range(1,S+1):
            if weights[i-1]<=j:
                t[i][j]=max(weights[i-1]+t[i-1][j-weights[i-1]] , t[i-1][j])
            else:
                t[i][j]=t[i-1][j]
    print(t[size][S])
w,n=map(int,input().split())
weights=list(map(int, input().split()))
value(weights,w)
