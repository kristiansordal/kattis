p = int(input())
a = int(input())
b = int(input())

max_kills = p // a
max_assists = p // b

# combs.append((max_kills))

combs = []
for i in range(max_kills):
    diff = p - i * a
    combs.append((i, diff // b))
    # for j in range(max_assists, 0, -1):
    #     if i * a + j * b == p:
    #         combs.append((i, j))
print(len(combs))

for l in combs:
    print(" ".join(str(x) for x in l))
