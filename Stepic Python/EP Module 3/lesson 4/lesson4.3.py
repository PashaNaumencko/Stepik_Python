studentAverage = []
totalSum = [0, 0, 0]
counter = 0
with open("D:\WebDev Test\dataset_3363_4.txt", "r") as inf:
    for s in inf:
        seq = s.strip().split(";")
        studentAverage.append((int(seq[1]) + int(seq[2]) + int(seq[3])) / 3)
        totalSum[0] += int(seq[1])
        totalSum[1] += int(seq[2])
        totalSum[2] += int(seq[3])
        counter += 1
with open("D:\WebDev Test\dataset_3363_4.txt", "w") as inf:
    for i in studentAverage:
        inf.write(str(i))
        inf.write("\n")
with open("D:\WebDev Test\dataset_3363_4.txt", "a") as inf:
    inf.write(str(totalSum[0] / counter))
    inf.write(" ")
    inf.write(str(totalSum[1] / counter))
    inf.write(" ")
    inf.write(str(totalSum[2] / counter))
print("Complete")

