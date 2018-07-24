n = int(input())
seq = []
counter = 1
counterIn = 1
while len(seq) < n:
    while counter <= counterIn and len(seq) < n:
        seq.append(counterIn)
        counter += 1
    counter = 1
    counterIn += 1
for i in seq:
    print(i, end=" ")
