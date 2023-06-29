import sys
import math
inp = [[float(x) for x in l.strip().split()] for l in sys.stdin]
segs = int(inp[0].pop(0))
rings = int(inp[0].pop(0))
r = inp[0].pop(0)
s = (inp[1][0], inp[1][1])
e = (inp[1][2], inp[1][3])

def amsterdam_dist(segs, rings, r, s, e):
    angle = 180  * (abs(s[0] - e[0]) / segs)
    radius = r * (min(s[1], e[1]) / rings)
    inward = r * (abs(s[1] - e[1]) / rings)
    circumference = math.pi * radius
    perc = angle / 180 
    segDist = perc * circumference
    if inward == 0:
        return (r * (s[1] / rings) * 2)
    elif inward + segDist == 0:
        return 0
    return (inward + segDist)


print(amsterdam_dist(segs, rings, r, s, e))
