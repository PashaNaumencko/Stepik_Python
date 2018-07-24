s = input().lower().split()
d = {}
for i in s:
    d[i] = s.count(i)
for i in d.keys():
    print(i, d[i], end="\n")

