""" input consists of three lines
 number of slots ---n
 n activities
 n clicks per slots"""
 #outout is the max profit
n=int(input())
if n==0:
     print("0")
     exit()
act=input().split()
clicksPerDay=input().split()
a=list()
cpd=list()
for i in range(n):
    a.append(int(act[i]))
    cpd.append(int(clicksPerDay[i]))
#print(a)
#print(cpd)
a.sort()
cpd.sort()
profit=0
for i in range(n):
    profit+=a[i]*cpd[i]
print(profit)
