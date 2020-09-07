"""
gurus algorithm
"""
n=int(input())#number of items of the list
if n==0:
    print("0")
    exit()
start=list()
end=list()
for i in range(n):
    t=input().split()
    start.append(int(t[0]))
    lst=list()
    lst.append(int(t[1]))
    lst.append(i)
    end.append(lst)
print(end)
end.sort()
print(end)
print(start)
index=0
answerCount=0
ans=list()
while index<n:
    if end[index][0]!=-1:
        key=end[index][0]
        for i in range(n):
            if start[i]<=key:
                for j in range(n):
                    if end[j][1]==i:
                        end[j][0]=-1
            i+=1
        answerCount+=1
        ans.append(key)
    index+=1
print(answerCount)
for points in ans:
    print(points,end=" ")
