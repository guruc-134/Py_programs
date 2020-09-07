lst=list()
for _ in range(int(input())):
    name = input()
    score = float(input())
    l=list()
    l.append(name)
    l.append(score)
    lst.append(l)

newlist=list()
for name,marks in lst:
    l=list()
    l.append(marks)
    l.append(name)
    newlist.append(l)
newlist.sort()

min=newlist[0][0]
secondmin=0
for marks,names in newlist:
    if marks >min:
        secondmin=marks
        break
for marks,names in newlist:
    if marks==secondmin:
        print(names)
