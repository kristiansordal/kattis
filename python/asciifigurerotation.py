import numpy as np
import sys

figs = []
fig = []
for x in sys.stdin:
    try:
        int(x.strip())
        figs.append(fig)
        fig = []
    except:
        fig.append(x.strip())

figs = np.array(figs[1:])
figs = figs.T 

arr = np.array([['a', 'b', 'c', 'd'], ['d', 'e', 'f']])
print(arr.T)
rotated = []
for fig in figs:
    f = []
    for line in fig:
        l = []
        for c in line:
            if c == '-':
                l.append('|')
            elif c == '|':
                l.append('-')
            elif c == '+':
                l.append('+')
            else:
                l.append(' ')

        f.append(l)
    rotated.append(f)
    

print(np.matrix(np.array(rotated[0])))

for fig in rotated:
    for line in fig:
        print(' '.join(line))
    print('\n')
# print()
        


