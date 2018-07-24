x = int(input())
h = int(input())
m = int(input())
#if(x % 60 + m) > 60:
#    h += 1
#    m -= 60
print((x + h * 60 + m) // 60)
print((x + h * 60 + m) % 60)

