"""file_name=input("enter the file name")
fh=open(file_name)
emails=dict()
for line in fh:
    if line.startswith("From") :
        if not line.startswith("From:"):
            words=line.split()
            emails[words[5][:2]]=emails.get(words[5][:2],0)+1
print(emails)
print()
print(emails.items())
lst=sorted(emails.items())
print(lst)

tmp=list()
for k,v in lst:
    print(k,v)
    tup=(v,k)
    tmp.append(tup)

newlist=sorted(tmp,reverse=False)
print(newlist)
for v,k in newlist:
    print(k,v)
"""
tup=tuple()
print(dir(tup))
