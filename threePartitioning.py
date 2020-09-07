def sum(nums,S):
    size=len(nums)
    t=[[False for i in range(S+1)] for j in range(size+1)]
    for i in range(S+1):
        t[0][i]=False
    for i in range(size+1):
        t[i][0]=True
    for i in range(1,size+1):
        for j in range(1,S+1):
            if nums[i-1]>=j:
                t[i][j]=max(t[i-1][j-nums[i-1]] or t[i-1][j])
            else:
                t[i][j]=t[i-1][j]
n=int(input())
nums=list(map(int, input().split()))
