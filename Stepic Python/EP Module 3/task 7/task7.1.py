table = {}
for i in range(int(input())):
    match = input().split(";")
    if match[0] not in table.keys():
        table[match[0]] = [0, 0, 0, 0, 0]
    if match[2] not in table.keys():
        table[match[2]] = [0, 0, 0, 0, 0]
    table[match[0]][0] += 1
    table[match[2]][0] += 1
    if match[1] > match[3]:
        table[match[0]][1] += 1
        table[match[2]][3] += 1
        table[match[0]][4] += 3
    elif match[3] > match[1]:
        table[match[2]][1] += 1
        table[match[0]][3] += 1
        table[match[2]][4] += 3
    else:
        table[match[0]][2] += 1
        table[match[2]][2] += 1
        table[match[0]][4] += 1
        table[match[2]][4] += 1
for i in table.keys():
    print(i, end=":")
    for j in table[i]:
        print(j, end=" ")
    print()
