def NSL(heights):
    left=[]
    stack=[]
    for i in range(len(heights)):
        if stack==[]:
            left.append(-1)
        elif stack[-1][0]<heights[i]:
            left.append(stack[-1][1])
        else:
            while len(stack)!=0 and stack[-1][0]>=heights[i]:
                stack.pop(-1)
            if stack==[]:
                left.append(-1)
            else:
                left.append(stack[-1][1])
        stack.append([heights[i],i])
    return left
def NSR(heights):
    right=[]
    stack=[]
    for i in range(len(heights)-1,-1,-1):
        if stack==[]:
            right.append(len(heights))
        elif stack[-1][0]<heights[i]:
            right.append(stack[-1][1])
        else:
            while len(stack)!=0 and stack[-1][0]>=heights[i]:
                stack.pop(-1)
            if stack==[]:
                right.append(len(heights))
            else:
                right.append(stack[-1][1])
        stack.append([heights[i],i])
    right.reverse()
    return right
def MAH(heights):
    left=NSL(heights)
    right= NSR(heights)
    print("right",right)
    print("left",left)
    M=0
    for i in range(len(heights)):
        Area=heights[i]*(right[i]-left[i]-1)
        M=max(Area,M)
    print('area',M)
    return M
rows=4
arr= [list(map(int,input().split())) for y in range(rows)]
lst=arr[0][:]
maxArea=MAH(lst)
for i in range(1,rows):
    for j in range(len(arr[0])):
        if arr[i][j]==0:
            lst[j]=0
        else:
            lst[j]+=arr[i][j]
    print(lst)
    maxArea=max(maxArea,MAH(lst))
print(maxArea)
