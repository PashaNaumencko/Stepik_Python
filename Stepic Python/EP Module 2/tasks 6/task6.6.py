temp = []
lst = []
while "end" not in temp:
    temp = [i for i in input().split()]
    lst.append(temp)
lst.remove(["end"])
res = [[0 for j in range(len(lst[0]))] for i in range(len(lst))]
for i in range(len(lst)):
    for j in range(len(lst[i])):
        lst[i][j] = int(lst[i][j])
for i in range(len(lst)):
    for j in range(len(lst[i])):
        if i + 1 == len(lst) and j + 1 == len(lst[i]):
            res[i][j] = lst[i - 1][j] + lst[(i + 1) * -1][j] + lst[i][j - 1] + lst[i][(j + 1) * -1]
        elif i + 1 == len(lst):
            res[i][j] = lst[i - 1][j] + lst[(i + 1) * -1][j] + lst[i][j - 1] + lst[i][j + 1]
        elif j + 1 == len(lst[i]):
            res[i][j] = lst[i - 1][j] + lst[i + 1][j] + lst[i][j - 1] + lst[i][(j + 1) * -1]
        else:
            res[i][j] = lst[i - 1][j] + lst[i + 1][j] + lst[i][j - 1] + lst[i][j + 1]
for i in range(len(res)):
    for j in range(len(res[i])):
        print(res[i][j], end=" ")
    print()
