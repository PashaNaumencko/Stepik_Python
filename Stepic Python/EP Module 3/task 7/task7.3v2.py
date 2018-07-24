dictionary = {input().lower() for i in range(int(input()))}
ltext = []
for j in range(int(input())):
    ltext += input().lower().split()
ltext = set(ltext)
print("\n".join(ltext - dictionary))