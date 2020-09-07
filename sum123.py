dic={}
for i in list(map(int,input().split())):
    dic[i]=1+dic.get(i,0)
for i in sorted(dic ,key=lambda k: (dic[k],arr.index(k))):
    for j in range(dic[i]):
        print(i,end=" ")
