res = ""
with open("D:\WebDev Test\dataset_3363_2.txt", "r") as inf:
    s = inf.readline().strip()
    print(s)
    for i in range(len(s)):
        if i == len(s) - 2:
            res += s[i] * int(s[i + 1])
        elif s[i].isalpha():
            if s[i + 2].isdigit():
                res += s[i] * int(s[i + 1] + s[i + 2])
            else:
                res += s[i] * int(s[i + 1])
with open("D:\WebDev Test\dataset_3363_2.txt", "w") as inf:
    inf.write(res)
print("Complete")
