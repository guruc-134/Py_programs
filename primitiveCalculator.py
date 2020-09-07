import math

n = int(input())
numList = [0, 0] + [math.inf]*(n-1)
for i in range(2, n+1):
    way1, way2, temp3 = [math.inf]*3

    way1 = numList[i-1] + 1
    if i%2 == 0: way2 = numList[i//2] + 1
    if i%3 == 0: temp3 = numList[i//3] + 1
    minSteps = min(way1, way2, temp3)
    numList[i] = minSteps

print(numList[n])

nums = [n]
while n!=1:
    if n%3 ==0 and numList[n]-1 == numList[n//3]:
        nums += [n//3]
        n = n//3
    elif n%2 ==0 and numList[n]-1 == numList[n//2]:
        nums += [n//2]
        n = n//2
    else:
        nums += [n-1]
        n = n - 1

print(' '.join([str(i) for i in nums][::-1]))
