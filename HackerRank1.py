# given string and k value k is the length of the substring

AABCAAADA
li=list()
ll=list()
count=1
for i in string:
    print("actual",i)
    if count==k:
        li.append(ll)
        print("li",li)
        ll.clear()
    print("ll",ll)
    if i not in ll:
        print("selected",i)
        ll.append(i)
        count+=1
print(li)
