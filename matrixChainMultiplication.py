# %%
def matrixChainOrder(p, n):
    m = [[0 for x in range(n)] for x in range(n)]
    s = [[0 for x in range(n)] for x in range(n)]
    for i in range(1, n):
        m[i][i] = 0
    for L in range(2, n):
        for i in range(1, n-L+1):
            j = i+L-1
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    return m, s


def printOptimalParems(s, i, j):
    if i == j:
        print("A", i, end="")
    else:
        print("(", end="")
        printOptimalParems(s, i, s[i][j])
        printOptimalParems(s, s[i][j]+1, j)
        print(")", end="")


# example usage
p = [5, 4, 6, 2, 7]
n = len(p)
m, s = matrixChainOrder(p, n)
print("Minimum number of multiplications is", m[1][n-1])
# example usage of printOptimalParems
printOptimalParems(s, 1, n-1)
# %%
