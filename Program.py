
def solve(s):
    s=s.strip()
    len1=len(s)
    temp=s.replace(" ","")
    len2=len(temp)
    print(len1-len2)
    if temp.isdigit() :
        return s
    words=s.split()
    print(len(words))
    result=""
    for w in words:
        result+=w[0].upper()+w[1:]+" "
    return result

s = input()
result = solve(s)
print(result)
