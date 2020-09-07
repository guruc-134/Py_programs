lst=list()
for i in range(200):
    data=input().split(" ")
    lst.append(data[-1])
lst.sort(reverse=True)
index=lst.index('9.64')
print(index)
