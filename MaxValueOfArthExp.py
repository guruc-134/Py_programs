import math
def compute(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    else:
        return a * b

def MinAndMax(M, m, i, j, symbol):
    minval = math.inf
    maxval = -math.inf
    for k in range(i, j):
        a = compute(M[i][k], M[k+1][j], symbol[k])
        b = compute(M[i][k], m[k+1][j], symbol[k])
        c = compute(m[i][k], M[k+1][j], symbol[k])
        d = compute(m[i][k], m[k+1][j], symbol[k])
        minval = min(minval, a, b, c, d)
        maxval = max(maxval, a, b, c, d)
    return minval, maxval


def MVAE(values, symbol):
    n = len(values)
    m = [[None for x in range(n)] for x in range(n)]
    M = [[None for x in range(n)] for x in range(n)]

    for i in range(n):
        m[i][i] = values[i]
        M[i][i] = values[i]

    for s in range(1, n):
        for i in range(0, n-s):
            j = i + s
            m[i][j], M[i][j] = MinAndMax(M, m, i, j, symbol)

    return M[0][n-1]


exp = input()
symbol, values = [], []

for i in exp:
    if i in ['+', '-', '*']:
        symbol.append(i)
    else:
        values.append(int(i))

print(MVAE(values, symbol))
