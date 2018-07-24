n = int(input())
d = {}
for i in range(n):
    x = int(input())
    if x not in d.keys():
        print(f(x))
        d[x] = f(x)
    else:
        print(d[x])