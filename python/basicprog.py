import sys
import string
inp = [[int(x) for x in l.strip().split()] for l in sys.stdin]

c = inp[0][1]
a = inp[1]

if c == 1:
        print(7)
elif c == 2:
    if a[0] > a[1]: print('Bigger')
    elif a[0] == a[1]: print('Equal')
    else: print('Smaller')
elif c ==  3:
    print(sorted(a[0:2])[1])
elif c ==  4:
    print(sum(a))
elif c ==  5:
    print(sum(list(filter(lambda x: x % 2 == 0, a ))))
elif c ==  6:
    mod = list(map(lambda x: string.ascii_lowercase[x], map(lambda x: x % 26, a)))
    print(''.join(mod))
elif c ==  7:
    i = 0
    seen = {k : False for k in a}
    while True:
        if i > len(a) - 1:
            print('Out')
            break
        if i == len(a) - 1:
            print('Done')
            break
        if seen[i] == True:
            print('Cyclic')
            break
        seen[i] = True
        i = a[i]



