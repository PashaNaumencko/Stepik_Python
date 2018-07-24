firstAlph, lastAlph = input(), input()
encryptedStringToList, cryptedStringToList = list(input()), list(input())
ecryptedDict = dict(zip(firstAlph, lastAlph))
cryptedDict = dict(zip(lastAlph, firstAlph))
for i in range(len(encryptedStringToList)):
    if encryptedStringToList[i] in ecryptedDict.keys():
        encryptedStringToList[i] = ecryptedDict[encryptedStringToList[i]]
for i in range(len(cryptedStringToList)):
    if cryptedStringToList[i] in cryptedDict.keys():
        cryptedStringToList[i] = cryptedDict[cryptedStringToList[i]]
print(str().join(encryptedStringToList))
print(str().join(cryptedStringToList))

