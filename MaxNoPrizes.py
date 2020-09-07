n = int(input())
if n == 1:
    print("1\n1")
    quit()
temp = n
prizes = []
for i in range(1, n):
    if temp>2*i:
        prizes.append(i)
        temp -= i
    else:
        prizes.append(temp)
        break
print(len(prizes))
for i in prizes:
    print(i,end=" ")
