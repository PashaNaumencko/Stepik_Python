l = [int(i) for i in input().split()]
if len(l) == 1:
    print(l[0])
else:
    res = []
    for i in range(len(l)):
        if i == 0:
            res.append(l[i + 1] + l[-1])
        elif i == len(l) - 1:
            res.append(l[i - 1] + l[0])
        else:
            res.append(l[i - 1] + l[i + 1])
    for i in res:
        print(i, end=" ")

