line1=input().split()
line2=input().split()
count1=int(line1[0])
count2=int(line2[0])
arr1=[int(x) for x in line1]
arr1.pop(0)
arr2=[int(x) for x in line2]
arr2.pop(0)

def BinarySearch(arr1,num):
    l=0
    h=len(arr1)-1
    #print(num,end=" ")
    while l<=h:
        mid=int((l+h)/2)
        if arr1[mid]==num:
            return mid
        elif arr1[mid]<num:
            l=mid+1
        else:
            h=mid-1
    return -1

for num in arr2:
    print(BinarySearch(arr1,num),end=" ")
