import numpy as np
def lcs(text1,text2,text3):
    n1=len(text1)
    n2=len(text2)
    n3=len(text3)
    #t=np.zeros(n1+1 ,n2+1,n3+1
    t=[[ [0 for col in range(n3+1)] for col in range(n2+1)] for row in range(n1+1)]
    for i in range(1,n1+1):
      for j in range(1,n2+1):
          for k in range(1,n3+1):
              if text1[i-1]==text2[j-1]==text3[k-1]:
                  t[i][j][k]=1+t[i-1][j-1][k-1]
              else:
                  t[i][j][k]=max(t[i-1][j][k],t[i][j-1][k],t[i][j][k-1])

    i=n1
    j=n2
    k=n3
    lcs=""
    while i>0 and j>0 and k>0:
        if text1[i-1]==text2[j-1]==text3[k-1]:
            lcs+=str(text1[i-1])
            i-=1
            j-=1
            k-=1

        if  t[i-1][j][k]>t[i][j-1][k]:
            if t[i-1][j][k]>t[i][j][k-1]:
                i-=1
            else:
                k-=1
        else:
            if t[i][j-1][k]> t[i][j][k-1]:
                j-=1
            else:
                k-=1
    return lcs[::-1]
n1=int(input())
text1=[int(x) for x in input().split()]
n2=int(input())
text2=[int(x) for x in input().split()]
n3=int(input())
text3=[int(x) for x in input().split()]
lcsAns=lcs(text1,text2,text3)
print(len(lcsAns))
