n = int(input())
lst = [int(i) for i in input().split()]


def IsGreaterOrEqual(digit, max_digit):
    return int(str(digit)+str(max_digit))>=int(str(max_digit)+str(digit))

def largestnumber(lst):
    answer = []

    while lst!=[]:
        print("pass:\n")
        max_digit = 0
        for digit in lst:
            print("digit",digit)
            if IsGreaterOrEqual(digit, max_digit):
                max_digit = digit
                print("\ndig max:",max_digit)
        answer.append(max_digit)
        lst.remove(max_digit)
    print("\nanswer",answer)
    return answer

print(''.join([str(i) for i in largestnumber(lst)]))
