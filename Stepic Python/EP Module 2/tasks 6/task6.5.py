lst = [int(i) for i in input().split()]
x = int(input())
res = []
for i in range(len(lst)):
    if lst[i] == x:
       res += [i]
if len(res) == 0:
    print("Отсутствует")
else:
    for i in res:
        print(i, end=" ")