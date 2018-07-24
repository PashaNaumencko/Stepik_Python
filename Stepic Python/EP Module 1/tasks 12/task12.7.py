n = int(input())
left = n // 1000
right = n % 1000
leftSum = left // 100 + (left % 100) // 10 + left % 10
rightSum = right // 100 + (right % 100) // 10 + right % 10
if leftSum == rightSum:
    print("Счастливый")
else:
    print("Обычный")
