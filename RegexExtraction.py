import re
hand=open('text.txt')
S=0
for line in hand:
    line=line.strip()
    y=re.findall('([0-9]+)',line)
    if len(y)==0:
        continue
    S+=sum([int(x) for x in y])
print(S)
