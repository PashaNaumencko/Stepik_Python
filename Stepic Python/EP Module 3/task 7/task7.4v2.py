d = {"север": 0, "юг": 0, "восток": 0, "запад": 0}
for i in range(int(input())):
    command = input().split()
    d[command[0]] += int(command[1])
print(d["восток"] - d["запад"], d["север"] - d["юг"])
