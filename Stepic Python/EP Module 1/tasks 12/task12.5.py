a = int(input())
b = int(input())
c = int(input())
maxi = a
mini = a
if b > maxi:
    maxi = b
elif b < mini:
    mini = b
if c > maxi:
    maxi = c
elif c < mini:
    mini = c
print(maxi)
print(mini)
print(a + b + c - maxi - mini)