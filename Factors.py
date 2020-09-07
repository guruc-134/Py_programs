
import math
i=int(input("enter a number to find its factors\n"))

for c in range(1,int(math.sqrt(i/1))+1):
    if i%c==0:
        print(c,int(i/c))
