
def merge(left, right):
    i, j, invc = 0, 0, 0
    final = list()
    while i < len(left) and j< len(right):
        if left[i] <= right[j]:
            final.append(left[i])
            i += 1
        else:
            final.append(right[j])
            invc += len(left) - i
            j += 1

    final += left[i:]
    final += right[j:]

    return final, invc

def MergeSort(arr):
    global invcTotal
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2

    left = MergeSort(arr[:mid])
    right = MergeSort(arr[mid:])
n
    sorted_arr, invc = merge(left, right)
    invcTotal += invc

    return sorted_arr

invcTotal = 0
n = int(input())
seq = [int(i) for i in input().split()]
MergeSort(seq)
print(invcTotal)
