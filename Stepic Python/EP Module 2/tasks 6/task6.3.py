sum = 0
sumSq = 0
while True:
    a = int(input())
    sum += a
    sumSq += a ** 2
    if sum == 0:
        print()
        break
print(sumSq)