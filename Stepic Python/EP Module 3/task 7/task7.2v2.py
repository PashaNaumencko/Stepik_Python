firstAlph, lastAlph, encryptedString, cryptedString = list(input()), list(input()), list(input()), list(input())
for i in range(len(encryptedString)):
    encryptedString[i] = lastAlph[firstAlph.index(encryptedString[i])]
for i in range(len(cryptedString)):
    cryptedString[i] = firstAlph[lastAlph.index(cryptedString[i])]
print(str().join(encryptedString))
print(str().join(cryptedString))