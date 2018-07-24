a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(end="\t")
for i in range(a - 1, b + 1):
    for j in range(c, d + 1):
        if i == a - 1:
            print(j, end="\t")
        else:
            print(i  * j, end="\t")
    if i != b:
        print()
        print(i + 1, end="\t")
