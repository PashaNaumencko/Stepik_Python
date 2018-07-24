objects = [1, 2, 1, 2, 3]
uniqIdSet = set()
for i in objects:
    if i not in uniqIdSet:
        uniqIdSet.add(i)
print(len(uniqIdSet))