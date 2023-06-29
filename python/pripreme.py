import sys

inp = [[int(x) for x in l.strip().split()] for l in sys.stdin]

teams = {k: [inp[1][k], False, False] for k in range(inp[0][0])}
