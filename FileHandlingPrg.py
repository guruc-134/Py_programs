fh=open("sampletext.txt")
list=list()
count=0
for line in fh :
    if line.startswith('From:') :
        list=line.split()
        print(str(list[1]))
        count+=1
print(count)
