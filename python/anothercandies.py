import sys

inp = sys.stdin.read().split("\n\n")[1:]
inp = [[int(x) for x in l.split()] for l in inp]
for i in inp:
    if sum(i[1:]) % i[0] == 0:
        print("YES")
    else:
        print("NO")
