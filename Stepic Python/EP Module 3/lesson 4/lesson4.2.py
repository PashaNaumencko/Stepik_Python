with open("D:\WebDev Test\dataset_3363_3.txt", "r") as inf:
        s = inf.read().strip().lower().split()
d = {}
for i in s:
    d[i] = s.count(i)
maxValue = max(d.values())
maxKeys = []
for i in d.keys():
    if d[i] == maxValue:
        maxKeys.append(i)
print(sorted(maxKeys)[0], d[sorted(maxKeys)[0]])
with open("D:\WebDev Test\dataset_3363_3.txt", "w") as inf:
    inf.write(sorted(maxKeys)[0] + " " + str(d[sorted(maxKeys)[0]]))
print("Complete")
