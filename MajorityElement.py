n=int(input())
nums=[int(x) for x in input().split()]
count=1
majority=nums[0]
for i in range(1,n):

    if nums[i]==majority:
        count+=1

    else:
        count-=1
    if count==0:
        majority=nums[i]
        count=1
print(majority)
count=0
for i in nums:
    if i==majority:
        count+=1
if count>n/2:
    print('1')
else :
    print('0')
