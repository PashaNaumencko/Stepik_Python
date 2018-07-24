dictionary = {input().lower() for i in range(int(input()))}
ltext = set()
for j in range(int(input())):
    ltext.update(input().lower().split())
print("\n".join(ltext - dictionary))