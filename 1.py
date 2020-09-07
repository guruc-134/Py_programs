n=int(input())
ip=input().split()
lsb=list()
num=list()
for i in range(n):
    num.append(int(ip[i]))
    lsb.append(num[i] and -num[i])
print(lsb)
