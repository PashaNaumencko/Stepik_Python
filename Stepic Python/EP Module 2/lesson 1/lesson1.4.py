a = int(input())
b = int(input())
num1 = a
num2 = b
while num1 != num2:
    if num1 > num2:
        num1 -= num2
    else:
        num2 -= num1
print((a * b) // num1)