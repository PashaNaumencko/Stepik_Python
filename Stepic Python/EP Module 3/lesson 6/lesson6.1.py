import requests
with open("D:\WebDev Test\dataset_3378_2.txt", "r") as inf:
    r = requests.get(inf.readline().strip())
    res = r.text.splitlines()
with open("D:\WebDev Test\dataset_3378_2.txt", "w") as inf:
    inf.write(str(len(res)))
print("Complete")