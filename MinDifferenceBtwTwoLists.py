def findMinDiff(ind0,ind1)
    result=math.inif
    arr1.sort()
    arr0.sort()
    a = 0
    b = 0
    m=len(arr0)
    n=len(arr1)
    while a < m and b < n :
        if (abs(arr0[a] - arr1[b]) < result):
            result = abs(arr0[a] - arr1[b])
        if (arr0[a] < arr1[b]):
            a += 1
        else:
            b += 1
    return result-1
# pass two lists to this function and  this function will return the minimum difference
# between any two elements in the lists
