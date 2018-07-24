firstAlph, lastAlph, encryptedString, cryptedString = list(input()), list(input()), list(input()), list(input())
print("".join(lastAlph[firstAlph.index(encryptedString[i])] for i in range(len(encryptedString))))
print("".join(firstAlph[lastAlph.index(cryptedString[i])] for i in range(len(cryptedString))))