l = [int(i) for i in input().split()]
res = []
l.sort()
for i in l:
    if l.count(i) > 1 and i not in res:
        res.append(i)
for i in res:
    print(i, end=" ")