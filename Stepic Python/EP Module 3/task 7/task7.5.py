table = {i:[0, 0] for i in range(1, 12)}
with open("D:\WebDev Test\dataset_3380_5.txt", "r") as inf:
    for s in inf:
        studentInf = s.strip().split()
        table[int(studentInf[0])][0] += int(studentInf[2])
        table[int(studentInf[0])][1] += 1
with open("D:\WebDev Test\dataset_3380_5.txt", "w") as inf:
    for i in table:
        if table[i] == [0, 0]:
            inf.writelines([str(i), " ", "-", "\n"])
        else:
            inf.writelines([str(i), " ", str(table[i][0] / table[i][1]), "\n"])
print("Complete")
