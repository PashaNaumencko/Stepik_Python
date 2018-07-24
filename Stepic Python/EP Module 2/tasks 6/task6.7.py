n = int(input())
mtx = [[0 for j in range(n)] for i in range(n)]
i = 0
j = 0
di = 0
dj = 1
for k in range(1, n ** 2 + 1):
    mtx[i][j] = k
    if 0 <= i + di < n and 0 <= j + dj < n and mtx[i + di][j + dj] == 0:
        i += di
        j += dj
    else:
        di, dj = dj, -di
        i += di
        j += dj
for i in range(len(mtx)):
    for j in range(len(mtx[i])):
        print(mtx[i][j], end=" ")
    print()