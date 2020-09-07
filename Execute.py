def findTargetSumWays( nums,S):
    n=len(nums)
    h=[{} for i in range(n+1)]
    print("---------     -------\n",h)
    def helper(s,i):
        if i==n:
            return 1 if s==S else 0
        if s in h[i]:
            return h[i][s]
        h[i][s]=helper(s+nums[i], i+1)+helper(s-nums[i], i+1)
        return h[i][s]
    return helper(0,0)

print(findTargetSumWays([1, 1, 1, 1, 1],3))
