"""
idea is to add the numbers starting from one to the list
till the sum of the list is less than half of the number value
and then the next num would ne n-sum
"""
"""
num=int(input())
sum=0
i=1
lst=list()
if num==2:
    print("1\n2")
    exit()
while True:
    if sum<=int(num/2):
        sum+=i
        lst.append(i)
        i+=1
        if sum==num:
            break
    else:
        a=num-sum
        print(a)
        while True:
            l=lst[-1]+1
            print(l)
            p=a-l
            if p not in lst:
                print(p)
                lst.append(min(p,l))
                lst.append(max(p,l))
            else:
                break
        if a in lst:
            p=int(lst.pop())
            lst.append(a+p)
            break
        else:
            lst.append(num-sum)
        break
print(len(lst))
print(lst)
"""
