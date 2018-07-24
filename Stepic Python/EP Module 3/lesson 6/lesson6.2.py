import requests
with open("D:\WebDev Test\dataset_3378_3.txt", "r") as inf:
    req = requests.get(inf.readline().strip())
    while req.text[:2] != "We":
        req = requests.get("https://stepic.org/media/attachments/course67/3.6.3/" + req.text)
        res = req.text
with open("D:\WebDev Test\dataset_3378_3.txt", "w") as inf:
    inf.write(res)

