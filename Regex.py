import re
fh=open("text.txt")
lst=list()
sum=0
for line in fh:
    line=line.rstrip()
    y=re.findall('[0-9]+',line)
    if len(y)==0:
        continue
    for num in y:
        sum+=int(num)
print(sum)
