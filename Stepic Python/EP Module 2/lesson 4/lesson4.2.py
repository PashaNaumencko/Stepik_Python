s = input()
temp = s[0]
counter = 1
for i in s[1:]:
    if i != temp:
        print(temp + str(counter), end='')
        temp = i
        counter = 1
    else:
        counter += 1
print(temp + str(counter))