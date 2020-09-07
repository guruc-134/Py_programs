text1=input()
n1=len(text1)
text2=input()
n2=len(text2)
cols=n1
rows=n2
t=[[0 for i in range(cols+1)] for j in range(rows+1)]
for i in range(cols):
    t[i][0]=i
for j in range(rows):
    t[0][j]=j
#print(t)
#print(cols)
for i in range(1,rows+1):
  for j in range(1,cols+1):
      ins=t[i][j-1]+1
      dele=t[i-1][j]+1
      mismatch=t[i-1][j-1]+1
      match=t[i-1][j-1]
      if text1[j-1]==text2[i-1]:
          t[i][j]=min(ins,dele,match)
      else:
          t[i][j]=min(ins,dele,mismatch)

print(t[rows][cols])


"""if text1[j-1]==text2[i-1]:
    t[i][j]=t[i-1][j-1]

else:
    t[i][j]=min(t[i-1][j]+1,t[i][j-1]+1)"""
